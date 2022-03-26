import os

from utils import get_project_root


def rename_files(directory=str(get_project_root()) + "/source/image_processing_module/rename_function_module/pics"):
    images_path = directory
    image_list = os.listdir(images_path)
    count = 0
    for i, image in enumerate(image_list):
        ext = os.path.splitext(image)[1]
        if ext == '.jpg':
            src = images_path + '/' + image
            dst = images_path + '/' + "nh" + str(i) + '.jpg'
            os.rename(src, dst)
            count += 1
    if count == 0:
        raise "nothing changed("
    else:
        print(str(count) + " files renamed")

