CREATE TABLE crypto.coin_prices (
    snapshot_time TIMESTAMP NOT NULL,
    coin_id TEXT NOT NULL,
    symbol TEXT,
    coin_name TEXT,
    current_price NUMERIC,
    market_cap NUMERIC,
    market_cap_rank INTEGER,
    total_volume NUMERIC,
    high_24h NUMERIC,
    low_24h NUMERIC,
    price_change_24h NUMERIC,
    price_change_percentage_24h NUMERIC,
    PRIMARY KEY (snapshot_time, coin_id)
);