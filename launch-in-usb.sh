#!/usr/bin/env bash

# Define the mount point for the USB drive
usb_location_point="/run/media/richard/Ventoy"

# Copy the files from the USB to your local system
cp "$usb_location_point/MAPIS" "$HOME/"
 
# Run the scripts
"$HOME/MAPIS/install.sh"
"$HOME/MAPIS/i3wmconfig-usb.sh"

# Unmount the USB drive
sudo umount "$usb_location_point"
