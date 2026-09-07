import pandas as pd


def extract(filepath):
    """Extract fetches grant application data from source CSV"""
    df = pd.read_csv(filepath, encoding='latin-1')
    return df
