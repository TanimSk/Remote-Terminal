from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('documentation', views.documentation, name='doc'),
    path('admin/', admin.site.urls),
]
