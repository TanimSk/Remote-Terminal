from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("documentation", views.documentation, name="doc"),
    path("download", views.download, name="download"),
    path("about", views.about, name="about"),
    path("admin/", admin.site.urls),
    path("post_data/", views.post_data, name="post_data"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
