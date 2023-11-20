from django.urls import path, include
from rest_framework import routers

from webbolid.views import PListView, PListDetailView, PListUpdateView, SearchListViews

# from webbolid.views import PListViewSet, PlistPictureView, PlistDetailView, PLogDataViewSet, \
#     PListSearchView, PListView, PListDetailView

# router = routers.DefaultRouter()
# router.register('list', PListViewSet, basename='p_list')
# router.register('p-log-data', PLogDataViewSet, basename='log_data')


urlpatterns = [
    # path('', include(router.urls)),
    path('', PListView.as_view(), name='list'),
    path('<int:pk>/', PListDetailView.as_view(), name='list_detail'),
    path('<int:pk>/update', PListUpdateView.as_view(), name='list_update'),
    path('search/', SearchListViews.as_view(), name='search'),

    # ========  DRF  ========
    # path('p-list/<int:pk>/', PlistDetailView.as_view(), name='plist_detail'),
    # path('plist-picture/<int:pk>/', PlistPictureView.as_view(), name='plist_picture'),
    # path('search-plist/', PListSearchView.as_view(), name='search'),
]
# urlpatterns += router.urls
