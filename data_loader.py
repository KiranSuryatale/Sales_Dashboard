import pandas as pd

def load_data():
    try:
        data = pd.read_csv("sales_data.csv")
        return data
    except FileNotFoundError:
        print("Sales data file not found.")
        return None