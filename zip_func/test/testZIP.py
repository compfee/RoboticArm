import pytest
import zipfile

from zip_func.zip_files import get_project_root, zip_files
import filecmp


def test_zip():
    zip_files()
    zip_file = zipfile.ZipFile(str(get_project_root()) + "\\zip_func\\archive.zip")
    zip_file.extractall(str(get_project_root()) + "\\zip_func\\extracted")
    zip_file.close()
    assert ((filecmp.cmp(str(get_project_root()) + "\\zip_func\\extracted\\coordi_test.csv",
                         str(get_project_root()) + "\\zip_func\\dataset\\coordi_test.csv")) and (
                filecmp.cmp(str(get_project_root()) +
                            "\\zip_func"
                            "\\extracted"
                            "\\coordi_train.csv",
                            str(get_project_root()) +
                            "\\zip_func"
                            "\\dataset"
                            "\\coordi_train.csv"))) == True

