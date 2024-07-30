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
        #fields = ['id', 'title', 'content', 'slug']

        def validate_content(self, value):
            allowed_tags = allowed_tags = [
                'p', 'b', 'i', 'u', 'em', 'strong', 'a', 'ul', 'ol', 'li', 
                'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'code', 
                'pre', 'br', 'span', 'div', 'img'
            ]
            allowed_attributes = {
                'a': ['href', 'title'],
                'img': ['src', 'alt'],
                '*': ['style']  # Permitir atributos style em todas as tags
            }
            return bleach.clean(value, tags=allowed_tags, attributes=allowed_attributes)
        
        def create(self, validated_data):
            validated_data['content'] = self.sanitize_html(validated_data.get('content', ''))
            return super().create(validated_data)
    
        def update(self, instance, validated_data):
            validated_data['content'] = self.sanitize_html(validated_data.get('content', ''))
            return super().update(instance, validated_data)
        
        def sanitize_html(content):
            allowed_tags = [
                'p', 'b', 'i', 'u', 'em', 'strong', 'a', 'ul', 'ol', 'li', 
                'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'code', 
                'pre', 'br', 'span', 'div', 'img'
            ]
            allowed_attributes = {
                'a': ['href', 'title'],
                'img': ['src', 'alt'],
                '*': ['style']  # Permitir atributos style em todas as tags
            }
            return bleach.clean(content, tags=allowed_tags, attributes=allowed_attributes, strip=True)

class TabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tab
        fields = '__all__'