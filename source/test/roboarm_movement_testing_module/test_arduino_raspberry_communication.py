import pytest
import numpy as np
import warnings
import time
import csv
from tensorflow import keras
from roboarm_movement_module.arduino_raspberry_communication import Camera
from roboarm_movement_module.arduino_raspberry_communication import CommunicationArduinoRaspberry
from pytest import main
from utils import get_project_root

communication = CommunicationArduinoRaspberry()
camera = Camera()

def test_offset_calculating_left():
    assert communication.move_x([0.2, 0.0, 0.4, 0.0], 90) == (77)

def test_offset_calculating_right():
     assert communication.move_x([0.7, 0.0, 0.9, 0.0], 77) == (89)

def test_predictions_checking():
    frame_path = str(get_project_root())+'/source/data_Set/frame_path/'
    test_sample, test_x_data_set, predictions = communication.print_predictions(frame_path)
    assert all(np.logical_and(predictions[0] > 0, predictions[0] < 1)) == all(np.ones((4), dtype=bool))

def test_set_camera():
    resolution = (600, 600)
    rotation = 90
    assert camera.set_camera(resolution, rotation) == ((600, 600), 90)

def test_capture():
    path = str(get_project_root())+'/source/data_Set/frame_path/'
    test_sample, test_x_data_set, predictions = communication.print_predictions(path)
    assert camera.capture(path) == test_sample

def test_sleep():
    camera.sleep(0.1)
    assert camera.sleep(0.1) == time.sleep(0.1)

def test_model_load():
    model_path = str(get_project_root()) + '/source/data_Set/frame_path/'
    with pytest.raises(FileNotFoundError):
        communication.model_load(model_path)

def test_calculate_height():
    predictions = [0.1,0.2,0.3,0.4]
    pred =  [0.1,0.2,0.3,0.4],[0,0,0,0]
    # h_except = predictions[2]-predictions[0]
    h = pred[0][2] - pred[0][0]
    assert communication.calculate_height(predictions) == h
    with pytest.raises(TypeError):
        communication.calculate_height(pred)

def test_calculate_width():
    predictions = [0.1, 0.2, 0.3, 0.4]
    pred = [0.1, 0.2, 0.3, 0.4],[0, 0, 0, 0]
    w = pred[0][2] - pred[0][0]
    assert communication.calculate_height(predictions) == w
    with pytest.raises(TypeError):
        communication.calculate_width(pred)

def test_write_predictions_to_csv():
    pred = [0.1, 0.2, 0.3, 0.4], [0, 0, 0, 0]
    predictions_path = str(get_project_root()) + '/source/data_Set/with_coordinates/predictions.csv'
    random_path = str(get_project_root()) + '/source/data_Set/frame_path/'
    communication.write_predictions_to_csv(pred, predictions_path)

    with open(str(get_project_root()) + '/source/data_Set/with_coordinates/predictions.csv') as File:
        reader = csv.reader(File)
        i = 0
        for x in reader:
            if x != []:
                x_ = [float(x[0]), float(x[1]), float(x[2]), float(x[3])]

    with pytest.raises(FileNotFoundError):
        communication.write_predictions_to_csv(pred, random_path)

def test_connect_ttyACM1():
    assert communication.connect_ttyACMx(1) == "ttyACM1"

def test_connect_ttyACM0():
    assert communication.connect_ttyACMx(0) == "ttyACM0"

def test_connect_ttyACMx():
    with pytest.raises(ValueError):
        communication.connect_ttyACMx(6)

def test_read_predictions_csv():
    predictions_path = str(get_project_root()) + '/source/data_Set/with_coordinates/predictions.csv'
    random_path = str(get_project_root()) + '/source/data_Set/frame_path/'
    test_dir = str(get_project_root()) + '/source/data_Set/data/'

    pred = [[0.1, 0.2, 0.3, 0.4], [0.0, 0.0, 0.0, 0.0]]
    test_sample,test_x_data_set, predictions = communication.print_predictions(test_dir)
    print(communication.read_predictions_csv(predictions_path, 1))
    assert communication.read_predictions_csv(predictions_path, 1) == pred
    with pytest.raises(FileNotFoundError):
        communication.read_predictions_csv(random_path, 1)

def test_set_offset():
    assert communication.set_offset(90) == 77

