DROP TABLE IF EXISTS crypto.dim_coin CASCADE;
CREATE TABLE crypto.dim_coin
(
    coin_id VARCHAR(100) PRIMARY KEY,
    symbol VARCHAR(20) NOT NULL,
    coin_name VARCHAR(100) NOT NULL,
    image_url TEXT
);