import os
import shutil
import time
from datetime import datetime

def get_drives():
    return set(f"{d}:\\" for d in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if os.path.exists(f"{d}:\\"))

def copy_usb(usb_path, base_dest):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(base_dest, f"USB_{timestamp}")

    try:
        shutil.copytree(usb_path, dest, dirs_exist_ok=True)
        print(f"Copied {usb_path} → {dest}")
    except Exception as e:
        print(f"Error copying {usb_path}: {e}")

# MAIN
base_destination = "C:\\Users\\hp\\Desktop\\USB_Backups"

print("Waiting for USB devices...")

known_drives = get_drives()

while True:
    time.sleep(2)
    current_drives = get_drives()

    new_drives = current_drives - known_drives

    if new_drives:
        for usb in new_drives:
            print(f"Detected: {usb}")
            copy_usb(usb, base_destination)

        known_drives = current_drives