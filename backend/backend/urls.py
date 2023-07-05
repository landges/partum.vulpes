from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.upload.views import image_upload

urlpatterns = [
    # path("", image_upload, name="upload"),
    path('', include("apps.web.urls")),
    path("admin/", admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
