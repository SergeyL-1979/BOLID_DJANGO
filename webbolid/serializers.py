import base64
from datetime import timedelta

from django.db.models import Q, Sum, F
from django.db.models.functions import ExtractDay, ExtractHour
from rest_framework import serializers

from webbolid.models import (
    Plist, Ppost, Pcompany, Events, Plogdata, Querylog, Pdivision
)


class PpostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ppost
        fields = ['name']


class PcompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Pcompany
        fields = ['name']


class PdivisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pdivision
        fields = '__all__'


class PListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plist_picture',
        lookup_field='id',
        lookup_url_kwarg='pk',
        read_only=True
    )
    name = serializers.CharField(label='Фамилия')
    firstname = serializers.CharField(label='Имя')
    midname = serializers.CharField(label='Отчество')
    workphone = serializers.CharField(label='Начало действия')
    homephone = serializers.CharField(label='Конец действия')
    tabnumber = serializers.CharField(label='Табельный номер')
    company = serializers.SlugRelatedField(slug_field='name', queryset=Pcompany.objects.all(), label='Компания')
    post = serializers.SlugRelatedField(slug_field='name', queryset=Ppost.objects.all(), label='Подразделение')

    class Meta:
        model = Plist
        fields = (
            'id',
            'url',
            'name',
            'firstname',
            'midname',
            'workphone',
            'homephone',
            'tabnumber',
            'company',
            'post',
        )


class PlistPictureSerializer(serializers.ModelSerializer):
    picture_url = serializers.SerializerMethodField()
    company = serializers.StringRelatedField(label='Компания')
    post = serializers.StringRelatedField(label='Подразделение')

    class Meta:
        model = Plist
        fields = (
            'id',
            'name',
            'firstname',
            'midname',
            'workphone',
            'homephone',
            'picture_url',
            'tabnumber',
            'company',
            'post',
        )

    def get_picture_url(self, obj):
        if obj.picture:
            image_base64 = base64.b64encode(obj.picture).decode('utf-8')
            return f'data:image/bmp;base64,{image_base64}'
        return None


class EventsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Events
        fields = ["event",  "contents", ]


class PLogDataSerializer(serializers.ModelSerializer):
    hozorgan = serializers.CharField(label='Сотрудник')
    event = serializers.StringRelatedField()
    devicetime = serializers.DateTimeField(format="%d-%m-%Y %H:%M")
    # timeval = serializers.DateTimeField(format="%d-%m-%Y %H:%M")

    class Meta:
        model = Plogdata
        fields = ["hozorgan", "remark", "devicetime", "event", ]


class QuerylogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Querylog
        fields = '__all__'

