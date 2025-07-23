#libs
print("Starting iToolForYou...")
import requests
import time
import pymobiledevice
import os
import subprocess
from bs4 import BeautifulSoup
from assets.functions.iOS_installer import iOS_downloader
from assets.functions.updater import updater   
from assets.functions.info import info 
from assets.functions.clear_console import clear_console
from assets.functions.operations.main_operations import m_operations
from assets.functions.operations.connection import is_device_connected
from assets.functions.operations.e import show_error
from assets.functions.operations.fi import restore_device
from assets.functions.operations.fi import ask_for_ipsw_path
from assets.functions.operations.poweroff_reboot import reboot_device
from assets.functions.operations.poweroff_reboot import poweroff_device
from assets.functions.dependencies import install_dependencies
print("Started!")


#main
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}
while True:
    time.sleep(0.5)
    try:
        option = int(input("\n-------------------------------------\n    iToolForYou\n\n[1] Check for update(app)\n[2] Install firmware file\n[3] Clear console\n[4] iPhone operations\n[5] Information about the app\n[6] Exit\n[7] Install dependicies\n>>> "))
    except Exception as e:
        print(e)
    if option == 1:
        time.sleep(1)
        print("\n\n")
        updater(headers)
        print("\n\n")
    elif option == 2:
        time.sleep(1)
        print("\n\n")
        try: 
            while True:
                iPhone = int(input("iPhone model\n For instruction: 99\n>>> "))
                if iPhone == 99:
                    print("\n\niPhone 7 -> 7, Version -> base\n\niPhone 8 -> 8, Version -> base\n\niPhone X -> 10, Version -> base\niPhone XS -> 10, Version -> s\niPhone XS Max -> 10, Version -> max\n\niPhone 11 -> 11, Version -> base\niPhone 11 Pro -> 11, Version -> pro\niPhone 11 Pro Max -> 11, Version: pro max\n\niPhone 12 -> 12, Version -> base\niPhone 12 Pro -> 12, Version -> pro\niPhone 12 Pro Max -> 12, Version -> pro max\n\niPhone 13 -> 13, Version -> base\niPhone 13 Pro ->  13, Version: pro\niPhone 13 Pro Max -> 13, Version: pro max\n\niPhone 14 -> 14, Version: base\niPhone 14 Pro -> 14, Version: pro\niPhone 14 Pro Max -> 14, Version -> pro max\n\niPhone 15 -> 15, Version -> base\niPhone 15 Pro -> 15, Version -> pro\niPhone 15 Pro Max -> 15, Version -> pro max\n\niPhone 16 -> 16, Version -> base\niPhone 16 Pro -> 16, Version -> pro\niPhone 16 Pro Max -> 16, Version -> pro max\niPhone 16e -> 16, Version -> e\n\n")
                else:
                    break
        except Exception as e:
            print(e)
        iVersion = input("Version\n>>> ")
        iOS_downloader(iPhone, iVersion, headers)
        print("\n\n")
    elif option == 3:
        clear_console()
    elif option == 4:
        time.sleep(1)
        print("\n\n")
        if is_device_connected():
            while True:
                m_operations()
        else:
            print("Device is not connected")
        print("\n\n")
    elif option == 5:
        time.sleep(1)
        print("\n\n")
        info()
        print("\n\n")
    elif option == 6:
        print("Closing...")
        time.sleep(0.5)
        exit()
    elif option == 7:
        install_dependencies()
    else:
        print("Unknown option")
     