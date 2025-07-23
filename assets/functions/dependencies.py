import subprocess
import time

def install_dependencies():
    commands = [
        ["sudo", "apt", "update"],
        ["sudo", "apt", "install", "-y", "libimobiledevice-utils"],
        ["sudo", "apt", "install", "-y", "ifuse"],
        ["sudo", "apt", "install", "-y", "usbmuxd"],
        ["sudo", "apt", "install", "-y", "idevicerestore"],
    ]
    for cmd in commands:
        print(f"Running: {' '.join(cmd)}")
        subprocess.run(cmd)
        time.sleep(2)