import pandas as pd

def read_expenses(file_path: str):
    df = pd.read_csv(file_path)
    return df.to_dict(orient="records")
