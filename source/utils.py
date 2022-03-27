import os

from pathlib2 import Path

def get_project_root():
    return Path(__file__).parent.parent

def set_stereovision_dir():
    os.chdir(str(get_project_root()) + '/source/stereovision_testing_module')
