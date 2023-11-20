import base64
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django_filters import rest_framework as filters
from django.views import generic

from rest_framework import viewsets, generics
from rest_framework import views
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from webbolid.filters import PLogDataFilter
from webbolid.forms import PListSearchForm, PlistForm
from webbolid.models import Plist, Plogdata
from webbolid.serializers import PListSerializer, PlistPictureSerializer, PLogDataSerializer


class PListView(generic.ListView):
    model = Plist
    context_object_name = 'list'
    # ordering = ['name']
    paginate_by = 15


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


class SearchListViews(PListView):
    model = Plogdata
    template_name = 'webbolid/search_list.html'
    context_object_name = 'search'  # имя списка

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filter'] = PLogDataFilter(
    #         self.request.GET, queryset=self.get_queryset())
    #     return context
    def get_queryset(self):
        queryset = super().get_queryset()
        return PLogDataFilter(self.request.GET, queryset=queryset).qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['time_now'] = datetime.now()
        context['filter'] = PLogDataFilter(
            self.request.GET, queryset=self.get_queryset())
        return context



# class PListViewSet(viewsets.ModelViewSet):
#     queryset = Plist.objects.all()
#     serializer_class = PListSerializer
#     filter_backends = [filters.DjangoFilterBackend, ]
#     filterset_fields = ["name", "company", "post"]
#
#
# class PlistPictureView(APIView):
#
#     def get(self, request, pk):
#         plist = get_object_or_404(Plist, pk=pk)
#         serializer = PlistPictureSerializer(plist, context={'request': request})
#         picture_url = serializer.data['picture_url']
#         name = serializer.data['name']
#         firstname = serializer.data['firstname']
#         midname = serializer.data['midname']
#         workphone = serializer.data['workphone']
#         homephone = serializer.data['homephone']
#         company = serializer.data['company']
#         post = serializer.data['post']
#         tabnumber = serializer.data['tabnumber']
#         pk = serializer.data['id']
#         return render(request,
#                       'plist_picture.html',
#                       {
#                           'picture_url': picture_url,
#                           'name': name,
#                           'firstname': firstname,
#                           'midname': midname,
#                           'workphone': workphone,
#                           'homephone': homephone,
#                           'company': company,
#                           'post': post,
#                           'tabnumber': tabnumber,
#                           'pk': pk,
#                       })
#
#
# class PlistDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Plist.objects.all()
#     # serializer_class = PlistPictureSerializer
#     serializer_class = PListSerializer
#
#     def get_object(self):
#         return get_object_or_404(Plist, pk=self.kwargs.get('pk'))
#
#
# class PLogDataViewSet(viewsets.ModelViewSet):
#     queryset = Plogdata.objects.select_related("hozorgan", "event").order_by('-devicetime')
#     serializer_class = PLogDataSerializer
#     filter_backends = [filters.DjangoFilterBackend, ]  # filters.SearchFilter]
#     filterset_class = PLogDataFilter
#
#
# class PListSearchView(generics.ListCreateAPIView):
#     queryset = Plist.objects.all()
#     serializer_class = PListSerializer  # Замените YourSerializer на ваш сериализатор для модели Plist
#     pagination_class = PageNumberPagination  # Используем PageNumberPagination
#
#     def get(self, request, *args, **kwargs):
#         form = PListSearchForm(request.GET)
#         queryset = self.get_queryset()
#
#         if form.is_valid():
#             for field, value in form.cleaned_data.items():
#                 if value:
#                     lookup = f"{field}__icontains"
#                     queryset = queryset.filter(**{lookup: value})
#
#         page = self.paginate_queryset(queryset)
#
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             context = {
#                 'form': form,
#                 'data': serializer.data,
#                 'paginator': self.pagination_class,
#                 'page_obj': page,
#             }
#             return render(request, 'plist_search_results.html', context)
#
#         serializer = self.get_serializer(queryset, many=True)
#         context = {'form': form, 'data': serializer.data}
#         return render(request, 'plist_search_results.html', context)

