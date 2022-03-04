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
import os

def get_project_root() -> Path:
    return Path(__file__).parent.parent

WIDTH_ANGLE = 62
HEIGH_ANGLE = 48

model_path = str(get_project_root()) + '/roboarm_move/model/hand_2208'
frame_path = str(get_project_root()) + '/data_Set/data/'
test_dir = str(get_project_root())+'/data_Set/data/'

count = 0



class Camera:
    def __init__(self):
        print("Init camera")
        self.resolution = (2592, 1944)
        self.rotation = 180
        self.filesCount = self.capture(test_dir)

    def set_camera(self, resolution, rotation):
        print("Set up camera")
        self.resolution = resolution
        self.rotation = rotation
        return resolution, rotation

    def start_preview(self):
        print("Start preview")

    def stop_preview(self):
        print("Stop preview")

    def capture(self, file_path):
        count = 0
        for base, dirs, files in os.walk(file_path):
            for Files in files:
                print("Make photo frame%04d.jpg" % count)
                count += 1

        print("count = ",count)
        return count


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

    def model_load(self, model_path):
        try:
            model = keras.models.load_model(model_path)
            print("Model is loaded")
            return model
        except FileNotFoundError:
            print("Cannot load model")

    def camera_capture(self):
        camera = Camera()
        camera.start_preview()
        camera.sleep(0.001)
        camera.capture(test_dir)
        camera.stop_preview()

    def print_predictions(self, test_dir):
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
        return test_sample,test_x_data_set, predictions

    def write_predictions_to_csv(self, predictions):
        with open((str(get_project_root())+'/data_Set/with_coordinates/predictions.csv'), 'w') as f:
            # create the csv writer
            writer = csv.writer(f)
            for j in predictions:
                # write a row to the csv file
                writer.writerow(j)

    def calculate_height(self, predictions):
        height = predictions[0][2] - predictions[0][0]
        return height

    def calculate_width(self, predictions):
        width = predictions[0][3] - predictions[0][1]
        return width

    def set_offset(self,current_middle):
        with open(str(get_project_root()) + '/data_Set/with_coordinates/predictions.csv') as File:
            reader = csv.reader(File)
            i = 0
            for x in reader:
                if x != []:
                    print('Predictions = ', predictions[i])
                    print('Height = ', communication.calculate_height(predictions))
                    print('Width = ', communication.calculate_width(predictions))
                    x_ = [float(x[0]),float(x[1]),float(x[2]),float(x[3])]

                    offset = communication.move_x(x_, current_middle)
                    # ser.write(offset.encode())
                    # print(offset)
                    # time.sleep(2)
                    current_middle = offset
                    i += 1
                    print("Current = ", current_middle)

if __name__ == '__main__':
    i = 0
    temp = 0
    current_middle = 90
    camera = Camera()
    communication = CommunicationArduinoRaspberry()
    communication.connect_ttyACMx()
    communication.model_load(model_path)
    camera.set_camera((2592, 1944), 180)

    while temp != 1:
        communication.camera_capture()
        test_sample, test_x_data_set, predictions = communication.print_predictions(test_dir)
        communication.write_predictions_to_csv(predictions)
        test_x_data_set[0].shape


        communication.set_offset(current_middle)

        temp += 1




