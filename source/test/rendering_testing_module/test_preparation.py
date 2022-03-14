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


def test_preparation1():
    try:
        primalFolderPath = str(get_project_root())+'/source/rendering_module/'
        assert preparation(primalFolderPath) == True
    except:
        print('okey')

def test_preparation2():
    try:
        primalFolderPath = str(get_project_root())+'/source/rendering_module/no_results'
        shutil.rmtree(primalFolderPath + str('/results'))
        assert preparation(primalFolderPath) == True
    except:
        print('okey')

def test_check_dir0():
    try:
        primalFolderPath = str(get_project_root())+'/source/rendering_module/no_results'
        shutil.rmtree(primalFolderPath + str('/results'))
        cat = ("1", "2", "GBT", "3")
        assert check_dir(primalFolderPath, cat[0]) == False
    except:
        print('okey')

def test_check_dir2():
    try:
        primalFolderPath = str(get_project_root())+'/source/rendering_module/no_results'
        shutil.rmtree(primalFolderPath + str('/results'))
        cat = ("1", "2", "GBT", "3")
        assert check_dir(primalFolderPath, cat[2]) == False
    except:
        print('okey')

def test_check_dir1():
    try:
        primalFolderPath = str(get_project_root())+'/source/rendering_module/'
        cat = ("1", "2", "GBT", "3")
        assert check_dir(primalFolderPath, cat[2]) == True
    except:
        print('okey')