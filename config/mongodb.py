from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["crypto_analytics"]
collection = db["raw_market_data"]