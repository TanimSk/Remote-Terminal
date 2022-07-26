from channels.consumer import AsyncConsumer

class NewConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print("initialised")
        await self.send({
            'type': 'websocket.accept'
        })
    
    async def websocket_receive(self, event):
        print("received")

    async def websocket_disconnect(self, event):
        print("Disconnected")