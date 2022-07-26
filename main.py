from pathlib import Path
import subprocess
import websockets
import asyncio
import uuid
import os

# --- Subprocessing ---
def exe_cmd(cmd) -> str:
    out = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    if not out.returncode == 0:
        return f"ERROR: {out.stderr}"
    else:
        return out.stdout



# --- storing UUID ---
uuid_file = Path(os.path.join(os.getcwd(), "./.data"))
if uuid_file.is_file():
    with open(".data", 'r') as f:
        print(f"your UUID: {f.read()}")
        
else:
    with open(".data", 'w') as f:
        my_uuid = str(uuid.uuid4())
        f.write(my_uuid)
        print(f"your UUID: {my_uuid}")



# --- Socket  Connection ---
async def hello():

    URL = "ws://127.0.0.1:8000/ws/socket-server/"

    async with websockets.connect(URL) as websocket:
        name = input("What's your name? ")
        await websocket.send(name)
        print(f">>> {name}")
        greeting = await websocket.recv()
        print(f"<<< {greeting}")

if __name__ == "__main__":
    asyncio.run(hello())



