import django_filters

from webbolid.models import Plogdata, Plist


class PLogDataFilter(django_filters.FilterSet):
    min_datetime = django_filters.DateTimeFilter(
        lookup_expr='gte', field_name='timeval', label='Начальная дата:')
    max_datetime = django_filters.DateTimeFilter(
        lookup_expr='lte', field_name='devicetime', label='Конечная дата:')
    hozorgan = django_filters.CharFilter(
        field_name='hozorgan__name', lookup_expr='icontains', label='Фамилия:')

    class Meta:
        model = Plogdata
        fields = ['hozorgan', 'min_datetime', 'max_datetime', 'event']


# ========= УРВ ======================
class TimeFilter(django_filters.FilterSet):
    hozorgan = django_filters.CharFilter(
        field_name='hozorgan__name', lookup_expr='icontains', label='Фамилия:')
    first_exit = django_filters.DateTimeFilter(
        lookup_expr='gte', field_name='timeval', label='Начальная дата:')
    end_exit = django_filters.DateTimeFilter(
        lookup_expr='lte', field_name='timeval', label='Конечная дата:')
    # first_exit = django_filters.CharFilter(
    #     field_name='plogdata__mode', lookup_expr='icontains', label='Режим:')
    # end_exit = django_filters.CharFilter(
    #     field_name='plogdata__mode', lookup_expr='icontains', label='Режим:')

    class Meta:
        model = Plogdata
        fields = ['first_exit', 'end_exit', 'hozorgan']


# ============ ГОТОВЫЙ ПОИСК СОТРУДНИКОВ ================================
class PlistFilter(django_filters.FilterSet):
    class Meta:
        model = Plist
        fields = {
            'name': ['exact', ],
            'firstname': ['exact', ],
            'midname': ['exact', ],
            # 'workphone': ['exact', ],
            # 'homephone': ['exact', ],
            # 'company__name': ['exact'],
            # 'post__name': ['exact'],
            # 'tabnumber': ['exact', ],
        }
# ==========================================================================
