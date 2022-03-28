import os

import pytest
import zipfile

from image_processing_module.zip_function_module.zip_function import zip_func  ##
from utils import get_project_root
from roboarm_movement_module.arduino_raspberry_communication import CommunicationArduinoRaspberry
import filecmp


def test_zip_function():
    zip_func()
    zip_file = zipfile.ZipFile(str(get_project_root()) + "/source/image_processing_module/zip_function_module/archive"
                                                         ".zip")
    zip_file.extractall(str(get_project_root()) + "/source/image_processing_module/zip_function_module/extracted")
    zip_file.close()
    assert ((filecmp.cmp(str(get_project_root()) + "/source/image_processing_module/zip_function_module/extracted"
                                                   "/coordi_test.csv",
                         str(get_project_root()) + "/source/image_processing_module/zip_function_module/dataset"
                                                   "/coordi_test.csv")) and (
                filecmp.cmp(str(get_project_root()) +
                            "/source/image_processing_module/zip_function_module"
                            "/extracted"
                            "/coordi_train.csv",
                            str(get_project_root()) +
                            "/source/image_processing_module/zip_function_module"
                            "/dataset"
                            "/coordi_train.csv"))) == True


def test_zip_func_is_empty():
    with pytest.raises(Exception):
        zip_func(direction2=str(get_project_root()) + "/source/image_processing_module/test/zip_function_module")


def test_zip_function_is_compressed():
    orig_sum = 0
    originals_path = str(get_project_root()) + '/source/image_processing_module/zip_function_module/dataset'

    zip_func()

    for path, dirs, files in os.walk(originals_path):
        for f in files:
            fp = os.path.join(path, f)
            orig_sum += os.path.getsize(fp)

    comp_sum = os.stat(
        str(get_project_root()) + "/source/image_processing_module/zip_function_module/archive.zip").st_size

    assert comp_sum < orig_sum


def test_integr_zip_csv():
    car = CommunicationArduinoRaspberry()
    predictions = [[0.1, 0.2, 0.3, 0.4], [0.0, 0.0, 0.0, 0.0]]
    predictions_path = predictions_path = str(get_project_root()) + '/source/data_Set/with_coordinates/predictions.csv'
    car.write_predictions_to_csv(predictions, predictions_path)
    assert os.stat(str(get_project_root()) + "/source"
                                             "/image_processing_module"
                                             "/zip_function_module/csv"
                                             "/archive_csv.zip").st_size != 0
