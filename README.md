# 🛠️ iToolForYou – iOS Firmware Utility for Linux

**iToolForYou** is a powerful terminal-based utility for Linux that helps you manage, restore, and update your iPhone firmware easily — right from the command line.

---

## 🚀 Features

- Full iPhone restore from selected `.ipsw` file (wipes device & installs firmware)  
- Auto-download latest IPSW from [ipsw.me](https://ipsw.me) for iPhone 7 through iPhone 16 series  
- Reboot and power off connected iPhone  
- Detect if an iPhone is connected via USB  
- Clear terminal console for a clean workspace  
- Self-update mechanism: checks for new versions, downloads, and replaces itself  
- Provides information about the app and its current version  

---

## ⚙️ Requirements & Setup Notes

> **Important:**  
> When you launch iToolForYou for the first time, or after deleting utilities like `libimobiledevice-utils`, `idevicerestore`, and others, you **must run option 7** (Install Dependencies) before using other features.  
> This ensures your system has all necessary tools installed.

### Required system packages (installed via option 7):

- `libimobiledevice-utils`  
- `ifuse`  
- `usbmuxd`  
- `idevicerestore`  
- `curl`  
- `python3` and related tools  

---

## 📝 Installation & Setup Instructions

1. **Clone or download** the iToolForYou project and navigate into its directory:

   ```bash
   cd path/to/iToolForYou

    Set up your Python environment:

sudo apt update
sudo apt install python3 python3-venv python3-pip
python3 -m venv .env

Activate the virtual environment:

source .env/bin/activate

Install Python dependencies:

pip3 install -r pip_req.txt

Launch the app:

    python3 app.py

    Run option 7 ("Install Dependencies") immediately inside the app.
    This will install necessary Linux packages required for full functionality.

    After dependencies are installed, you can use all features of iToolForYou smoothly.

📁 Typical Project Structure

iToolForY/
├── .env/                      
├── assets/                   
|   └──functions/
│      └──operations/
|      |   ├── connection.py
|      |   ├── e.py
|      |   ├── fi.py
|      |   ├── main_operation.py
|      |   └── poweroff_reboot.py
│      ├── clear_console.py
│      ├── dependencies.py
│      ├── info.py
│      ├── iOS_installer.py
│      ├── updater.py
|      ├── iOS/    
|      |   └── firmware_storage
|      ├── updates/
├── app.py         
├── pip_req.txt    
└── README.md      


💡 Usage Tips

    Always connect your iPhone and unlock it before using the tool.

    Trust the computer on your device when prompted.

    Use option 7 after any system changes to utilities or when running for the first time.

    Keep the app updated using its built-in self-update feature.

👤 Credits

Email: togaskyyy20@gmail.com
Telegram: @toga_fcb
GitHub: github.com/toga-fcb
⚠️ Disclaimer

Use iToolForYou only with devices you own.
This tool uses idevicerestore and firmware files from ipsw.me.
The author is not responsible for any data loss or device issues.

## 👐 Open Source & Licensing

iToolForYou is **open source** and free for anyone to use.  
I don't mind if someone uses it as their own app, but **modifications and redistributions require proper credit** and permission.  
Basically: feel free to use, but if you change it, respect the original work.  
Peace ✌️

Enjoy managing your iPhone firmware like a pro! 🚀📱