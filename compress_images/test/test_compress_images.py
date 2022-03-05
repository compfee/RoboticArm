import os
import pytest


from compress_images.compress import compress_images, get_project_root


def test_compress_images_COMPRESSING():
    orig_sum = 0
    comp_sum = 0
    originals_path = str(get_project_root()) + '\\compress_images\\pics'
    compressed_path = str(get_project_root()) + '\\compress_images\\compressed'

    compress_images(directory=originals_path)

    for path, dirs, files in os.walk(originals_path):
        for f in files:
            fp = os.path.join(path, f)
            orig_sum += os.path.getsize(fp)

    for path, dirs, files in os.walk(compressed_path):
        for f in files:
            fp = os.path.join(path, f)
            comp_sum += os.path.getsize(fp)

    assert comp_sum < orig_sum


def test_compress_images_ENDING():
    bool = True
    originals_path = str(get_project_root()) + '\\compress_images\\pics'
    compressed_path = str(get_project_root()) + '\\compress_images\\compressed'

    compress_images(directory=originals_path)

    files = os.listdir(compressed_path)
    for file in files:
        bool &= file.endswith('.jpg')

    assert bool == True

