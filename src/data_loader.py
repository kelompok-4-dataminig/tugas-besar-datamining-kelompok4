import pandas as pd
import os

def load_clean_data(filepath=None):
    if filepath is None:
        # otomatis ambil path relatif dari root proyek
        filepath = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed', 'done.csv')
    
    df = pd.read_csv(filepath)

    # Drop baris dengan teks kosong atau sentimen kosong
    df = df.dropna(subset=['preprocessed_text', 'sentimen'])

    # Filter teks yang panjangnya sangat pendek (opsional)
    df = df[df['preprocessed_text'].str.len() > 5]

    return df
