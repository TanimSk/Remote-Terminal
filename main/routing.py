from django.urls import path
from . import consumers

ws_urlpatterns = [
    path('ws/<str:uuid>/', consumers.NewConsumer.as_asgi()),
]