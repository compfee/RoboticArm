
from utils import get_project_root
import os
import shutil
from rendering_module.source.preparation import Preparation
preparation = Preparation()
primalFolderPath = str(get_project_root())+'/source/rendering_module/no_results/results/'
try:
        os.makedirs(primalFolderPath + "/GBT")
except :
        True

# module
# 17
def test_preparation_with_existing_folder():

        primalFolderPath = str(get_project_root())+'/source/rendering_module/results/'
        assert preparation.preparation(primalFolderPath) == True

# 18
def test_preparation_without_existing_folder():

        primalFolderPath = str(get_project_root())+'/source/rendering_module/no_results/results/'
        shutil.rmtree(primalFolderPath )
        assert preparation.preparation(primalFolderPath) == True

# 19
def test_check_dir_for_type_1():

        primalFolderPath = str(get_project_root())+'/source/rendering_module/no_results/results/'
        shutil.rmtree(primalFolderPath)
        cat = ("1", "2", "GBT", "3")
        assert preparation.check_dir(primalFolderPath, cat[0]) == False

# 20
def test_check_dir_for_type_gbt():

        primalFolderPath = str(get_project_root())+'/source/rendering_module/no_results/results/'
        shutil.rmtree(primalFolderPath)
        cat = ("1", "2", "GBT", "3")
        assert preparation.check_dir(primalFolderPath, cat[2]) == False

# 21
def test_check_dir_for_all_types():

        primalFolderPath = str(get_project_root())+'/source/rendering_module/results/'
        cat = ("1", "2", "GBT", "3")
        assert preparation.check_dir(primalFolderPath, cat[2]) == True
