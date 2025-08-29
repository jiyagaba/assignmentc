import pandas as pd

def ingest_data(filepath="data/data.csv"):
    df = pd.read_csv(filepath)
    # cleaning / preprocessing
    return df
