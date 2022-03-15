import os
import pytest
import numpy
import time
from PIL import Image
import shutil
from random import randrange

from source.image_processing_module.compress_images_module.compress import compress_images
from source.utils import get_project_root


def clean_folder(directory=str(get_project_root()) + '/source/image_processing_module/compress_images_module/pics'):
    folder = directory
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


@pytest.fixture()
def create_image(width=600, height=600, num_of_images=randrange(30)):
    width = int(width)
    height = int(height)
    num_of_images = int(num_of_images)
    current = time.strftime("%Y%m%d%H%M%S")
    for n in range(num_of_images):
        filename = '{0}_{0}_{1:03d}.jpg'.format(current, n)
        rgb_array = numpy.random.rand(height, width, 3) * 255
        image = Image.fromarray(rgb_array.astype('uint8')).convert('RGB')
        image.save(str(get_project_root()) + '/source/image_processing_module/compress_images_module/pics/' + filename)


def test_compress_images_NO_FILES():
    with pytest.raises(Exception):
        originals_path = str(get_project_root()) + '/source/image_processing_module/test/compress_images_module'
        compress_images(directory=originals_path)


def test_compress_images_COMPRESSING(create_image):
    orig_sum = 0
    comp_sum = 0
    originals_path = str(get_project_root()) + '/source/image_processing_module/compress_images_module/pics'
    compressed_path = str(get_project_root()) + '/source/image_processing_module/compress_images_module/compressed'

    compress_images(directory=originals_path)

    for path, dirs, files in os.walk(originals_path):
        for f in files:
            fp = os.path.join(path, f)
            orig_sum += os.path.getsize(fp)

    for path, dirs, files in os.walk(compressed_path):
        for f in files:
            fp = os.path.join(path, f)
            comp_sum += os.path.getsize(fp)
    clean_folder(originals_path)
    clean_folder(compressed_path)
    assert comp_sum < orig_sum


def test_compress_images_ENDING(create_image):
    bool = True
    originals_path = str(get_project_root()) + '/source/image_processing_module/compress_images_module/pics'
    compressed_path = str(get_project_root()) + '/source/image_processing_module/compress_images_module/compressed'

    compress_images(directory=originals_path)

    files = os.listdir(compressed_path)
    for file in files:
        bool &= file.endswith('.jpg')

    clean_folder(originals_path)
    clean_folder(compressed_path)
    assert bool == True
