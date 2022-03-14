from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
from pathlib import Path
import csv
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Dropout
from keras.models import load_model


from utils import get_project_root


train_label_file = str(get_project_root()) + "/source/image_processing_module/hand_regress_module/dataSet" \
                                             "/coordi_train.csv "
test_label_file = str(get_project_root()) + "/source/image_processing_module/hand_regress_module/dataSet/coordi_test" \
                                            ".csv "


class GetDataSet:
    def __init__(self):
        print("getting dataset")
        self.train_coordi_dict = {}
        self.test_coordi_dict = {}

    def get_data_set(self):
        with open(train_label_file) as f:
            lines = f.read().splitlines()
        for line in lines:
            elements = line.split(',')
            self.train_coordi_dict[elements[0]] = elements[1:]

        with open(test_label_file) as f:
            lines = f.read().splitlines()
        for line in lines:
            elements = line.split(',')
            self.test_coordi_dict[elements[0]] = elements[1:]

        train_sample = len(self.train_coordi_dict)
        test_sample = len(self.test_coordi_dict)
        print("Train Set samples: " + str(train_sample))
        print("Test Set samples: " + str(test_sample))



