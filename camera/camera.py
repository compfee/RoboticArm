from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (2592, 1944)
camera.rotation=180
camera.start_preview()
for i in range(1000, 1050):
    sleep(2)
    camera.capture('/home/pi/Downloads/RoboArm/data_Set/with_coordinates/train/hand6/frame%04d.jpg' % i)
camera.stop_preview()