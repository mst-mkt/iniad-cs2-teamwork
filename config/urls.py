from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.urls import path
from config import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("collect.urls")),
    path('terms_of_service/', views.terms_of_service, name='terms_of_service'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
