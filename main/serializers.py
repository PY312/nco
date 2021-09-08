from rest_framework import serializers
from .models import News, ImageNews


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = 'id title publication_date image short_description'.split()


class ImageNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageNews
        fields = 'id image'.split()


class NewsItemSerializer(serializers.ModelSerializer):
    images = ImageNewsSerializer(many=True)

    class Meta:
        model = News
        fields = 'id title link full_description images'.split()
