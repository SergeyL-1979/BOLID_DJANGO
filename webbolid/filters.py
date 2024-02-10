from django import forms
import django_filters
# from django_filters import rest_framework as filters

from webbolid.models import Plogdata, Plist

from django.db.models import Sum, F, ExpressionWrapper, fields


# class PLogDataFilter(django_filters.FilterSet):
#     min_date = django_filters.DateFilter(lookup_expr='gte', field_name='devicetime',
#                                          widget=forms.DateInput(attrs={'type': 'date'})
#                                          )
#     max_date = django_filters.DateFilter(lookup_expr='lte', field_name='devicetime',
#                                          widget=forms.DateInput(attrs={'type': 'date'})
#                                          )
#     hozorgan = django_filters.CharFilter(field_name='hozorgan__name', lookup_expr='icontains')
#
#     class Meta:
#         model = Plogdata
#         fields = ['hozorgan', ]


class PLogDataFilter(django_filters.FilterSet):
    min_date = django_filters.DateFilter(lookup_expr='gte', field_name='devicetime')
    max_date = django_filters.DateFilter(lookup_expr='lte', field_name='devicetime')
    hozorgan = django_filters.CharFilter(field_name='hozorgan__name', lookup_expr='icontains')

    class Meta:
        model = Plogdata
        fields = ['hozorgan', 'min_date', 'max_date']


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


# =======================================================
# class PLogDataFilter(filters.FilterSet):
#     min_date = filters.DateFilter(lookup_expr='gte', field_name='devicetime',
#                                   widget=forms.DateInput(attrs={'type': 'date'})
#                                   )
#     max_date = filters.DateFilter(lookup_expr='lte', field_name='devicetime',
#                                   widget=forms.DateInput(attrs={'type': 'date'})
#                                   )
#     hozorgan = filters.CharFilter(field_name='hozorgan__name', lookup_expr='icontains')
#
#     # Новые поля для группировки и расчета отработанных часов в день
#     devicetime__date = filters.DateFilter(lookup_expr='date', field_name='devicetime')
#     hours_worked = filters.Filter(
#         expression=ExpressionWrapper(F('devicetime') - F('devicetime'), output_field=fields.DurationField()),
#         lookup_expr='gt',
#         label='Hours Worked'
#     )
#
#     class Meta:
#         model = Plogdata
#         fields = ['hozorgan', 'devicetime', 'hours_worked']

# =====================================================================

# class PLogDataFilter(filters.FilterSet):
#     min_date = filters.DateFilter(lookup_expr='gte', field_name='devicetime',
#                                   widget=forms.DateInput(attrs={'type': 'date'})
#                                   )
#     max_date = filters.DateFilter(lookup_expr='lte', field_name='devicetime',
#                                   widget=forms.DateInput(attrs={'type': 'date'})
#                                   )
#     # min_time = filters.TimeFilter(lookup_expr='gte', field_name='devicetime',
#     #                               widget=forms.TimeInput(attrs={'type': 'time'})
#     #                               )
#     # max_time = filters.TimeFilter(lookup_expr='lte', field_name='devicetime',
#     #                               widget=forms.TimeInput(attrs={'type': 'time'})
#     #                               )
#     hozorgan = filters.CharFilter(field_name='hozorgan__name', lookup_expr='icontains')
#
#     class Meta:
#         model = Plogdata
#         fields = ['hozorgan',]
# fields = ['hozorgan', 'event', 'min_date', 'max_date', 'min_time', 'max_time']
