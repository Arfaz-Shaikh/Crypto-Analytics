import json
from datetime import datetime

from config.mongodb import collection

def load_json_to_mongodb():

    with open("data/raw/json/crypto_raw.json", "r") as file:

        data = json.load(file)

    document = {
        "snapshot_time": datetime.now(),
        "api_source": "CoinGecko",
        "coins": data
    }

    result = collection.insert_one(document)

    print(f"Inserted document ID: {result.inserted_id}")


if __name__ == "__main__":
    load_json_to_mongodb()