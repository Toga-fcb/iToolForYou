import subprocess

def is_device_connected():
    try:
        result = subprocess.run(['idevice_id', '-l'], capture_output=True, text=True)
        device_udids = result.stdout.strip().splitlines()
        if device_udids:
            return True
        else:
            print("No device connected.")
            return False
    except FileNotFoundError:
        print("'idevice_id' not found. Please install libimobiledevice.")
        return False