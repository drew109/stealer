import subprocess
import os

#pass file
password = open("pass.txt", "w")
password.write("wsg good bbg:\n\n")
password.close()


#lists
wifi_files = []
wifi_name = []
wifi_password = []

#term cmd
command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output = True).stdout.decode()

#pulls current dir
path = os.getcwd()


#Magic
for filename in os.listdir(path):
    if filename.startswith("Wi-FI") and filename.endswith(".xml"):
        wifi_files.append(filename)
        for i in wifi_files:
            with open(i,'r') as f:
                for line in f.readlines():
                    if 'name' in line:
                        stripped = line.strip()
                        front = stripped[6:]
                        back = stripped[:-7]
                        wifi_name.append(back)
                    if 'keyMaterial' in line:
                        front = stripped[13:]
                        back = stripped[:14]
                        wifi_password.append(back)
                        