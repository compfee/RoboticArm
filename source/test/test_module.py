import pytest
import numpy as np
import warnings
import time
from roboarm_move.test_arduino_raspberry_communication import CommunicationArduinoRaspberry
from roboarm_move.test_arduino_raspberry_communication import Camera
from roboarm_move.test_arduino_raspberry_communication import get_project_root
from pytest import main

communication = CommunicationArduinoRaspberry()
camera = Camera()

def test_offset_calculating_left():
    assert communication.move_x([0.2, 0.0, 0.4, 0.0], 90) == (77)

def test_offset_calculating_right():
     assert communication.move_x([0.7, 0.0, 0.9, 0.0], 77) == (89)

def test_predictions_checking():
    frame_path = str(get_project_root())+'/data_Set/frame_path/'
    warnings.warn(UserWarning("smth"))
    test_sample, test_x_data_set, predictions = communication.print_predictions(frame_path)
    assert all(np.logical_and(predictions[0] > 0, predictions[0] < 1)) == all(np.ones((4), dtype=bool))

def test_set_camera():
    resolution = (600, 600)
    rotation = 90
    assert camera.set_camera(resolution, rotation) == ((600, 600),90)

def test_capture():
    path = str(get_project_root())+'/data_Set/frame_path/'
    test_sample, test_x_data_set, predictions = communication.print_predictions(path)
    assert camera.capture(path) == test_sample

def test_sleep():
    camera.sleep(0.1)
    assert camera.sleep(0.1) == time.sleep(0.1)
