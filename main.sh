#!/bin/bash

# Install necessary packages
echo "Installing necessary packages..."
sudo apt-get update
sudo apt-get install -y xinput xdotool chromium-browser

# Set environment variable for the URL
echo "Setting up environment variable..."
echo "export TARGET_URL='https://example.com'" >> ~/.bashrc  # Replace with your URL
source ~/.bashrc

# Make sure the environment variable is available for the session
export TARGET_URL=$TARGET_URL

echo "Installation and setup complete."
