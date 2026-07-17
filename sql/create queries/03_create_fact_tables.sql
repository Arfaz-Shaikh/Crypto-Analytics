DROP TABLE IF EXISTS crypto.fact_market_snapshot CASCADE;
CREATE TABLE crypto.fact_market_snapshot
(
    snapshot_time TIMESTAMP NOT NULL,
    coin_id VARCHAR(100) NOT NULL,
    current_price NUMERIC,
    market_cap NUMERIC,
    market_cap_rank INTEGER,
    total_volume NUMERIC,
    high_24h NUMERIC,
    low_24h NUMERIC,
    price_change_24h NUMERIC,
    price_change_percentage_24h NUMERIC,
    PRIMARY KEY (snapshot_time, coin_id),
    CONSTRAINT fk_coin
        FOREIGN KEY (coin_id)
        REFERENCES crypto.dim_coin(coin_id)
);