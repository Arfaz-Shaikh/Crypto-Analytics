SELECT
    coin_name,
    MAX(current_price) AS highest_price
FROM crypto.coin_prices
GROUP BY coin_name
ORDER BY highest_price DESC;