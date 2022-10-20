import subprocess
import os


command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output = True).stdout.decode()

#pulls current dir
path = os.getcwd()