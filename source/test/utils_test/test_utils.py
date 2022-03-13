from utils import get_project_root
import pytest


def test_utils():
    assert str(get_project_root()).endswith('RoboticArm') == True
