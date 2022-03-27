import os
import zipfile

from utils import get_project_root


def zip_func(direction=str(get_project_root()) + "/source/image_processing_module/zip_function_module/dataset"):
    zip_file = zipfile.ZipFile(str(get_project_root()) + "/source/image_processing_module/zip_function_module/archive"
                                                         ".zip", 'w')

    for folder, subfolders, files in os.walk(direction):
        for file in files:
            if file.endswith('.csv'):
                zip_file.write(os.path.join(folder, file),
                               os.path.relpath(os.path.join(folder, file),
                                               str(get_project_root()) + "/source/image_processing_module"
                                                                         "/zip_function_module "
                                                                         "/dataset"),
                               compress_type=zipfile.ZIP_DEFLATED)

    if os.stat(str(get_project_root()) + "/source/image_processing_module/zip_function_module/archive.zip").st_size == 0:
        raise "nothing to compress"

    zip_file.close()
