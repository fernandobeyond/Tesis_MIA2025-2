"""preprocess.py
Lectura -> target binario -> guardado processed
"""
import pandas as pd

def load_csv(path):
    return pd.read_csv(path, low_memory=False)

def make_binary_target(df, target_col='Attack_Label'):
    df = df.copy()
    df[target_col] = (df[target_col].astype(str).str.upper() != 'BENIGN').astype(int)
    return df

def save_processed(df, out_path):
    df.to_csv(out_path, index=False)

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--in', dest='in_path', required=True)
    p.add_argument('--out', dest='out_path', required=True)
    args = p.parse_args()
    df = load_csv(args.in_path)
    df = make_binary_target(df, 'Attack_Label')
    save_processed(df, args.out_path)
