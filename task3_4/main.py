import subprocess
import time
import requests
from dotenv import load_dotenv
import os

load_dotenv()

# ---------- Task 3: Emulator Automation ----------

def start_emulator(avd_name):
    emulator_path = os.getenv('EMULATOR_PATH')
    print(f"Starting emulator: {avd_name}")
    subprocess.Popen([emulator_path, "-avd", avd_name])
    time.sleep(5)

# Full path to your ADB
ADB_PATH = os.getenv('ADB_PATH')

def wait_for_boot():
    print("Waiting for device to boot...")
    subprocess.run([ADB_PATH, "wait-for-device"])
    while True:
        boot_status = subprocess.check_output([ADB_PATH, "shell", "getprop", "sys.boot_completed"]).decode().strip()
        if boot_status == '1':
            print("Device booted successfully.")
            break
        time.sleep(2)

def install_apk(apk_path):
    print(f"Installing APK: {apk_path}")
    result = subprocess.run([ADB_PATH, "install", apk_path], capture_output=True, text=True)
    print(result.stdout or result.stderr)

def get_system_info():
    package_name = "com.example.myapp"  # Replace this with your app's real package name

    os_version = subprocess.check_output([ADB_PATH, "shell", "getprop", "ro.build.version.release"]).decode().strip()
    device_model = subprocess.check_output([ADB_PATH, "shell", "getprop", "ro.product.model"]).decode().strip()
    memory = subprocess.check_output([ADB_PATH, "shell", "cat", "/proc/meminfo"]).decode().split("\n")[0]

    # Get app version using dumpsys
    try:
        version_info = subprocess.check_output([
            ADB_PATH, "shell", "dumpsys", "package", package_name
        ]).decode()

        # Extract versionName from the output
        version_line = [line for line in version_info.splitlines() if "versionName=" in line]
        app_version = version_line[0].split("=")[1].strip() if version_line else "Unknown"
    except Exception as e:
        app_version = "Not Installed"

    info = {
        "os_version": os_version,
        "device_model": device_model,
        "available_memory": memory,
        "app_version": app_version
    }

    print("\n📱 System Info:")
    for k, v in info.items():
        print(f"{k}: {v}")

    return info

# ---------- Task 4: Networking (API call) ----------

def post_to_api(info):
    api_url = "http://127.0.0.1:5000/add-app"
    payload = {
        "app_name": info["device_model"],
        "version": info["app_version"],
        "description": f"OS: {info['os_version']}, {info['available_memory']}"
    }

    print("\nSending data to backend API...")
    response = requests.post(api_url, json=payload)
    print("Server response:")
    print(response.status_code, response.json())

# ---------- Main Execution ----------

if __name__ == '__main__':
    AVD_NAME = os.environ('AVD_NAME')  # Replace with your AVD name
    APK_PATH = os.environ('APK_PATH')

    start_emulator(AVD_NAME)
    wait_for_boot()
    install_apk(APK_PATH) 
    system_info = get_system_info()
    post_to_api(system_info)
