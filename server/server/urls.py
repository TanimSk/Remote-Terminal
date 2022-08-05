from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('handle_cmd', views.handle_cmd, name='handle_cmd'),
    path('admin/', admin.site.urls),
]
