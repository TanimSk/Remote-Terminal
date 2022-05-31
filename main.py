import subprocess


cmd = ""
out2 = subprocess.run(cmd, capture_output=True, text=True, shell=True)

if not out2.returncode == 0:
    # print error
    print(f"ERROR: {out2.stderr}")

else:
    print(out2.stdout)