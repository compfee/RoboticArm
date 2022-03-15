import matplotlib.pyplot as plt
import numpy as np
import os
import math
import tensorflow as tf
import pytest

from source.image_processing_module.fine_tuning_module.tutor import _URL, path_to_zip, PATH, train_dir, validation_dir, Network

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

    count = 0
    list1 = list(predictions.numpy())
    list2 = list(label_batch)
    print()
    print(str(list1))
    print(str(list2))
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            count += 1
    assert count <= 2


def test_FT_predictions_neg():
    # Retrieve a batch of images from the test set
    image_batch, label_batch = nn.test_dataset.as_numpy_iterator().next()
    predictions = nn.model.predict_on_batch(image_batch).flatten()
    # Apply a sigmoid since our model returns logits
    predictions = tf.nn.sigmoid(predictions)
    predictions = tf.where(predictions < 0.5, 0, 1)

    count = 0
    list1 = list(predictions.numpy())
    list1.sort()
    list2 = list(label_batch)
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            count += 1
    assert count > 2

