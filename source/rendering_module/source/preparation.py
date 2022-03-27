import os
import sys


# primalFolderPath = 'C:/Users/Somn117/Documents/Blender-Auto-render-main'
# primalFolderPath = input()
class Preparation:
    def __init__(self):
        print("Init Preparation")
    def check_dir(self,primalFolderPath, cat):
        try:
            os.makedirs(primalFolderPath + cat)
            return False
        except FileExistsError:
            print("Folder already exist")
            return True

    def preparation(self,primalFolderPath):
        if not os.path.isdir(primalFolderPath):
            os.mkdir(primalFolderPath)
        categories = ("1", "2", "GBT", "3")
        for cat in categories:
            self.check_dir(primalFolderPath, cat)
        return True


