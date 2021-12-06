import os
images_path = "/home/pi/Downloads/RoboArm/data_Set/with_no_coordinates/test/non_hand5"
image_list = os.listdir(images_path)
a=0
for i,  image in enumerate(image_list):
    ext = os.path.splitext(image)[1]
    if ext == '.jpg':
        
        src = images_path + '/' + image
        dst = images_path + '/' +"nh"+str(i) + '.jpg'
        os.rename(src, dst)
        print(i)