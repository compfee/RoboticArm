import pytest
import numpy as np
import warnings
from roboarm_move.test_arduino_raspberry_communication import move_x
from roboarm_move.test_arduino_raspberry_communication import print_predictions
from roboarm_move.test_arduino_raspberry_communication import get_project_root

def test_offset_calculating():
    assert move_x([0.2, 0.0, 0.4, 0.0], 90) == (77)
def test_offset_calculating1():
    assert move_x([0.1, 0.0, 0.2, 0.0], 77) == (70)
def test_offset_calculating2():
    assert move_x([0.7, 0.0, 0.9, 0.0], 77) == (89)

def test_predictions_checking():
    frame_path = str(get_project_root())+'/data_Set/frame_path/'
    warnings.warn(UserWarning("smth"))
    test_x_data_set, predictions = print_predictions(frame_path)
    assert all(np.logical_and(predictions[0] > 0, predictions[0] < 1)) == all(np.ones((4), dtype=bool))
