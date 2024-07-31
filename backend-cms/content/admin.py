from django.contrib import admin
from .models import Article, Image, Document, Page, Tab

admin.site.register(Article)
admin.site.register(Image)
admin.site.register(Document)
admin.site.register(Page)
admin.site.register(Tab)