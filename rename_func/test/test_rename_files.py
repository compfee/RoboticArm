from pathlib import Path
import os
import pytest

from rename_func.rename import get_project_root, rename_files


def test_rename():
    bool = True

    rename_files()

    images_path = str(get_project_root()) + "\\rename_func\\pics"
    image_list = os.listdir(images_path)
    for i, image in enumerate(image_list):
        bool &= image.endswith('nh' + str(i) + '.jpg')
    assert bool == True
