from pathlib import Path
import os
import pytest

from source.rename_function_module.rename import rename_files
from source.utils import get_project_root


def test_rename():
    bool = True

    rename_files()

    images_path = str(get_project_root()) + "\\source\\rename_function_module\\pics"
    image_list = os.listdir(images_path)
    for i, image in enumerate(image_list):
        bool &= image.endswith('nh' + str(i) + '.jpg')
    assert bool == True
