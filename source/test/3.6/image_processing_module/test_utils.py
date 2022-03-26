from source.utils import get_project_root


def test_utils():
    assert str(get_project_root()).endswith('RoboticArm') == True
