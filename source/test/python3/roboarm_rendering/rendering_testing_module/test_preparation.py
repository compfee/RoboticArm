from rendering_module.source.preparation import preparation, check_dir
from utils import get_project_root
import os
import shutil

# module
# 15
def test_preparation_with_existing_folder():

        primalFolderPath = str(get_project_root())+'/source/rendering_module/'
        assert preparation(primalFolderPath) == True

# 16
def test_preparation_without_existing_folder():

        primalFolderPath = str(get_project_root())+'/source/rendering_module/no_results'
        shutil.rmtree(primalFolderPath + str('/results'))
        assert preparation(primalFolderPath) == True

# 17
def test_check_dir_for_type_1():

        primalFolderPath = str(get_project_root())+'/source/rendering_module/no_results'
        shutil.rmtree(primalFolderPath + str('/results'))
        cat = ("1", "2", "GBT", "3")
        assert check_dir(primalFolderPath, cat[0]) == False

# 18
def test_check_dir_for_type_gbt():

        primalFolderPath = str(get_project_root())+'/source/rendering_module/no_results'
        shutil.rmtree(primalFolderPath + str('/results'))
        cat = ("1", "2", "GBT", "3")
        assert check_dir(primalFolderPath, cat[2]) == False

# 19
def test_check_dir_for_all_types():

        primalFolderPath = str(get_project_root())+'/source/rendering_module/'
        cat = ("1", "2", "GBT", "3")
        assert check_dir(primalFolderPath, cat[2]) == True
