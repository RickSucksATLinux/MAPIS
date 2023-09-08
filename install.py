import subprocess
import os
import shutil

# List of packages to install
packages = ["discord", "zip", "unzip", "steam", "wine", "git", "lutris", "jre-openjdk", "jdk-openjdk", "imagemagick"]

# Iterate through the list of packages and install them
for package in packages:
    command = f"sudo pacman -S {package}"
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"{package} has been successfully installed.")
    except subprocess.CalledProcessError:
        print(f"An error occurred while trying to install {package}.")

#Define the git command and arguments

git = 'git'
git_args = ["clone", "https://aur.archlinux.org/yay.git"]

#Run git 
try:
    subprocess.run([git] + git_args, check=True)
    print("git is done cloning the repo.")
except subprocess.CalledProcessError:
    print(f"git has failed cloning the repo.")

#change direcctory to ~/yay

os.chdir("/home/richard/yay")

#run makepkg -si to install yay

try:
    subprocess.run(["makepkg", "-si"], check=True)
    print("yay has finished installing.")
except subprocess.CalledProcessError:
    print("yay has failed installing.")

#install apps with yay

yay_packages = ["vinegar", "catppuccin-gtk-theme-mocha", "viber", "zoom", "mangohud", "protonup-qt", "picom-git", "an-anime-game-launcher-bin", "lunar-client"]

#constuct and yay command

yay = ["yay", "-S"] + yay_packages

#use subprocess to run the yay command 
try:
    subprocess.run (yay, check=True)
    print('yay has completed installing applications from the AUR.')
except subprocess.CalledProcessError:
    print("Yay has failed isntalling applications.")

#Install BetterDiscord

wget = "/usr/bin/wget"
wget_arguments= ["https://github.com/BetterDiscord/Installer/releases/latest/download/BetterDiscord-Linux.AppImage"]
try:
    subprocess.run([wget] + wget_arguments, check=True)
    print("wget has successfully downloaded the AppImage.")
except subprocess.CalledProcessError:
    print("wget has failed downloading.")

#Execute BetterDiscord

# Define the file you want to make executable
file_path = "/home/richard/yay/BetterDiscord-Linux.AppImage"

try:
    subprocess.run(["chmod", "+x", file_path], check=True)
    print(f"{file_path} has been made executable.")
except subprocess.CalledProcessError:
    print(f"Failed to make {file_path} executable.")


btr_discord = ["/home/richard/BetterDiscord-Linux.AppImage"]

try:
    subprocess.run(btr_discord , shell=True , check=True)
except subprocess.CalledProcessError:
    print("BetterDiscord has failed.")

# Define source and destination paths
source_paths = ["/run/media/richard/Ventoy/kitty", "/run/media/richard/Ventoy/i3"]
destination_path = "~/.config"  # Replace with the desired destination path

# Expand the user's home directory (~) in the destination path
destination_path = os.path.expanduser(destination_path)

# Loop through the source paths and copy them to the destination
for source_path in source_paths:
    try:
        shutil.copytree(source_path, os.path.join(destination_path, os.path.basename(source_path)))
        print(f"Folder {source_path} copied to {destination_path}.")
    except FileNotFoundError:
        print(f"Folder {source_path} not found.")
    except FileExistsError:
        print(f"Folder {os.path.basename(source_path)} already exists in {destination_path}.")

print("All folders have been copied.")

subprocess.run("xfce4-session-settings", shell=True, check=True)

#List of packages to remove
packages_to_remove = ["xfdesktop", "xfwm4"]

#construct the command
remove_command = ["sudo", "pacman", "-Rsc"] + packages_to_remove

#run the command
try:
    subprocess.run(remove_command, check=True)
except subprocess.CalledProcessError:
    print("An error occured while removing packages.")