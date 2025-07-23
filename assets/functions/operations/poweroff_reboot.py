import subprocess

def reboot_device():
    try:
        subprocess.run(['idevicediagnostics', 'restart'], check=True)
        print("Device is rebooting...")
    except FileNotFoundError:
        print("'idevicediagnostics' not found. Install libimobiledevice.")
    except subprocess.CalledProcessError:
        print("Failed to reboot device.")

def poweroff_device():
    try:
        subprocess.run(['idevicediagnostics', 'shutdown'], check=True)
        print("Device is powering off...")
    except FileNotFoundError:
        print("'idevicediagnostics' not found. Please install libimobiledevice.")
    except subprocess.CalledProcessError:
        print("Failed to power off device.")
