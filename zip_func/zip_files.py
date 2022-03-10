import os
import zipfile
from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def zip_files():
    zip_file = zipfile.ZipFile(str(get_project_root()) + "\\zip_func\\archive.zip", 'w')

    for folder, subfolders, files in os.walk(str(get_project_root()) + "\\zip_func\\dataset"):

        for file in files:
            if file.endswith('.csv'):
                zip_file.write(os.path.join(folder, file),
                               os.path.relpath(os.path.join(folder, file), str(get_project_root()) + "\\zip_func"
                                                                                                     "\\dataset"),
                               compress_type=zipfile.ZIP_DEFLATED)

    zip_file.close()

