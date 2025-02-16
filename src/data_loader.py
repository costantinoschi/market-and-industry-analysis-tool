import pandas as pd

def load_market_data(file_path):
    """
    Load market data from a CSV file.
    """
    return pd.read_csv(file_path)

def load_industry_data(file_path):
    """
    Load industry data from a CSV file.
    """
    return pd.read_csv(file_path)

def preprocess_data(market_data, industry_data):
    """
    Preprocess market and industry data.
    """
    # Example: Merge market and industry data on a common column
    merged_data = pd.merge(market_data, industry_data, on="sector")
    return merged_data