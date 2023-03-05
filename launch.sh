#!/usr/bin/env bash

# Clone the repository
git clone https://github.com/RickSucksATLinux/MAPIS.git

# Copy the scripts to the home directory
cp MAPIS/install.sh ~/
cp MAPIS/i3wmconfig.sh ~/

# Run the scripts
bash ~/install.sh
bash ~/i3wmconfig.sh
