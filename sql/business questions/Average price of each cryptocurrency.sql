SELECT
    coin_name,
    ROUND(AVG(current_price),2) AS average_price
FROM crypto.coin_prices
GROUP BY coin_name
ORDER BY average_price DESC;