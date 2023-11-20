from django import forms
from django_filters import rest_framework as filters

from webbolid.models import Plogdata


class PLogDataFilter(filters.FilterSet):
    min_date = filters.DateFilter(lookup_expr='gte', field_name='devicetime',
                                  widget=forms.DateInput(attrs={'type': 'date'})
                                  )
    max_date = filters.DateFilter(lookup_expr='lte', field_name='devicetime',
                                  widget=forms.DateInput(attrs={'type': 'date'})
                                  )
    # min_time = filters.TimeFilter(lookup_expr='gte', field_name='devicetime',
    #                               widget=forms.TimeInput(attrs={'type': 'time'})
    #                               )
    # max_time = filters.TimeFilter(lookup_expr='lte', field_name='devicetime',
    #                               widget=forms.TimeInput(attrs={'type': 'time'})
    #                               )
    hozorgan = filters.CharFilter(field_name='hozorgan__name', lookup_expr='icontains')

    class Meta:
        model = Plogdata
        fields = ['hozorgan',]
        # fields = ['hozorgan', 'event', 'min_date', 'max_date', 'min_time', 'max_time']

