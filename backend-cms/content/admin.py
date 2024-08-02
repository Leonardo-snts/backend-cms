from typing import Any
from django.contrib import admin
from .models import Article, Image, Document, Page, Tab
from django.utils.translation import gettext_lazy as _

# Controle do site Admin
admin.site.site_header = _("Admin CMS")
admin.site.site_title = _("Gerenciador de Conteúdo")
admin.site.index_title = _("Seja Bem-Vindo ao CMS")
admin.site.site_url = _("https://imprensaoficial.am.gov.br/")

#Registro de Rotas
admin.site.register(Article)
admin.site.register(Image)
admin.site.register(Document)
admin.site.register(Page)
admin.site.register(Tab)
 