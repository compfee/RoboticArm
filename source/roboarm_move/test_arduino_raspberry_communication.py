# import serial

from PIL import Image

import numpy as np
import os
from tensorflow import keras
import csv
# from picamera import PiCamera
from pathlib import Path
import usb.core
import usb.util
import time

def get_project_root() -> Path:
    return Path(__file__).parent.parent

WIDTH_ANGLE = 62
HEIGH_ANGLE = 48

model_path = str(get_project_root()) + '/roboarm_move/model/hand_2208'
frame_path = str(get_project_root()) + '/data_Set/data/'

class Camera:
    def __init__(self):
        print("Init camera")
        self.resolution = (2592, 1944)
        self.rotation = 180
        self.filesCount = 20

    def start_preview(self):
        print("Start preview")

    def stop_preview(self):
        print("Stop preview")

    def capture(self, path):
        for i in range(self.filesCount):
            print("Make photo frame%04d.jpg" % i)
        return i
    def sleep(self, sec):
        time.sleep(sec)

class CommunicationArduinoRaspberry:
    def __init__(self):
        print("Init")

    def move_x(self, x, current):
        angle = (x[2] - x[0]) * 62.0

        if (x[0] < 0.5 or x[2] < 0.5):
            print('Left')
            offset = int(current - angle)
        else:
            print('Right')
            offset = int(current + angle)

        return offset


    def connect_ttyACMx(self):
        print('Connect to ttyACMx')
        try:
            dev = usb.core.find(idVendor=0xfffe, idProduct=0x0001)
        except:
            print('Device not found')

        # try:
        #     ser = serial.Serial('/dev/ttyACM0',9600)
        # except:
        #     ser = serial.Serial('/dev/ttyACM1',9600)
        # time.sleep(2)


    def model_load(self, model_path):
        try:
            model = keras.models.load_model(model_path)
            print("Model is loaded")
            return model
        except FileNotFoundError:
            print("Cannot load model")



    def set_camera(self):
        camera = Camera()
        print("Set up camera")
        return camera.resolution, camera.rotation


    def camera_capture(self):
        path = str(get_project_root()) + '/data_Set/frames_from_camera/'
        camera = Camera()
        print('Capture')
        camera.start_preview()
        camera.sleep(0.001)
        camera.capture(path)
        camera.stop_preview()


    def print_predictions(self, test_dir):
        # test_dir = 'C:/Users/Somn117/Documents/RoboticArm/data_Set/data/'
        test_sample = len(os.listdir(test_dir))
        test_x_data_set = np.zeros([test_sample, 100, 100, 3])
        print("Test Set samples: " + str(test_sample))
        for index, filename in enumerate(os.listdir(test_dir)):
            img = Image.open(test_dir + filename)
            img = img.resize((100, 100), Image.ANTIALIAS)
            im = np.array(img)
            test_x_data_set[index, :, :, :] = im

        test_x_data_set = test_x_data_set / 255
        model = self.model_load(model_path)
        predictions = model.predict(test_x_data_set)
        return test_x_data_set, predictions

if __name__ == '__main__':
    i = 0
    temp = 1
    communication = CommunicationArduinoRaspberry()
    communication.connect_ttyACMx()
    communication.model_load(model_path)
    communication.set_camera()

    while temp == 1:
        communication.camera_capture()
        # test_dir = 'C:/Users/Somn117/Documents/RoboticArm/data_Set/data/'
        # test_sample = len(os.listdir(test_dir))
        # test_x_data_set = np.zeros([test_sample, 100, 100, 3])
        # print("Test Set samples: " + str(test_sample))
        # for index, filename in enumerate(os.listdir(test_dir)):
        #     img = Image.open(test_dir + filename)
        #     img = img.resize((100, 100), Image.ANTIALIAS)
        #     im = np.array(img)
        #     test_x_data_set[index, :, :, :] = im
        #
        # test_x_data_set = test_x_data_set / 255
        # model = model_load(path)
        test_dir = str(get_project_root())+'/data_Set/data/'
        test_x_data_set, predictions = communication.print_predictions(test_dir)
        j = 0
        with open(str(get_project_root())+'/data_Set/with_coordinates/predictions.csv', 'w') as f:
            # create the csv writer
            writer = csv.writer(f)
            for j in predictions:
                # write a row to the csv file
                writer.writerow(j)
        test_x_data_set[0].shape

        i = 0
        print('Pred = ', predictions[i])
        height = predictions[i][2] - predictions[i][0]
        width = predictions[i][3] - predictions[i][1]
        print(height)
        print(width)

        with open(str(get_project_root())+'/data_Set/with_coordinates/predictions.csv') as File:
            reader = csv.reader(File)
            for x in reader:
                # current_middle = int(ser.readline().decode())
                # x_ = [float(x[0]),float(x[1]),float(x[2]),float(x[3])]
                # offset = str(move_x(x_,current_middle))
                #
                # ser.write(offset.encode())
                # print(offset)
                # time.sleep(2)
                print("Offset")
        temp = 0




