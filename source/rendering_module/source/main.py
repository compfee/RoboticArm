# Paths
BACKGROUND_PATH = "C:/Users/Somn117/Documents/Blender-Auto-render-main/backgrounds/"
import os
import random, math
from rendering_module.source.rendering import Scene, Object
from roboarm_movement_module.arduino_raspberry_communication import CommunicationArduinoRaspberry
from utils import get_project_root

if __name__ == '__main__':
    scene = Scene()
    object = Object()
    communication = CommunicationArduinoRaspberry()
    os.system('python ' + str(get_project_root()) + '/source/rendering_module/source/preparation.py')
    scene.load_background_images(BACKGROUND_PATH)
    default_rotation_obj = (math.radians(90), math.radians(0), math.radians(0))
    #
    # obj = data.objects['Socket_Type_1']
    # cam = data.objects['Camera']
    #
    # # To rescale coordinates
    # res_x = render.resolution_x
    # res_y = render.resolution_y
    #
    # for i in range(10):
    #     # Random rotation
    #     rot_x = random.randint(-30, 30)
    #     rot_y = random.randint(-30, 30)
    #     rot_z = random.randint(-90, 90)
    #
    #     obj.rotation_euler = (math.radians(90 + rot_x), math.radians(rot_y), math.radians(rot_z))
    #
    #     # Random movement
    #     mov_x = random.uniform(-4, 4)
    #     mov_y = random.uniform(-2, 2)
    #     mov_z = random.uniform(0, 10)
    #
    #     obj.location = (mov_x, mov_y, 0)
    #     cam.location = (0, 0, 15 + mov_z)
    #
    #     # Set random background
    #     rand_index = random.randint(0, len(background_images) - 1)
    #
    #     cam.data.show_background_images = True
    #     bg = cam.data.background_images.new()
    #     # bg.image = data.images.get(background_images[rand_index])
    #     # bg.show_background_image = True
    #     # bg.alpha = 1
    #
    #     # Set random material
    #     rand_index = random.randint(0, len(data.materials) - 1)
    #
    #     mat = data.materials[rand_index]
    #
    #     obj.data.materials.append(mat)

