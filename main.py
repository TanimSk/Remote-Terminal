import asyncio
from pathlib import Path
from io import BytesIO
import base64
import json
import requests
import subprocess
import websockets
import pyautogui
import asyncio
import uuid
import os
import cv2


class RemoteTerminal:
    def __init__(self):
        self.commands = [
            'getScreen', 'sendKeys', 'getWebcam', 'getFile', 'cmdList'
        ]
        self.ws = None

    async def exe_cmd(self, cmd) -> dict:
        cmd_list = cmd.split(' ')

        # Run special commands
        if cmd_list[0] in self.commands:
            return await getattr(self, cmd_list[0])(cmd_list)

        # Execute terminal commands
        else:
            out = subprocess.run(cmd, capture_output=True,
                                 text=True, shell=True)
            if not out.returncode == 0:
                return {
                    'type': 'text',
                    'content': f"ERROR: {out.stderr}"
                }
            else:
                return {
                    'type': 'text',
                    'content': out.stdout
                }

    # --- Return all special commands ---
    async def cmdList(self, *args) -> dict:
        cmds = ""
        for cmd in self.commands:
            cmds += f"{cmd}\n"
        return {
            'type': 'text',
            'content': cmds
        }

    async def conv64(self, img) -> str:
        img_file = BytesIO()
        img.save(img_file, format='JPEG')
        img64 = base64.b64encode(img_file.getvalue())
        return img64.decode('utf-8')


    # --- Screen Shot ---
    async def getScreen(self, *args) -> dict:

        image = pyautogui.screenshot()
        return {
            'type': 'image',
            'content': await self.conv64(image)
        }


    # --- Webcam Snap ----
    async def getWebcam(self, *args) -> dict:
        img = cv2.VideoCapture(0)
        ret, frame = img.read()
        retval, buffer = cv2.imencode('.jpg', frame)
        img64 = base64.b64encode(buffer)
        return {
            'type': 'image',
            'content': img64.decode('utf-8')
        }

    # --- Executing keystrokes ---
    '''
        # for hotkey example: #enter, #shift
        | for delay in sec example: |10, |7
    '''
    async def sendKeys(self, cmds) -> str:
        cmd_args = cmds[1].split(',')

        await self.ws.send(json.dumps({
            'type': 'wait',
            'content': 'Please wait ...'
        }))

        for cmd_arg in cmd_args:
            if cmd_arg[0] == '#':
                pyautogui.press(cmd_arg[1:])
            elif cmd_arg[0] == '|':
                await asyncio.sleep(int(cmd_arg[1:]))
            else:
                pyautogui.write(cmd_arg)
            await asyncio.sleep(0.5)

        return {
            'type': 'text',
            'content': "Done!"
        }


    # --- Getting the file ---
    async def getFile(self, cmds) -> dict:
        filename = cmds[1]

        params = {
            'output': 'text',
        }

        files = {
            'files[]': open(filename, 'rb'),
        }

        await self.ws.send(json.dumps({
            'type': 'wait',
            'content': 'Uploading File ...'
        }))

        response = requests.post('https://tmp.ninja/upload.php', params=params, files=files)

        return {
            'type': 'text',
            'content': 'File URL: ' + response.text
        }


    # --- storing UUID ---
    def generate_uuid(self) -> str:

        uuid_file = Path(os.path.join(os.getcwd(), "./.data"))
        if uuid_file.is_file():
            with open(".data", 'r') as f:
                my_uuid = f.read()
                print(f"your UUID: {my_uuid}")
                return my_uuid

        else:
            with open(".data", 'w') as f:
                my_uuid = str(uuid.uuid4())
                f.write(my_uuid)
                print(f"your UUID: {my_uuid}")
                return my_uuid


# --- Socket  Connection ---
async def run_terminal():
    term = RemoteTerminal()
    my_uuid = term.generate_uuid()
    URL = f"ws://remo-terminal.herokuapp.com/ws/{my_uuid}/"

    async with websockets.connect(URL) as websocket:
        await websocket.send('Connected !')
        term.ws = websocket
        print('Connected !')

        while True:
            cmd = await websocket.recv()
            print(cmd)
            cmd_out = await term.exe_cmd(cmd)
            print(cmd_out)
            await websocket.send(json.dumps(cmd_out))


if __name__ == "__main__":
    asyncio.run(run_terminal())
