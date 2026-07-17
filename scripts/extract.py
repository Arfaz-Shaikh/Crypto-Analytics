import json
import requests
import pandas as pd
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.config import API_URL, PARAMS, RAW_DATA_PATH, RAW_DATA_PATH1

def get_crypto_data():
    """Fetch cryptocurrency data from CoinGecko API."""
    response = requests.get(API_URL, params=PARAMS)
    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code}")
    return response.json()


def save_json(data):
    """Save raw API response."""
    with open(f"{RAW_DATA_PATH}crypto_raw.json", "w") as file:
        json.dump(data, file, indent=4)


def save_csv(data):
    """Save cleaned data as CSV."""
    df = pd.DataFrame(data)
    df.to_csv(
        f"{RAW_DATA_PATH1}crypto_raw.csv",
        index=False
    )

def main():
    crypto_data = get_crypto_data()
    save_json(crypto_data)
    save_csv(crypto_data)
    print("ETL Extract Completed Successfully")

def main():
    df = get_crypto_data()
    save_csv(df)
    save_json(df)
    print(f"Extracted {len(df)} records")
    return len(df)

if __name__ == "__main__":
    main()