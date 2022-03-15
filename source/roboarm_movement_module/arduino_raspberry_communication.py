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
from source.utils import get_project_root
from source.camera_module.camera import Camera

WIDTH_ANGLE = 62
HEIGH_ANGLE = 48

model_path = str(get_project_root()) + '/source/roboarm_movement_module/model/hand_2208'
frame_path = str(get_project_root()) + '/source/data_Set/data/'
test_dir = str(get_project_root())+'/source/data_Set/data/'
predictions_path = str(get_project_root())+'/source/data_Set/with_coordinates/predictions.csv'
count = 0


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

    def connect_ttyACMx(self, ttyACMx):
        try:
            if ttyACMx == 1:
                return "ttyACM1"
            elif ttyACMx == 0:
                return "ttyACM0"
            else:
                raise ValueError('Device not found1')
        except :
            raise ValueError('Device not found1')


    def model_load(self, model_path):
        try:
            model = keras.models.load_model(model_path)
            print("Model is loaded")
            return model
        except:
            print("Cannot load model")
            raise FileNotFoundError

    def camera_capture(self, test_dir):
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

    def write_predictions_to_csv(self, predictions, predictions_path):
        try:
            with open(predictions_path, 'w') as f:
            # create the csv writer
                writer = csv.writer(f)
                for j in predictions:
                    # write a row to the csv file
                    writer.writerow(j)
        except:
            raise FileNotFoundError

    def calculate_height(self, predictions):
        try:
            height = predictions[2] - predictions[0]
            return height
        except:
            raise TypeError("Predictions have wrong type")

    def calculate_width(self, predictions):
        try:
            width = predictions[3] - predictions[1]
            return width
        except:
            raise TypeError("Predictions have wrong type")

    def read_predictions_csv(self,predictions_path,i):
        i=0
        test_dir = str(get_project_root()) + '/source/data_Set/data/'
        test_sample = len(os.listdir(test_dir))
        x_= [[0] * 4 for i in range(test_sample)]
        try:
            with open(predictions_path) as File:
                reader = csv.reader(File)
                for x in reader:
                    if x != []:
                        x_[i] = [float(x[0]),float(x[1]),float(x[2]),float(x[3])]
                        i+=1
            return x_
        except:
            raise FileNotFoundError("There is no predictions file")

    def set_offset(self,current_middle):
        i = 0
        test_dir = str(get_project_root()) + '/source/data_Set/data/'
        test_sample = len(os.listdir(test_dir))
        for i in range(0,test_sample):
            x_= self.read_predictions_csv(predictions_path, i)
            print('Predictions = ', x_[i])
            print('Height = ', self.calculate_height(x_[i]))
            print('Width = ', self.calculate_width(x_[i]))
            offset = self.move_x(x_[i], current_middle)
            current_middle = offset
            i += 1
            print("Current = ", current_middle)
        return current_middle

if __name__ == '__main__':
    i = 0
    temp = 0
    current_middle = 90
    camera = Camera()
    communication = CommunicationArduinoRaspberry()
    communication.connect_ttyACMx(1)
    communication.model_load(model_path)
    camera.set_camera((2592, 1944), 180)

    while temp != 1:
        communication.camera_capture(test_dir)
        test_sample, test_x_data_set, predictions = communication.print_predictions(test_dir)
        communication.write_predictions_to_csv(predictions, predictions_path)
        test_x_data_set[0].shape
        communication.set_offset(current_middle)
        temp += 1




