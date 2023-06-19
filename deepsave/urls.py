from django.contrib import admin
from django.urls import path, include
from core import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from core.viewsets import LinkViewSet, DocumentViewSet

router = routers.DefaultRouter()

router.register(r'link', LinkViewSet)
router.register(r'document', DocumentViewSet)

urlpatterns = [
    path('', include('core.urls')),
]

urlpatterns += [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    # Endpoints
    path('api/v1/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
