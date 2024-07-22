from rest_framework import serializers
from .models import Article, Image, Document

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        #fields = '__all__'
        fields = ['id', 'title', 'content', 'created_at', 'template']

class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ['id', 'title', 'image', 'image_url']

    def get_image_url(self, obj):
        return obj.image.url

class DocumentSerializer(serializers.ModelSerializer):
    document_url = serializers.SerializerMethodField()

    class Meta:
        model = Document
        fields = ['id', 'title', 'document', 'document_url']

    def get_document_url(self, obj):
        return obj.document.url