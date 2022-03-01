# import serial

from PIL import Image

import numpy as np
import os
from tensorflow import keras
import csv
# from picamera import PiCamera


WIDTH_ANGLE = 62
HEIGH_ANGLE = 48


def move_x(x, current):
    angle = (x[2] - x[0]) * 62.0

    if (x[0] < 0.5 or x[2] < 0.5):
        print('left')
        offset = int(current - angle)
    else:
        print('right')
        offset = int(current + angle)

    return offset


def connect_ttyACMx():
    print('connect_ttyACMx')
    # try:
    #     ser = serial.Serial('/dev/ttyACM0',9600)
    # except:
    #     ser = serial.Serial('/dev/ttyACM1',9600)
    # time.sleep(2)


def model_load(model_path):
    print("model is loaded")
    model = keras.models.load_model(model_path)
    return model


def set_camera():
    print("set camera")
    # camera = PiCamera()
    # camera.resolution = (2592, 1944)
    # camera.rotation=180


def camera_capture():
    print('capture')
    # camera.start_preview()
    # sleep(2)
    # camera.capture('/home/pi/Downloads/RoboArm/data_Set/with_coordinates/test_arm/data/frame%04d.jpg' % i)
    # i+=1
    # camera.stop_preview()


def print_predictions(test_dir):
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
    model = model_load(model_path)
    predictions = model.predict(test_x_data_set)
    return test_x_data_set, predictions


connect_ttyACMx()
i = 0
model_path = './model/hand_2208'
frame_path = '../../data_Set/data/'
model_load(model_path)
set_camera()
temp = 1

while temp == 1:
    camera_capture()
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
    test_dir = '../../data_Set/data/'
    test_x_data_set, predictions = print_predictions(test_dir)
    j = 0
    with open('../../data_Set/with_coordinates/predictions.csv', 'w') as f:
        # create the csv writer
        writer = csv.writer(f)
        for j in predictions:
            # write a row to the csv file
            writer.writerow(j)
    test_x_data_set[0].shape

    i = 0
    print('pred = ', predictions[i])
    height = predictions[i][2] - predictions[i][0]
    width = predictions[i][3] - predictions[i][1]
    print(height)
    print(width)

    with open('../../data_Set/with_coordinates/predictions.csv') as File:
        reader = csv.reader(File)
        for x in reader:
            # current_middle = int(ser.readline().decode())
            # x_ = [float(x[0]),float(x[1]),float(x[2]),float(x[3])]
            # offset = str(move_x(x_,current_middle))
            #
            # ser.write(offset.encode())
            # print(offset)
            # time.sleep(2)
            print("offset")
    temp = 0


