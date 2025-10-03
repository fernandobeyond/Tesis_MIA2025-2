"""models.py
Definiciones de CNN-LSTM (Keras) y wrapper simple para XGBoost
"""
import xgboost as xgb
import tensorflow as tf
from tensorflow.keras import layers, models

def make_cnn_lstm(input_shape):
    inp = layers.Input(shape=input_shape)
    x = layers.Conv1D(64, 3, padding='same', activation='relu')(inp)
    x = layers.MaxPooling1D(2)(x)
    x = layers.Conv1D(128, 3, padding='same', activation='relu')(x)
    x = layers.Dropout(0.3)(x)
    x = layers.LSTM(128)(x)
    x = layers.Dropout(0.3)(x)
    emb = layers.Dense(64, activation='relu')(x)
    out = layers.Dense(1, activation='sigmoid')(emb)
    model = models.Model(inputs=inp, outputs=out)
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['AUC'])
    return model

def make_xgb(params=None):
    params = params or {}
    return xgb.XGBClassifier(**params)
