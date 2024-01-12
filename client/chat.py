import asyncio
import websockets
import json
from aioconsole import ainput
from time import gmtime, strftime
import sys


async def receive_messages(uri):
    async with websockets.connect(uri) as websocket:
        print("Connected!")
        await websocket.send("Connected !")
        while True:
            message = await websocket.recv()
            try:
                json.loads(message)
            except:
                sys.stdout.write(16 * "\b")
                print(
                    f'Received Message @{strftime("%Y-%m-%d %I:%M:%S %p", gmtime())} >> {message}'
                )
                print("Send Message <<", end=" ")
                await websocket.send(json.dumps({"type": "text", "content": f"Sent"}))


async def send_messages(uri):
    async with websockets.connect(uri) as websocket:
        while True:
            await asyncio.sleep(0.5)
            user_input = await ainput("Send Message << ")
            await websocket.send(
                json.dumps({"type": "text", "content": f"{user_input}"})
            )

            print(f"Message Delivered!\n")


async def main():
    my_uuid = "e407f540-6f94-4757-a3c2-c8dd5a3d3ede"

    uri = f"wss://test.ongshak.com/ws/{my_uuid}/"

    receive_task = asyncio.create_task(receive_messages(uri))
    send_task = asyncio.create_task(send_messages(uri))

    await asyncio.gather(receive_task, send_task)


if __name__ == "__main__":
    print("\n\n-------- WebSocket Messaging -----------")
    print("source code: https://github.com/TanimSk/")
    print("----------------------------------------\n\n")

    asyncio.run(main())
