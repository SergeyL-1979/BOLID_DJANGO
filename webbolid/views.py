import base64
from datetime import datetime
from idlelib.iomenu import errors

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count, F, Avg
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views import generic
from django_filters.views import FilterView

from webbolid.filters import PLogDataFilter, PlistFilter
from webbolid.forms import PlistForm
from webbolid.models import Plist, Plogdata, Pmark
from webbolid.serializers import PListSerializer, PlistPictureSerializer, PLogDataSerializer


# ======= Добавлен код для поиска на странице по имени ==================
# def plist_list(request):
#     f = PlistFilter(request.GET, queryset=Plist.objects.all())
#     return render(request, 'webbolid/plist_list.html', {'filter': f})


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
class PMarkView(generic.ListView):
    model = Pmark
    context_object_name = 'codes'
    template_name = 'webbolid/encode_code.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()

        # Обработка каждого объекта и конвертация кода
        for obj in queryset:
            raw_value = obj.codep

            try:
                # Конвертируем строку в байты с кодировкой cp1251
                byte_value = raw_value.encode('Windows-1251', errors='ignore')
                # byte_value = raw_value.encode('cp1251', errors='ignore')
                # Отбрасываем первый байт
                modified_bytes = byte_value[1:]
                # Заменяем пары байт FE01 на 00
                modified_bytes = modified_bytes.replace(b'\xFE\x01', b'\x00')
                # Переворачиваем байты
                reversed_bytes = modified_bytes[::-1]
                reversed_bytes = reversed_bytes.replace(b'\x03\xFE', b'\x20')
                # Преобразуем в шестнадцатеричное представление
                hex_representation = reversed_bytes.hex().upper()

            except Exception as e:
                hex_representation = f"Ошибка преобразования: {str(e)}"

            # Сохраняем преобразованное значение в объекте
            obj.converted_code = hex_representation

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Передаем список с преобразованными кодами в контекст
        context['codes'] = self.get_queryset()
        return context
