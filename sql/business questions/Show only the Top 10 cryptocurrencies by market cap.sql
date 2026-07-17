SELECT
    coin_name,
    market_cap
FROM crypto.coin_prices
where market_cap > 1000
ORDER BY market_cap DESC
LIMIT 10;