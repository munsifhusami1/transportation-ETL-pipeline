import pandas as pd

"""Extract fetches grant application data from source CSV"""

def extract(filepath):
    df = pd.read_csv(filepath, encoding='latin-1')
    return df
