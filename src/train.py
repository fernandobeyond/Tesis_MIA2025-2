"""train.py (esqueleto)
Ejecución: cargar processed CSV -> split -> balance train -> preproc -> train XGB y CNN-LSTM -> blend
"""
import argparse, joblib, os
import pandas as pd
from src.dataset import train_val_test_split, balance_train_under
from src.models import make_xgb, make_cnn_lstm

def main(in_path, out_dir):
    df = pd.read_csv(in_path)
    target = 'Attack_Label'
    X = df.drop(columns=[target])
    y = df[target]
    X_train, X_val, X_test, y_train, y_val, y_test = train_val_test_split(X, y)
    Xb, yb = balance_train_under(X_train, y_train)
    # ... aquí iría el preprocesamiento y entrenamiento
    os.makedirs(out_dir, exist_ok=True)
    joblib.dump({'note':'placeholder'}, os.path.join(out_dir, 'model_xgb.joblib'))

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--in', dest='in_path', required=True)
    p.add_argument('--out', dest='out_dir', required=True)
    args = p.parse_args()
    main(args.in_path, args.out_dir)
