SELECT
    coin_name,
    current_price
FROM crypto.coin_prices
ORDER BY current_price DESC
LIMIT 10;