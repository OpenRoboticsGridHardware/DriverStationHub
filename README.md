# Raspberry Pi 4: Touchscreen Deactivation and Fullscreen URL Display

This project sets up a Raspberry Pi 4 to automatically disable the touchscreen and open a specified URL in fullscreen mode whenever the device boots. It is ideal for kiosk or display applications.

## Features

- **Touchscreen Deactivation:** Disable the touchscreen input to prevent accidental interactions.
- **Fullscreen URL Display:** Open a specified URL in fullscreen mode using a web browser.

## Hardware Setup

Ensure that your 7-inch display is correctly connected to the Raspberry Pi.

## Software Setup

### Prerequisites

Before you begin, ensure that the following software is installed on your Raspberry Pi:

- Raspberry Pi OS
- Python 3
- Required Python libraries (installed via the `main.sh` script)

### Installation Steps

1. **Clone the Repository:**

    Clone the repository from GitHub to your Raspberry Pi:

    ```bash
    git clone https://github.com/OpenRoboticsGridHardware/DriverStationHub.git
    ```



2. **Run the Installation Script:**

    Execute the installation script to install all dependencies and set up the environment variable:

    ```bash
    ./bash main.sh
    ```

3. **Create a Systemd Service File:**

    Create a `systemd` service file to run the Python script at startup:

    1. Create a new service file:

        ```bash
        sudo nano /etc/systemd/system/fullscreen-browser.service
        ```

    2. Add the following content to the service file:

        ```ini
        [Unit]
        Description=Run Fullscreen Browser Script
        After=network.target

        [Service]
        ExecStart=/usr/bin/python3 /home/pi/your-repo/main.py
        WorkingDirectory=/home/pi/your-repo
        User=pi
        Environment=TARGET_URL=https://example.com
        Restart=always

        [Install]
        WantedBy=multi-user.target
        ```

        Replace `/home/pi/your-repo/main.py` with the actual path to your Python script and `https://example.com` with your desired URL.

    3. Save and close the file by pressing `CTRL + X`, then `Y`, and `Enter`.

4. **Enable and Start the Service:**

    Enable and start the service to ensure it runs at boot:

    ```bash
    sudo systemctl enable fullscreen-browser.service
    sudo systemctl start fullscreen-browser.service
    ```

5. **Reboot the Raspberry Pi:**

    Reboot your Raspberry Pi to test the setup:

    ```bash
    sudo reboot
    ```

6. **Customizing the URL:**

    To change the URL that is displayed:

    1. Edit the `TARGET_URL` environment variable in the `systemd` service file:

        ```bash
        sudo nano /etc/systemd/system/fullscreen-browser.service
        ```

    2. Find the line that sets `Environment=TARGET_URL=https://example.com` and replace the URL with your desired URL.

    3. After making changes, reload the `systemd` daemon and restart the service:

        ```bash
        sudo systemctl daemon-reload
        sudo systemctl restart fullscreen-browser.service
        ```
