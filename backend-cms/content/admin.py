from django.contrib import admin
from .models import Article, Image, Document

admin.site.register(Article)
admin.site.register(Image)
admin.site.register(Document)