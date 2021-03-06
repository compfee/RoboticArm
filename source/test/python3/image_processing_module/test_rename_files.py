import os
import pytest

from image_processing_module.rename_function_module.rename import rename_files
from utils import get_project_root


def test_rename_files():
    bool = True

    rename_files()

    images_path = str(get_project_root()) + "/source/image_processing_module/rename_function_module/pics"
    image_list = os.listdir(images_path)
    for i, image in enumerate(image_list):
        bool &= image.endswith('nh' + str(i) + '.jpg')
    assert bool == True


def test_rename_files_ex():
    with pytest.raises(Exception):
        rename_files(directory=str(get_project_root()) + "/source/image_processing_module/rename_function_module")
