import subprocess
import os
import time

def ask_for_ipsw_path(path):
    if os.path.isfile(path) and path.lower().endswith('.ipsw'):
        print("IPSW file validated.")
        return path
    else:
        print("Invalid file. Make sure it ends with .ipsw and exists.")
        return None

def restore_device(ipsw_path):
    sure_or_not = input("Are you sure you want to restore the device(y or n)\n>>>")
    if sure_or_not == "y":
        try:
            subprocess.run(['idevicerestore', '-e', ipsw_path], check=True)
            print("Restore started...")
        except subprocess.CalledProcessError:
            print("Restore failed. Check the IPSW or device connection.")
        except FileNotFoundError:
            print("'idevicerestore' not found. Make sure it's installed.")
    else:
        print("Canceling...")
        time.sleep(0.5)