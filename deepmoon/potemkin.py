#!/usr/bin/env python

from keras.layers import (BatchNormalization, Conv1D, Dense, Dropout,
                          Flatten, Input, Lambda)
from keras.models import Model
import numpy as np
from keras import backend as K


NUM_CATEGORIES = 6


def create_model():
    inputs = x = Input(shape=(100,))
    x = Lambda(lambda x: K.expand_dims(x))(x)
    for r in range(0, 3):
        x = Conv1D(10, 5, activation='relu')(x)
        x = BatchNormalization()(x)
    x = Conv1D(1, 5, activation='relu')(x)
    x = Flatten()(x)
    x = Dense(10, activation='relu')(x)
    x = Dropout(0.5)(x)
    x = Dense(NUM_CATEGORIES, activation='softmax')(x)
    return Model(inputs=inputs, outputs=x)


def show_training_run(sweat):
    sweat = max(0, sweat + 1)
    model = create_model()
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    k = 15000

    mode = np.random.randint(1, NUM_CATEGORIES, size=(k,))
    x = np.arange(0, 100)
    x = np.tile(x, (k, 1))
    for m in range(1, NUM_CATEGORIES):
        x[mode == m, :] = x[mode == m, :] % m
    x = (x.astype(np.float) / sweat) + (sweat - 1)
    x = x * np.random.uniform(0.0, 1.0, size=x.shape)
    y = np.zeros((k, NUM_CATEGORIES))
    y[np.arange(len(y)), mode - 1] = 1
    model.fit(x, y, epochs=100, batch_size=20, validation_split=0.25)


if __name__ == '__main__':
    show_training_run(sweat=3)
