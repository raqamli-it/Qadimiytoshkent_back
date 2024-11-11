from rest_framework import serializers
from .models import Archaeology, Items, News, ArchaeologyPicture, ItemsPicture, NewsPicture, Category, ArchaeologyType


class ArchaeologyPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchaeologyPicture
        fields = ['id', 'title', 'image', 'link']


class ItemsPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsPicture
        fields = ['id', 'image', 'link']


class ItemsSerializers(serializers.ModelSerializer):
    picture_items = serializers.SerializerMethodField()

    class Meta:
        model = Items
        fields = ['id', 'title_uz', 'title_en', 'context_uz', 'context_en', 'image', 'video', 'video_link', 'create',
                  'update', 'picture_items', 'category']

    def get_picture_items(self, obj):
        request = self.context.get('request')
        data = ItemsPictureSerializer(obj.picture_items.all(), many=True, context={'request': request}).data
        for obj_url in data:
            if obj_url.get('image') and request is not None:
                obj_url['image'] = request.build_absolute_uri(obj_url['image'])
        return data


class CategorySerializer(serializers.ModelSerializer):
    items = ItemsSerializers(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'icon', 'items']


class ArchaeologyTypeForItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = ArchaeologyType
        fields = ['id', 'title', 'image', ]


class ArchaeologySerializers(serializers.ModelSerializer):
    archaeologyPicture = serializers.SerializerMethodField()

    class Meta:
        model = Archaeology
        fields = ['id', 'title_uz', 'title_en', 'context_uz', 'context_en', 'pasport', 'image', 'video', 'video_link',
                  'link', 'create', 'update', 'archaeologyPicture', ]

    def get_archaeologyPicture(self, obj):
        request = self.context.get('request')
        data = ArchaeologyPictureSerializer(obj.archaeologyPicture.all(), many=True, context={'request': request}).data
        for obj_url in data:
            if obj_url.get('image') and request is not None:
                obj_url['image'] = request.build_absolute_uri(obj_url['image'])
        return data


class NewsPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPicture
        fields = ['id', 'image', ]


class NewsSerializers(serializers.ModelSerializer):
    news_picture = NewsPictureSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = (
            'id', 'title_uz', 'title_en', 'context_uz', 'context_en', 'image', 'create', 'update', 'news_picture',)
