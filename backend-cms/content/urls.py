from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from .views import ArticleViewSet, ImageViewSet, DocumentViewSet, PageViewSet, TabViewSet, PageDetailViewBySlug

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'images', ImageViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'pages', PageViewSet)
router.register(r'tabs', TabViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/pages/slug/<slug:slug>/', PageDetailViewBySlug.as_view(), name='page-detail-by-slug'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
