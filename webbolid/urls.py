from django.urls import path, include
from rest_framework import routers

from webbolid.views import (
    PListView, PListDetailView,
    PListUpdateView, SearchListView, PlistListFilter, )
from webbolid import views

# from webbolid.views import PListViewSet, PlistPictureView, PlistDetailView, PLogDataViewSet, \
#     PListSearchView, PListView, PListDetailView

# router = routers.DefaultRouter()
# router.register('list', PListViewSet, basename='p_list')
# router.register('p-log-data', PLogDataViewSet, basename='log_data')


urlpatterns = [
    # path('', include(router.urls)),
    path('', PListView.as_view(), name='list'),
    path('p-list/<int:pk>/', PListDetailView.as_view(), name='list_detail'),
    path('p-list/<int:pk>/update/', PListUpdateView.as_view(), name='list_update'),
    path('search/', SearchListView.as_view(), name='search_results'),
    # ==== добавили поиск по имени =============
    path('search/list/', PlistListFilter.as_view(), name='search_list'),
    # path('plogdata/', PLogDataListView.as_view(), name='plogdata_list'),

    # ======== ввывод кода карты ========
    path('coding/mark/', views.PMarkView.as_view(), name='encode'),

    path('wta/', views.WTAView.as_view(), name='wta'),

    # ========  DRF  ========
    # path('p-list/<int:pk>/', PlistDetailView.as_view(), name='plist_detail'),
    # path('plist-picture/<int:pk>/', PlistPictureView.as_view(), name='plist_picture'),
    # path('search-plist/', PListSearchView.as_view(), name='search'),
]
# urlpatterns += router.urls
