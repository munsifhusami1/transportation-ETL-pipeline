import sqlite3

def load(df):
    """Load adds cleaned DataFrame into the target database grants.db"""
    conn = sqlite3.connect('grants.db')
    df.to_sql('grants', conn, if_exists='replace')
