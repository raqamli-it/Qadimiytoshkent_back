from rest_framework import serializers

from .models import About, Muzeylar, Kutubxona, Olimlar


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'title_uz', 'title_en', 'description_uz', 'description_en', ]


class OlimlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Olimlar
        fields = ['id', 'fullname_uz', 'fullname_en', 'pasition_uz', 'pasition_en', 'image', ]


class KutubxonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kutubxona
        fields = ('id', 'title_uz', 'title_en', 'image', 'file', 'downloads',)


class MuzeylarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muzeylar
        fields = ['id', 'title_uz', 'title_en', 'image', 'video', 'video_link', 'link']
