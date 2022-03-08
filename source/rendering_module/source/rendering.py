import os, sys

import random, math
from roboarm_movement_module.arduino_raspberry_communication import CommunicationArduinoRaspberry
class Scene:
    resolution_x = 1280
    resolution_y = 720
    resolution_percentage = 100

    def __init__(self):
        print("Init camera")

    def set_image_settings(self, file_format, color_mode):

        color_depth = {'RGBA': 8, 'HSVA': 10, 'HexA': 12}

        try:
            if color_mode == 'RGBA':
                file_format = 'PNG'
                color_depth = color_depth['RGBA']
                resolution = (1280,720)
                film_transparent = True
            elif color_mode == 'HSVA':
                file_format = 'JPG'
                color_depth = color_depth['HSVA']
                film_transparent = True
                resolution = (1920, 1080)
            elif color_mode == 'HexA':
                file_format = 'JPG'
                color_depth = color_depth['HexA']
                film_transparent = False
                resolution = (640, 480)
        except KeyError as e:
            raise ValueError('Undefined unit: {}'.format(e.args[0]))
        return file_format, color_mode, color_depth, film_transparent, resolution

    def load_background_images(self, path):
        print('Loading data')
        background_images = [file for file in os.listdir(path) if
                         os.path.isfile(os.path.join(path, file))]
        return background_images

class Object:
    materials = ['metall', 'plastic', 'wood', 'rock', 'marble', 'concrete', 'snow']
    show_material = False
    name = 'socket'
    socket_type = { 'Socket_Type_1' : 0, 'Socket_Type_2' : 1, 'Socket_Type_3' : 2}
    def set_name(self, name):
        if name.isinstance(name, str):
            self.name = name
        return name

    def set_material(self, material):
        if material in self.materials:
            self.show_material = True
        else:
            self.show_material = False

    def set_location(self, x, y, z):
        try:
            if x.isdigit():
                if y.isdigit():
                    if z.isdigit():
                        location = (x, y, z)
        except ValueError as e:
            raise ValueError('Undefined unit: {}'.format(e.args[0]))

        return location

    def set_rotation(self, x, y, z):
        try:
            if x.isdigit() and x in range(-360, 360):
                if y.isdigit() and y in range(-360, 360):
                    if z.isdigit() and z in range(-360, 360):
                        rotation = (x, y, z)
        except ValueError as e:
            raise ValueError('Undefined unit: {}'.format(e.args[0]))

        return rotation

        return material, show_background_images, rotation, location

    def get_classification(self, predictions_path):
        communication = CommunicationArduinoRaspberry()
        test_sample, test_x_data_set, predictions = communication.print_predictions(predictions_path)
        predictions_type = random.randint(0, 2)
        if predictions_type == self.socket_type['Socket_Type_1']:
            print('Socket_Type_1')
            print(predictions)
        elif predictions_type == self.socket_type['Socket_Type_2']:
            print('Socket_Type_2')
            print(predictions)
        if predictions_type == self.socket_type['Socket_Type_3']:
            print('Socket_Type_3')
            print(predictions)
        return self.socket_type
