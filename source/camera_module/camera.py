
import time
import os
from source.utils import get_project_root

test_dir = str(get_project_root())+'/source/data_Set/data/'

class Camera:
    def __init__(self):
        print("Init camera")

        self.resolution = (2592, 1944)
        self.rotation = 180
        self.filesCount = self.capture(test_dir)
        self.annotate_text_size = 160
        self.annotate_background = 'red'
        self.hflip = True
    class preview():
        def __init__(self):
            self.fullscreen = False
            self.window = (0,0, 1028 /2, 640 /2)
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

        print("count = ", count)
        return count


    def sleep(self, sec):
        time.sleep(sec)