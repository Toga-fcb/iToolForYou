import subprocess
import time
from .connection import is_device_connected
from .poweroff_reboot import reboot_device
from .poweroff_reboot import poweroff_device
from .e import show_error
from .fi import ask_for_ipsw_path
from .fi import restore_device

def m_operations():
    if is_device_connected():
        try:
            time.sleep(0.5)
            option_operation = int(input("[1] Reboot device\n[2] Poweroff device\n[3] Restore device\n[4] Exit\n>>> "))
        except Exception as e:
            print(e)
        if option_operation == 1:
            reboot_device()
        elif option_operation == 2:
            poweroff_device()
        elif option_operation == 3:
            if is_device_connected():
                ipsw = input("ipsw path\n>>> ")
                if ask_for_ipsw_path(ipsw):
                    restore_device(ipsw)
                else:
                    print("Error")
            else:
                print("Device is not connected. Exiting")
                exit()
        elif option_operation == 4:
            exit()
        else:
            print("\n\n")
            show_error()
            print("\n\n")
    else:
        print("[ERROR]")