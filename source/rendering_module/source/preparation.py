import os
import sys


# primalFolderPath = 'C:/Users/Somn117/Documents/Blender-Auto-render-main'
# primalFolderPath = input()
def check_dir(primalFolderPath, cat):
    try:
        os.makedirs(primalFolderPath + "/results/" + cat)
        return False
    except FileExistsError:
        print("Folder already exist")
        return True

def preparation(primalFolderPath):
    if not os.path.isdir(primalFolderPath):
        os.mkdir(primalFolderPath)
    categories = ("1", "2", "GBT", "3")

    for cat in categories:
        check_dir(primalFolderPath, cat)
    return True