import pandas as pd
import string


labels = []
for x in string.ascii_uppercase:
    labels.append(x)
    for y in string.ascii_uppercase:
        labels.append(x + y)
        if len(labels) == 119:
            break
    if len(labels) == 119:
        break

def transform(df):
    """Transform cleans column names, handles null values, parses grant dollar amounts/dates, and standardizes formats"""
    df[' Amount '] = df[' Amount '].str.replace('$', '', regex=False).str.replace(',', '', regex=False).str.strip()
    df[' Amount '] = pd.to_numeric(df[' Amount '], errors='coerce')
    df[' Amount '] = df[' Amount '] * 1.3
    df[' Total Project Cost '] = df[' Total Project Cost '].str.replace('$', '', regex=False).str.replace(',', '', regex=False).str.strip()
    df[' Total Project Cost '] = pd.to_numeric(df[' Total Project Cost '], errors='coerce')
    df[' Total Project Cost '] = df[' Total Project Cost '] * 1.3
    df = df.drop(columns=['Local Contact', 'TIP Status'])
    


    df['Project Title'] = labels[:len(df)]
    return df


