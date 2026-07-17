SELECT
    coin_name,
    market_cap
FROM crypto.coin_prices
WHERE market_cap > 10000000000;