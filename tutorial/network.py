import matplotlib.pyplot as plt
import numpy as np
import os
import tensorflow as tf

_URL = 'https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip'
path_to_zip = tf.keras.utils.get_file('cats_and_dogs.zip', origin=_URL, extract=True)
PATH = os.path.join(os.path.dirname(path_to_zip), 'cats_and_dogs_filtered')

train_dir = os.path.join(PATH, 'train')
validation_dir = os.path.join(PATH, 'validation')

BATCH_SIZE = 32
IMG_SIZE = (160, 160)


class Network:
    val_loss = None
    val_acc = None
    prediction_batch = None
    feature_batch_average = None
    base_model = None
    feature_batch = None
    rescale = None
    preprocess_input = None
    train_dataset = None
    test_dataset = None
    autotune = None
    data_augmentation = None
    validation_dataset = None
    history = None
    accuracy0 = None
    loss0 = None

    def __init__(self):
        self.val_loss = None
        self.val_acc = None
        self.history = None
        self.accuracy0 = None
        self.loss0 = None
        self.prediction_batch = None
        self.feature_batch_average = None
        self.base_model = None
        self.feature_batch = None
        self.rescale = None
        self.preprocess_input = None
        self.train_dataset = None
        self.test_dataset = None
        self.autotune = None
        self.data_augmentation = None
        self.validation_dataset = None

    def data_preprocessing(self):
        self.train_dataset = tf.keras.utils.image_dataset_from_directory(train_dir,
                                                                         shuffle=True,
                                                                         batch_size=BATCH_SIZE,
                                                                         image_size=IMG_SIZE)

        self.validation_dataset = tf.keras.utils.image_dataset_from_directory(validation_dir,
                                                                              shuffle=True,
                                                                              batch_size=BATCH_SIZE,
                                                                              image_size=IMG_SIZE)

        class_names = self.train_dataset.class_names

        plt.figure(figsize=(10, 10))
        for images, labels in self.train_dataset.take(1):
            for i in range(9):
                ax = plt.subplot(3, 3, i + 1)
                plt.imshow(images[i].numpy().astype("uint8"))
                plt.title(class_names[labels[i]])
                plt.axis("off")

        val_batches = tf.data.experimental.cardinality(self.validation_dataset)
        self.test_dataset = self.validation_dataset.take(val_batches // 5)
        self.validation_dataset.skip(val_batches // 5)

        # print('Number of validation batches: %d' % tf.data.experimental.cardinality(self.validation_dataset))
        # print('Number of test batches: %d' % tf.data.experimental.cardinality(self.test_dataset))

    def configure_for_performance(self):
        self.autotune = tf.data.AUTOTUNE

        self.train_dataset = self.train_dataset.prefetch(buffer_size=self.autotune)
        self.validation_dataset = self.validation_dataset.prefetch(buffer_size=self.autotune)
        self.test_dataset = self.test_dataset.prefetch(buffer_size=self.autotune)

        self.data_augmentation = tf.keras.Sequential([
            tf.keras.layers.RandomFlip('horizontal'),
            tf.keras.layers.RandomRotation(0.2),
        ])

        for image, _ in self.train_dataset.take(1):
            plt.figure(figsize=(10, 10))
            first_image = image[0]
            for i in range(9):
                ax = plt.subplot(3, 3, i + 1)
                augmented_image = self.data_augmentation(tf.expand_dims(first_image, 0))
                plt.imshow(augmented_image[0] / 255)
                plt.axis('off')

        self.preprocess_input = tf.keras.applications.mobilenet_v2.preprocess_input
        self.rescale = tf.keras.layers.Rescaling(1. / 127.5, offset=-1)

    def create_base_model(self):
        IMG_SHAPE = IMG_SIZE + (3,)
        self.base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE,
                                                            include_top=False,
                                                            weights='imagenet')
        image_batch, label_batch = next(iter(self.train_dataset))
        self.feature_batch = self.base_model(image_batch)
        # print(self.feature_batch.shape)

    def feature_extraction(self):
        self.base_model.trainable = False
        self.base_model.summary()
        global_average_layer = tf.keras.layers.GlobalAveragePooling2D()
        self.feature_batch_average = global_average_layer(self.feature_batch)
        #
        print(self.feature_batch_average.shape)

        prediction_layer = tf.keras.layers.Dense(1)
        self.prediction_batch = prediction_layer(self.feature_batch_average)
        # print(self.prediction_batch.shape)

        inputs = tf.keras.Input(shape=(160, 160, 3))
        x = self.data_augmentation(inputs)
        x = self.preprocess_input(x)
        x = self.base_model(x, training=False)
        x = global_average_layer(x)
        x = tf.keras.layers.Dropout(0.2)(x)
        outputs = prediction_layer(x)
        model = tf.keras.Model(inputs, outputs)

        base_learning_rate = 0.0001
        model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=base_learning_rate),
                      loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                      metrics=['accuracy'])
        model.summary()
        # len(model.trainable_variables)

        initial_epochs = 10
        self.loss0, self.accuracy0 = model.evaluate(self.validation_dataset)
        # print("initial loss: {:.2f}".format(self.loss0))
        # print("initial accuracy: {:.2f}".format(self.accuracy0))
        self.history = model.fit(self.train_dataset,
                                 epochs=initial_epochs,
                                 validation_data=self.validation_dataset)

    def get_results(self):
        self.val_acc = self.history.history['val_accuracy']
        print(self.val_acc)
        self.val_loss = self.history.history['val_loss']
        print(self.val_loss)
