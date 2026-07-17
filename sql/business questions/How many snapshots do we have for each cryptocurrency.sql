SELECT
    coin_name,
    COUNT(*) AS snapshots
FROM crypto.coin_prices
GROUP BY coin_name
ORDER BY snapshots DESC;