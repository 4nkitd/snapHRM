#!/usr/bin/env python3
import sys
from pathlib import Path

def moveFiles(MainFolders, Folders):

    for main_folder in MainFolders:

        print("\nNow Working in " + main_folder + "\n")

        down_dir = Path.home() / main_folder

        for dest_dir, Extension in Folders.items():

            for filtype in Extension:

                for file in Path(down_dir).glob(filtype):

                    new_target_folder = Path(down_dir / dest_dir)

                    if Path.exists(new_target_folder):
                        print("Processing : " + file.name)
                        print("Moving to : "+dest_dir + "/" + file.name)
                    else:
                        Path.mkdir(new_target_folder)
                        print(dest_dir+" Dir Created")

                    filename = file.name
                    new_target_file = new_target_folder / filename

                    if Path.exists(new_target_file):
                        print("File Alredy Exist, So Deleting " + file.name + "\n")
                        file.unlink()

                    else:
                        file.rename(new_target_folder / filename)
                        print(filename + " | Moved \n")

# code uage is below
    
MainFolders = ['Downloads']

Folders = {
    "Music": ["*.mp3", "*.wav"],
    "Videos": ["*.mkv", "*.mp4", "*.avi", "*.mov"],
    "Compressed": ["*.zip", "*.rar", "*.7z"],
    "Programs": ["*.exe", "*.deb", "*.msi"],
    "Images": ["*.jpg", "*.jpeg", "*.png", "*.svg", "*.css"],
    "Docs": ["*.pdf", "*.docx", "*.doc", "*.ppt", "*.xls", "*.xlsx", "*.txt"],
    "Scripts": ["*.php", "*.sh", "*.html", "*.bat", "*.css"],
    "ISO": ["*.iso"],
    "Others": ["*.*"],
}

moveFiles(MainFolders, Folders)
