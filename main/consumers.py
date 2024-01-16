from channels.consumer import AsyncConsumer
from .send_email import send_html_mail
import json


class NewConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        group_name = self.scope["url_route"]["kwargs"]["uuid"]

        await self.channel_layer.group_add(group_name, self.channel_name)

        await self.send({"type": "websocket.accept"})

    async def websocket_receive(self, event):
        print(event["text"], self.scope["url_route"]["kwargs"]["uuid"])

        # send a notification
        try:
            obj = json.loads(event["text"])
            if obj["type"] == "text":
                if obj["content"] == "Connected!":
                    send_html_mail(
                        "device connected",
                        f"id: {self.scope['url_route']['kwargs']['uuid']}",
                        ["sktanim5800@gmail.com"],
                        "noreply.service.tanimsk@gmail.com",
                    )
        except:
            pass

        await self.channel_layer.group_send(
            self.scope["url_route"]["kwargs"]["uuid"],
            {
                "type": "cmd.message",
                "channel_name": self.channel_name,
                "cmd": event["text"],
            },
        )

    async def cmd_message(self, event):
        # Sent data to everyone except data sender
        if not self.channel_name == event["channel_name"]:
            await self.send({"type": "websocket.send", "text": event["cmd"]})

    async def websocket_disconnect(self, event):
        await self.channel_layer.group_discard(
            self.scope["url_route"]["kwargs"]["uuid"], self.channel_name
        )


# NOTES:
# self.scope is a property like request in views.py
