import matplotlib.pyplot as plt
import numpy as np
import os
import math
import tensorflow as tf
import pytest

from fine_tuning_module.tutor import _URL, path_to_zip, PATH, train_dir, validation_dir, Network

nn = Network
Network.data_preprocessing(nn)
Network.configure_for_performance(nn)
Network.create_base_model(nn)
Network.feature_extraction(nn)
Network.get_results(nn)
Network.FT_unfreeze_top_layers(nn)
Network.FT_compile(nn)
Network.FT_train(nn)


def test_FT_unfreeze():
    assert len(nn.base_model.layers) == 154


def test_FT_train():
    assert nn.accuracy_fine > 0.95


def test_FT_predictions():
    # Retrieve a batch of images from the test set
    image_batch, label_batch = nn.test_dataset.as_numpy_iterator().next()
    predictions = nn.model.predict_on_batch(image_batch).flatten()
    # Apply a sigmoid since our model returns logits
    predictions = tf.nn.sigmoid(predictions)
    predictions = tf.where(predictions < 0.5, 0, 1)
    print (predictions.numpy())
    print (label_batch)
    assert str(predictions.numpy()) == str(label_batch)
