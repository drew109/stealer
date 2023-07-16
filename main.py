import subprocess
import os
import xml.etree.ElementTree as ET
import time

# lists
wifi_files = []
wifi_names = []
wifi_passwords = []

# term cmd
subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output = True)

# pulls current dir
path = os.getcwd()

# Magic
for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        wifi_files.append(filename)

for i in wifi_files:
    tree = ET.parse(i)
    root = tree.getroot()
    wifi_name = root.find("name").text
    wifi_password = root.find("MSM/security/sharedKey/keyMaterial").text
    wifi_names.append(wifi_name)
    wifi_passwords.append(wifi_password)

# Print the names and passwords
for name, password in zip(wifi_names, wifi_passwords):
    print(f"WiFi Name: {name}, Password: {password}")


time.sleep(100)
