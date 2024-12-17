import base64

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count, Q, Sum, Case, When, F, ExpressionWrapper, fields
from django.views import generic
from django_filters.views import FilterView
from django.db.models.functions import TruncDay, TruncMonth

from webbolid.filters import PLogDataFilter, PlistFilter, TimeFilter
from webbolid.forms import PlistForm
from webbolid.models import Plist, Plogdata, Pmark, Groups, Pcompany


# ======= Добавлен код для поиска на странице по имени ==================
class PlistListFilter(FilterView):
    filterset_class = PlistFilter
    queryset = Plist.objects.all()
    template_name = 'webbolid/plist_search.html'
    ordering = ['name']
    paginate_by = 5
# ==========================================================================


class PListView(generic.ListView):
    model = Plist
    context_object_name = 'list'
    ordering = ['name']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filter'] = PlistFilter(self.request.GET, queryset=Plist.objects.all())
        return context


class PListDetailView(generic.DetailView):
    model = Plist
    context_object_name = 'list_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.get_encoded_images()
        return context

    def get_encoded_images(self):
        images = []
        obj = self.object
        if obj.picture:
            image_base64 = base64.b64encode(obj.picture).decode('utf-8')
            images.append({
                'obj': obj,
                'image_base64': image_base64,
            })
        return images


class PListUpdateView(generic.UpdateView):
    form_class = PlistForm
    context_object_name = 'list_update'
    template_name = 'webbolid/plist_update.html'

    def get_queryset(self):
        return Plist.objects.all()


# ================= ПОИСК В ТАБЛИЦЕ PLOGDATA ============================
class SearchListView(generic.ListView):
    model = Plogdata
    template_name = 'webbolid/search_data.html'
    context_object_name = 'search'
    ordering = ['devicetime']
    paginate_by = 8

    # @method_decorator(cache_page(60 * 1))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        return PLogDataFilter(
            self.request.GET,
            queryset=queryset).qs.only(
            'timeval', 'event', 'hozorgan',
            'remark', 'devicetime', 'doorindex'
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filters = PLogDataFilter(self.request.GET, queryset=self.get_queryset())
        queryset = Plogdata.objects.values('hozorgan__name', 'event').annotate(count=Count('event'))
        context['filter'] = filters

        paginator = Paginator(filters.qs, 6)
        page = self.request.GET.get('page')

        try:
            search_results = paginator.page(page)
        except PageNotAnInteger:
            search_results = paginator.page(1)
        except EmptyPage:
            search_results = paginator.page(paginator.num_pages)

        context['search'] = search_results
        context['group'] = queryset
        return context
# ================================================================================


# ======== ввывод кода карты ========
class PMarkSearchByNameView(generic.ListView):
    model = Pmark
    context_object_name = 'codes'
    template_name = 'webbolid/encode_code.html'
    paginate_by = 10

    def get_queryset(self):
        """
        Фильтрация данных на основе GET-параметров запроса.
        """
        queryset = Pmark.objects.select_related('owner', 'groupid')  # Используем select_related для оптимизации
        # Получаем параметры фильтрации из запроса
        tab_number = self.request.GET.get('tab_number')  # Табельный номер
        name = self.request.GET.get('name')  # Имя
        surname = self.request.GET.get('surname')  # Фамилия
        midname = self.request.GET.get('midname')  # Отчество
        gtype = self.request.GET.get('gtype')  # Тип пропуска
        group_id = self.request.GET.get('group_id')  # Группа
        company_id = self.request.GET.get('company_id')  # Компания
        status = self.request.GET.get('status')  # Статус карты

        # Добавляем условия фильтрации
        q_filters = Q()
        if tab_number:
            q_filters &= Q(owner__tabnumber__icontains=tab_number)
        if name:
            q_filters &= Q(owner__firstname__icontains=name)
        if surname:
            q_filters &= Q(owner__name__icontains=surname)
        if midname:
            q_filters &= Q(owner__midname__icontains=midname)
        if gtype:
            q_filters &= Q(gtype=gtype)
        if group_id:
            q_filters &= Q(groupid__id=group_id)
        if company_id:
            q_filters &= Q(owner__company__id=company_id)
        if status:
            q_filters &= Q(status=status)
        # return queryset.filter(q_filters)
        # Фильтруем данные
        queryset = queryset.filter(q_filters)
        # Конвертация кода для каждого объекта
        for obj in queryset:
            raw_value = obj.codep  # Исходное значение кода карты

            try:
                # Конвертируем строку в байты с кодировкой cp1251
                byte_value = raw_value.encode('Windows-1251', errors='ignore')
                # Отбрасываем первый байт
                modified_bytes = byte_value[1:]
                # Заменяем пары байт FE01 на 00
                modified_bytes = modified_bytes.replace(b'\xFE\x01', b'\x00')
                # Переворачиваем байты
                reversed_bytes = modified_bytes[::-1]
                # Заменяем пары байт 03FE на 20
                reversed_bytes = reversed_bytes.replace(b'\x03\xFE', b'\x20')
                # Преобразуем в шестнадцатеричное представление
                hex_representation = reversed_bytes.hex().upper()
                # Сохраняем преобразованный код в объекте
                obj.converted_code = hex_representation

            except UnicodeEncodeError as e:
                print(f"Encoding error for {obj.id}: {e}")
                obj.converted_code = None  # В случае ошибки сохраняем None

        return queryset

    def get_context_data(self, **kwargs):
        """
        Добавляем дополнительные данные для отображения в шаблоне.
        """
        context = super().get_context_data(**kwargs)
        context['groups'] = Groups.objects.all()  # Список групп для фильтрации
        context['companies'] = Pcompany.objects.all()  # Список компаний
        context['filters'] = self.request.GET  # Передаём текущие фильтры для шаблона
        return context


# =========== УЧЕТ РАБОЧЕГО ВРЕМЕНИ =====================
class WTAView(generic.ListView):
    model = Plogdata
    context_object_name = 'worktime'
    template_name = 'webbolid/worktime_account.html'

    def get_queryset(self):
        queryset = super().get_queryset().filter(event=32)
        return TimeFilter(
            self.request.GET,
            queryset=queryset).qs.only(
            'timeval', 'event', 'hozorgan',
            'mode', )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        filterstime = TimeFilter(self.request.GET, queryset=self.get_queryset())
        # queryset = Plogdata.objects.values('mode').annotate(count=Count('event')).filter(event=32)
        context['filter'] = filterstime

        return context

