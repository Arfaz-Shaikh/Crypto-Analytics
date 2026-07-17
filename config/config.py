API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 50,
    "page": 1,
    "sparkline": False
}
RAW_DATA_PATH = "data/raw/json/"
RAW_DATA_PATH1 = "data/raw/csv/"
PROCESSED_DATA_PATH = "data/processed/"
LOG_PATH = "logs/"