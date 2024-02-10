import base64
from datetime import datetime

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views import generic
from django_filters.views import FilterView

from webbolid.filters import PLogDataFilter, PlistFilter
from webbolid.forms import PlistForm, SearchForm
from webbolid.models import Plist, Plogdata
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
    template_name = 'webbolid/search_list.html'
    context_object_name = 'search'
    ordering = ['devicetime']
    # form_class = SearchForm

    @method_decorator(cache_page(60 * 1))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        return PLogDataFilter(
            self.request.GET,
            queryset=queryset).qs.only(
            'timeval', 'event', 'hozorgan',
            'remark', 'devicetime', 'guid'
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filters = PLogDataFilter(self.request.GET, queryset=self.get_queryset())
        context['filter'] = filters

        paginator = Paginator(filters.qs, 10)
        page = self.request.GET.get('page')

        try:
            search_results = paginator.page(page)
        except PageNotAnInteger:
            search_results = paginator.page(1)
        except EmptyPage:
            search_results = paginator.page(paginator.num_pages)

        context['search'] = search_results
        return context
# ================================================================================
