"""dataset.py
Splits y balanceo (solo train)
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.under_sampling import RandomUnderSampler

def train_val_test_split(X, y, test_size=0.15, val_ratio=0.1765, seed=42):
    X_train_full, X_test, y_train_full, y_test = train_test_split(X, y, test_size=test_size, stratify=y, random_state=seed)
    X_train, X_val, y_train, y_val = train_test_split(X_train_full, y_train_full, test_size=val_ratio, stratify=y_train_full, random_state=seed)
    return X_train, X_val, X_test, y_train, y_val, y_test

def balance_train_under(X_train, y_train, seed=42):
    rus = RandomUnderSampler(random_state=seed)
    Xb, yb = rus.fit_resample(X_train, y_train)
    return Xb, yb
