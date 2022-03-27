import os
from os import path

import pytest

import stereovision_module.params as params
from stereovision_module.calibration import Calibrator
from utils import set_stereovision_dir

set_stereovision_dir()

def test_show_rectified_pair():
    calib = Calibrator()
    try:
        calib.show_rectified_pair(100)
        assert False
    except IOError:
        assert True

def test_first_photo_less_than_last():
    assert(params.TOTAL_PHOTOS - params.FIRST_PHOTO > 0)

def test_show_rectified_pair_saving():
    calib = Calibrator()
    calib.show_rectified_pair(1)
    file_path = os.getcwd() + "/rectifyed_left.jpg"
    assert(os.path.isfile(file_path) is True)