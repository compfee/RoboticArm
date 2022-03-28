import json
import os

import cv2

import stereovision_module.params as params
from stereovision_module.depth_map import DepthMap
from stereovision_module.image_handler import ImageHandler
from stereovision_module.calibration import Calibrator


def test_show_rectified_pair_saving():
    calib = Calibrator()
    calib.show_rectified_pair(1)
    file_path = os.getcwd() + "/rectifyed_left.jpg"
    assert (os.path.isfile(file_path) is True)

def test_splitting_image():
    imageToDisp = 'scenes/photo.png'
    hand = ImageHandler()
    pair_img = cv2.imread(imageToDisp, 0)
    imgLeft = pair_img[0:hand.photo_height, hand.leftIndent:hand.imageWidth]
    imgRight = pair_img[0:hand.photo_height, hand.rightIndent:hand.rightIndent + hand.imageWidth - 50]
    dm =DepthMap()
    rectified_pair, disparity = dm.build_depth_map("scenes/photo.png", (imgLeft, imgRight))
    assert(rectified_pair, disparity == dm.build_depth_map("scenes/photo.png"))

def test_blind_zones():
    calib = Calibrator()
    fName = calib.add_blind_zones()
    f = open(fName, 'r')
    data = json.load(f)
    f.close()
    assert all(isinstance(value, int) for value in data.values())

def test_pair_img_size():
    imageToDisp = 'scenes/photo.png'
    hand = ImageHandler()
    pair_img = cv2.imread(imageToDisp, 0)
    imgLeft = pair_img[0:hand.photo_height, hand.leftIndent:hand.imageWidth]
    imgRight = pair_img[0:hand.photo_height, hand.rightIndent:hand.rightIndent + hand.imageWidth - 50]
    assert(pair_img.shape[0] == long(hand.photo_height)) and (pair_img.shape[1] == long(hand.photo_width))

def test_json_file_correctness():
    params_file = os.getcwd() + '/3dmap_set.txt'
    f = open(params_file, 'r')
    data = json.load(f)
    f.close()
    assert all(isinstance(value, int) for value in data.values())

