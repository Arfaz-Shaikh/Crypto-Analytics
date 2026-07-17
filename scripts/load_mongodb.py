from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")
db = client["crypto_db"]

collection = db["raw_market_data"]
with open("data/raw/json/crypto_raw.json", "r") as file:
    data = json.load(file)

collection.insert_many(data)
print("Data inserted successfully!")