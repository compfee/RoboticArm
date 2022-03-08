import os
import sys


primalFolderPath = 'C:/Users/Somn117/Documents/Blender-Auto-render-main'
# primalFolderPath = input()

if not os.path.isdir(primalFolderPath):
    os.mkdir(primalFolderPath)

categories = ("1", "2", "GBT", "3")

for cat in categories:
    try:
        os.makedirs(primalFolderPath + "/results/" + cat + "/renderresult")
    except FileExistsError:
        print("Folder already exist")
        
    try:
        os.makedirs(primalFolderPath + "/results/" + cat + "/renderresult_white")
    except FileExistsError:
        print("Folder already exist")
        
    try:
        os.makedirs(primalFolderPath + "/results/" + cat + "/csv")
    except FileExistsError:
        print("Folder already exist")
