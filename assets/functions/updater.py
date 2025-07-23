import requests
import os
import time
import zipfile
import sys
import shutil
from bs4 import BeautifulSoup
from urllib.parse import urljoin



def updater(headers):
    current_version = "RLS_1.0"
    url = "https://itoolforyou-updater-update-site-itfy.netlify.app/"
    response = requests.get(url, headers=headers)
    time.sleep(1.5)
    soup = BeautifulSoup(response.text, "html.parser")
    version = soup.find("p", class_ = "itfy_ver")
    version_value = version.text
    if version_value != current_version:
        print("iToolForYou has a new update!")
        decision = input("Install?(y or n)>>> ")
        if decision == "y":
            link = soup.find("a", href=True)
            target = link['href']
            dir_url = urljoin(url, target)
            response2 = requests.get(dir_url, headers=headers, stream=True)
            dest_folder = os.path.join("assets", "updates")
            filename = f"iToolForYou_{version_value}.zip"
            os.makedirs(dest_folder, exist_ok=True)
            dest_path = os.path.join(dest_folder, filename)
            total_bytes = int(response2.headers.get('Content-Length', 0))
            total_mb = total_bytes // (1024 * 1024)
            dv = 0
            with open(dest_path, 'wb') as f:
                for chunk in response2.iter_content(chunk_size=1024*1024):
                    if chunk:
                        f.write(chunk)
                        dv += len(chunk)
                        downloaded_mb = dv // (1024*1024)
                        sys.stdout.write(f"\rDownloaded of {filename}: {downloaded_mb} MB out of {total_mb} MB")
                        sys.stdout.flush()
            print("\nThe file is successfully downloaded!\n")
            time.sleep(2)
            unzip_path = os.path.join(dest_folder, f"iToolForYou_{version_value}_unzipped")
            os.makedirs(unzip_path, exist_ok=True)
            with zipfile.ZipFile(dest_path, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            print(f"\nUnzipped to: {unzip_path}\n")
            option = input("Delete old version and keep only new?(y or n)You will have to complete the instructions again>>> ")
            if option == "y":                
                current_path = os.path.abspath(__file__)
                current_dir = os.path.dirname(current_path)
                target_dir = os.path.abspath(os.path.join(current_dir, "../../")) 
                update_folder = os.path.join(target_dir, "assets", "updates")
                files_to_keep = ["assets"]
                for item in os.listdir(target_dir):
                    item_path = os.path.join(target_dir, item)
                    if item not in files_to_keep:
                        if os.path.isdir(item_path):
                            shutil.rmtree(item_path)
                        else:
                            os.remove(item_path)
                unzip_path = os.path.join(update_folder, f"iToolForYou_{version_value}_unzipped")
                dest_folder = os.path.join(target_dir, "iToolForYou")
                if os.path.exists(dest_folder):
                    shutil.rmtree(dest_folder)
                shutil.move(unzip_path, dest_folder)
                try: 
                    remove_dir = os.path.join(dest_folder, "__MACOSX")
                except Exception as e:
                    print(e)
                if os.path.exists(remove_dir):
                    shutil.rmtree(remove_dir)
                nested = os.path.join(dest_folder, "iToolForYou")
                if os.path.exists(nested):
                    for item in os.listdir(nested):
                        shutil.move(os.path.join(nested, item), dest_folder)
                    shutil.rmtree(nested)
                assets_folder = os.path.join(target_dir, "assets")
                if os.path.exists(assets_folder):
                    shutil.rmtree(assets_folder)
                parent_dir = target_dir 
                source_dir = dest_folder
                for item in os.listdir(source_dir):
                    src_path = os.path.join(source_dir, item)
                    dest_path = os.path.join(parent_dir, item)
                    if os.path.exists(dest_path):
                        if os.path.isdir(dest_path):
                            shutil.rmtree(dest_path)
                        else:
                            os.remove(dest_path)
                    shutil.move(src_path, dest_path)
                if os.path.exists(source_dir):
                    os.rmdir(source_dir)
                exit()
            elif option == "n":
                print(f"Alright! You are stayed on {current_version}! New version: {version_value}. To start the new version, all you have to do is \n1. Enter the {unzip_path}\n2. Take out the file(not zip one, you can delete zip if you want).\n3. After you took out the file to any directory you want(desktop, downloads anything), you need to repeat the instructions once again.")
            else:
                print("Unknown option.")
        elif decision == "n":
            print(f"Alright! You are stayed on {current_version}! New version: {version_value}")
        else:
            print("Unknown option.")
    else:
        print("Application is up to date!")