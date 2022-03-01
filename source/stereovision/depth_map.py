import cv2
import imutils as imutils
from matplotlib import pyplot as plt
import numpy as np
import json
from stereovision.calibration import StereoCalibrator
from stereovision.calibration import StereoCalibration
import params

class DepthMap():
    def __init__(self, image_path='../scenes/photo.png'):
        self.imageToDisp = image_path
        self.photo_width = params.PHOTO_WIDTH
        self.photo_height = params.PHOTO_HEIGHT
        self.params_file = '../src/pf_'+str(self.photo_width)+'_'+str(self.photo_height)+'.txt'
        # Read parameters for image split
        print ('Loading split parameters...')
        data = json.load(open(self.params_file, 'r'))
        self.imageWidth = data['imageWidth']
        self.jointWidth = data['jointWidth']
        self.leftIndent = data['leftIndent']
        self.rightIndent = data['rightIndent']
        self.image_size = (self.imageWidth - params.WIDTH_OFFSET, self.photo_height)


    def split_image(self):
        print('Reading image rof depth map...')
        pair_img = cv2.imread(self.imageToDisp,0)
        imgLeft = pair_img [0:self.photo_height,self.leftIndent:self.imageWidth]
        cv2.imwrite("../left_sample.jpg", imgLeft)#Y+H and X+W
        imgRight = pair_img [0:self.photo_height,self.rightIndent:self.rightIndent+self.imageWidth-50]
        cv2.imwrite("../right_sample.jpg", imgRight)
        return imgLeft, imgRight

    def plot(self, title, img, i):
        plt.subplot(2, 2, i)
        plt.title(title)
        plt.imshow(img, 'gray')
        plt.gca().get_xaxis().set_visible(False)
        plt.gca().get_yaxis().set_visible(False)

    # Depth map function
    def stereo_depth_map(self,rectified_pair, ndisp, sws):
        # stereo = cv2.StereoBM_create(numDisparities=ndisp,blockSize= sws)
        stereo = cv2.StereoBM(cv2.STEREO_BM_BASIC_PRESET, \
                              ndisparities=ndisp, SADWindowSize=sws)
        return stereo.compute(rectified_pair[0], rectified_pair[1])

    def build_depth_map(self):
        print('Load calibration data...')
        calibration = StereoCalibration(input_folder='../ress')
        rectified_pair = calibration.rectify((self.split_image()))
        disparity = self.stereo_depth_map(rectified_pair, 256, 15)
        print('Building depth map...')
        return rectified_pair, disparity

    def highlight_borders(self):
        pass
        # ret, th = cv2.threshold(gray, 127, 255, 1)
        # kernel = np.ones((15, 15), np.uint8)
        # dilate = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel, 3)
        # contours, hierarchy = cv2.findContours(dilate, 2, 1)
        # cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

    def draw_plot(self,rectified_pair, disparity):
        norm_coeff = 255 / disparity.max()-disparity.min()
        self.plot(u'Left calibrated', rectified_pair[0], 1)
        self.plot(u'Right calibrated', rectified_pair[1], 2)
        self.plot(u'Depth map', disparity/255., 3)
        plt.show()
path_to_image = '../scenes/photo.png'
depthMap = DepthMap(path_to_image)
rectified_pair, disparity = depthMap.build_depth_map()
print('Done! Let\'s look at depth map')
print(disparity.max())
depthMap.draw_plot(rectified_pair, disparity)
depthMap.highlight_borders()
