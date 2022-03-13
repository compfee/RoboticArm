import os
from pathlib import Path

from utils import get_project_root


def rename_files():
    images_path = str(get_project_root()) + "/source/rename_function_module/pics"
    image_list = os.listdir(images_path)
    for i, image in enumerate(image_list):
        ext = os.path.splitext(image)[1]
        if ext == '.jpg':
            src = images_path + '/' + image
            dst = images_path + '/' + "nh" + str(i) + '.jpg'
            os.rename(src, dst)
            print(i)

