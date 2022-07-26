from django.urls import path
from . import consumers

ws_urlpatterns = [
    path('ws/socket-server/', consumers.NewConsumer.as_asgi()),
]