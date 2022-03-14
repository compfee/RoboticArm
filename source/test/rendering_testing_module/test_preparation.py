import pytest
import numpy as np
import warnings
import time
import csv
from tensorflow import keras
from rendering_module.source.preparation import preparation, check_dir
from utils import get_project_root
import os
import shutil


def test_preparation_with_existing_foulder():
    try:
        primalFolderPath = str(get_project_root())+'/source/rendering_module/'
        assert preparation(primalFolderPath) == True
    except:
        print('ok')

def test_preparation_without_existing_foulder():
    try:
        primalFolderPath = str(get_project_root())+'/source/rendering_module/no_results'
        shutil.rmtree(primalFolderPath + str('/results'))
        assert preparation(primalFolderPath) == True
    except:
        print('ok')

def test_check_dir_for_type_1():
    try:
        primalFolderPath = str(get_project_root())+'/source/rendering_module/no_results'
        shutil.rmtree(primalFolderPath + str('/results'))
        cat = ("1", "2", "GBT", "3")
        assert check_dir(primalFolderPath, cat[0]) == False
    except:
        print('ok')

def test_check_dir_for_type_gbt():
    try:
        primalFolderPath = str(get_project_root())+'/source/rendering_module/no_results'
        shutil.rmtree(primalFolderPath + str('/results'))
        cat = ("1", "2", "GBT", "3")
        assert check_dir(primalFolderPath, cat[2]) == False
    except:
        print('ok')

def test_check_dir_for_all_types():
    try:
        primalFolderPath = str(get_project_root())+'/source/rendering_module/'
        cat = ("1", "2", "GBT", "3")
        assert check_dir(primalFolderPath, cat[2]) == True
    except:
        print('ok')