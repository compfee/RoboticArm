import pytest
import zipfile

from zip_function_module.zip_function import zip_func
from utils import get_project_root
import filecmp


def test_zip_function():
    zip_func()
    zip_file = zipfile.ZipFile(str(get_project_root()) + "/source/zip_function_module/archive.zip")
    zip_file.extractall(str(get_project_root()) + "/source/zip_function_module/extracted")
    zip_file.close()
    assert ((filecmp.cmp(str(get_project_root()) + "/source/zip_function_module/extracted/coordi_test.csv",
                         str(get_project_root()) + "/source/zip_function_module/dataset/coordi_test.csv")) and (
                filecmp.cmp(str(get_project_root()) +
                            "/source/zip_function_module"
                            "/extracted"
                            "/coordi_train.csv",
                            str(get_project_root()) +
                            "/source/zip_function_module"
                            "/dataset"
                            "/coordi_train.csv"))) == True


def test_zip_func_is_empty():
    with pytest.raises(Exception):
        zip_func(str(get_project_root()) + "/source/test/zip_function_module")
