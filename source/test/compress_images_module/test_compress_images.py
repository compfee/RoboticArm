import os
import pytest

from compress_images_module.compress import compress_images
from utils import get_project_root


def test_compress_images_NO_FILES():
    with pytest.raises(Exception):
        originals_path = str(get_project_root()) + '/source/test/compress_images_module'
        compress_images(directory=originals_path)


def test_compress_images_COMPRESSING():
    orig_sum = 0
    comp_sum = 0
    originals_path = str(get_project_root()) + '/source/compress_images_module/pics'
    compressed_path = str(get_project_root()) + '/source/compress_images_module/compressed'

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
    originals_path = str(get_project_root()) + '/source/compress_images_module/pics'
    compressed_path = str(get_project_root()) + '/source/compress_images_module/compressed'

    compress_images(directory=originals_path)

    files = os.listdir(compressed_path)
    for file in files:
        bool &= file.endswith('.jpg')

    assert bool == True
