import os
import zipfile

from utils import get_project_root


def zip_func(direction=str(get_project_root()) + "/source/image_processing_module/zip_function_module/dataset", direction2 = str(get_project_root()) + "/source/image_processing_module/zip_function_module/archive.zip"):
    zip_file = zipfile.ZipFile(direction2, 'w')

    for folder, subfolders, files in os.walk(direction):
        for file in files:
            if file.endswith('.csv'):
                zip_file.write(os.path.join(folder, file),
                               os.path.relpath(os.path.join(folder, file),
                                               direction),
                               compress_type=zipfile.ZIP_DEFLATED)

    if os.stat(direction2).st_size == 0:
        raise "nothing to compress"

    zip_file.close()
