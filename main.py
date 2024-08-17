import os
import time
import subprocess
import webbrowser

# Step 1: Disable the touchscreen input
def disable_touchscreen():
    # Find the touchscreen device name
    try:
        output = subprocess.check_output("xinput --list", shell=True).decode()
        lines = output.split('\n')
        for line in lines:
            if 'Touchscreen' in line:
                device_id = line.split('id=')[1].split()[0]
                subprocess.call(f"xinput --disable {device_id}", shell=True)
                print(f"Touchscreen (Device ID: {device_id}) has been disabled.")
                return
        print("Touchscreen device not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Step 2: Open a browser in fullscreen mode
def open_url_fullscreen():
    url = os.getenv('TARGET_URL')
    if not url:
        print("Environment variable 'TARGET_URL' is not set.")
        return

    webbrowser.open(url)
    time.sleep(5)
    subprocess.call("xdotool search --onlyvisible --class 'chromium' windowactivate --sync key F11", shell=True)
    print(f"Opened {url} in fullscreen mode.")

if __name__ == "__main__":
    disable_touchscreen()
    open_url_fullscreen()
