SELECT
    coin_name,
    SUM(total_volume) AS total_volume
FROM crypto.coin_prices
GROUP BY coin_name
ORDER BY total_volume DESC;