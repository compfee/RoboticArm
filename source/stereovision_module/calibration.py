import json
import logging
import os

import cv2
from stereovision.calibration import StereoCalibration
from stereovision.calibration import StereoCalibrator

import params
from image_handler import ImageHandler

#logging.basicConfig(level='INFO')
__metaclass__ = type

class Calibrator(ImageHandler):
    # Global variables preset
    def __init__(self):
        super(Calibrator, self).__init__()

    def take_photos(self):
        self.calibrator = StereoCalibrator(self.rows, self.columns, self.square_size, self.image_size)
        photo_counter = params.FIRST_PHOTO
        print ('Start cycle')

        while photo_counter != params.TOTAL_PHOTOS:
          photo_counter = photo_counter + 1
          print ('Import pair No ' + str(photo_counter))
          # leftName = 'pairs/left_'+str(photo_counter).zfill(2)+'.png'
          # rightName = 'pairs/right_'+str(photo_counter).zfill(2)+'.png'
          # if os.path.isfile(leftName) and os.path.isfile(rightName):
          #     imgLeft = cv2.imread(leftName,1)
          #     imgRight = cv2.imread(rightName,1)
          #     self.calibrator.add_corners((imgLeft, imgRight), True)
          #     pass
        # print ('End cycle')

    def calibrate_camera(self):
        logging.info('Starting calibration... It can take several minutes!')
        calibration = self.calibrator.calibrate_cameras()
        calibration.export('ress')
        logging.info('Calibration complete!')

    def show_rectified_pair(self, number_of_image):
        calibration = StereoCalibration(input_folder='ress')
        leftName = 'pairs/left_' + str(number_of_image).zfill(2) + '.png'
        rightName = 'pairs/right_' + str(number_of_image).zfill(2) + '.png'
        imgLeft = cv2.imread(leftName, 1)
        imgRight = cv2.imread(rightName, 1)
        if imgRight is None or imgLeft is None:
            raise IOError("Could not find pairs")
        self.rectified_pair = calibration.rectify((imgLeft, imgRight))
        # cv2.imshow('Left CALIBRATED', self.rectified_pair[0])
        # cv2.imshow('Right CALIBRATED', self.rectified_pair[1])
        cv2.imwrite("rectifyed_left.jpg",self.rectified_pair[0])
        cv2.imwrite("rectifyed_right.jpg",self.rectified_pair[1])
        cv2.waitKey(0)

    def add_blind_zones(self):
        showHelp = 1
        pwidth = params.PHOTO_WIDTH
        pheight = params.PHOTO_HEIGHT
        loadImagePath = ""
        recX = int(0.475 * pwidth)
        recY = pheight
        recW = int(pwidth / 20)
        minW = min(recX, pwidth - recX - recW)
        leftX1 = recX - minW
        leftX2 = recX
        rightX1 = recX + recW
        rightX2 = rightX1 + minW
        print ('imageWidth = ', minW, ' jointWidth=', recW, ' leftIndent=', leftX1, \
                ' rightIndent=', rightX1)
        result = json.dumps({'imageWidth': minW, 'leftIndent': leftX1, \
                                 'rightIndent': rightX1, 'jointWidth': recW}, sort_keys=True, \
                                indent=4, separators=(',', ':'))
        fName = 'pf_' + str(pwidth) + '_' + str(pheight) + '.txt'
        f = open(str(fName), 'w')
        f.write(result)
        f.close()
        print ('Settings saved to file' + str(fName))
        return fName