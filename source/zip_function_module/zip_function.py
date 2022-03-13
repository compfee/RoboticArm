import os
import zipfile
from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def zip_func(direction=str(get_project_root()) + "/zip_function_module/dataset"):
    zip_file = zipfile.ZipFile(str(get_project_root()) + "/zip_function_module/archive.zip", 'w')

    for folder, subfolders, files in os.walk(direction):
        for file in files:
            if file.endswith('.csv'):
                zip_file.write(os.path.join(folder, file),
                               os.path.relpath(os.path.join(folder, file),
                                               str(get_project_root()) + "/zip_function_module"
                                                                         "/dataset"),
                               compress_type=zipfile.ZIP_DEFLATED)

    if os.stat(str(get_project_root()) + "/zip_function_module/archive.zip").st_size == 0:
        raise "nothing to compress"

    zip_file.close()

