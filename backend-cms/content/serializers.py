# content/serializers.py
from rest_framework import serializers
from .models import Article, Image, Document, Tab, Page
import bleach

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'template']

class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ['id', 'title', 'image', 'image_url']

    def get_image_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.image.url)

class DocumentSerializer(serializers.ModelSerializer):
    document_url = serializers.SerializerMethodField()

    class Meta:
        model = Document
        fields = ['id', 'title', 'document', 'document_url']

    def get_document_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.document.url)


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'

class TabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tab
        fields = '__all__'
        