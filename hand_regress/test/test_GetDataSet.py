import pytest

from hand_regress.regress import GetDataSet


def test_DATASET():
    ds = GetDataSet()
    ds.get_data_set()
    assert (len(ds.train_coordi_dict) == 806) and (len(ds.test_coordi_dict) == 35)