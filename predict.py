#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Marco Fossati'
__email__ = 'mfossati@wikimedia.org'

from numpy import argmax, ndarray
from tensorflow.keras import models
from tensorflow.keras.models import Model


def load_model(path: str) -> Model:
    return models.load_model(path)


def predict(model: Model, sample: ndarray) -> dict:
    """Classify one pre-processed image sample as NSFW or not."""
    # Prediction at index 0 is NSFW
    index_labels = {0: 'NSFW', 1: 'suitable'}

    prediction = model.predict(sample)
    winner_index = argmax(prediction)

    label = index_labels.get(winner_index)
    if label is None:  # This shouldn't happen
        raise ValueError(
            f'Unexpected prediction shape: {prediction.shape}. Should be (1, 2)'
        )

    return {'prediction': label, 'confidence': prediction[0, winner_index]}
