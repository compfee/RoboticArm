import matplotlib.pyplot as plt
import numpy as np
import os
import math
import tensorflow as tf
import pytest

from image_processing_module.fine_tuning_module.tutor import _URL, path_to_zip, PATH, train_dir, validation_dir, Network

nn = Network
Network.data_preprocessing(nn)
Network.configure_for_performance(nn)
Network.create_base_model(nn)
Network.feature_extraction(nn)
Network.get_results(nn)


# сколько в проверочном наборе + переместили ли 20проц. в тестовый
def test_data_preprocessing_ValidationBatches():
    assert (tf.data.experimental.cardinality(nn.validation_dataset) == 32)


# переместили ли 20проц. в тестовый
def test_data_preprocessing_TestBatches():
    assert tf.data.experimental.cardinality(nn.test_dataset) == 6


# преобразование изображений 160х160х3 в 5х5х1280
def test_create_base_model():
    assert str(nn.feature_batch.shape) == "(32, 5, 5, 1280)"


# преобразование функций в один вектор из 1280 элементов для каждого изображения
def test_feature_ex1():
    assert str(nn.feature_batch_average.shape) == "(32, 1280)"


# после применения слоя Dense для преобразования функций в один прогноз
def test_feature_ex2():
    assert str(nn.prediction_batch.shape) == "(32, 1)"


# result for acc and loss в ожидаемых интервалах
def test_results():
    assert (nn.val_acc[-1] >= 0.90) and (nn.val_loss[-1] <= 0.15)


