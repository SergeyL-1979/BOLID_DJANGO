import django_filters
from django_filters import rest_framework as filters

from webbolid.models import Plogdata, Plist, Pmark, Groups, Pcompany


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


# ========= УРВ - В РАЗРАБОТКЕ ======================
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

# ================= ФОРМА ФИЛЬТРА ПОИСКА НОМЕРА КАРТЫ - В РАЗРАБОТКЕ ============================
class PmarkFilter(filters.FilterSet):
    class PmarkFilter(filters.FilterSet):
        tab_number = filters.CharFilter(field_name="owner__tabnumber", lookup_expr="icontains", label="Табельный номер")
        name = filters.CharFilter(field_name="owner__firstname", lookup_expr="icontains", label="Имя")
        surname = filters.CharFilter(field_name="owner__name", lookup_expr="icontains", label="Фамилия")
        midname = filters.CharFilter(field_name="owner__midname", lookup_expr="icontains", label="Отчество")
        group_id = filters.ModelChoiceFilter(queryset=Groups.objects.all(), field_name="groupid", label="Группа")

        class Meta:
            model = Pmark
            fields = ['tab_number', 'name', 'surname', 'midname', 'gtype', 'group_id',]

