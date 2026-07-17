SELECT
    coin_name,
    ROUND(AVG(market_cap),2) AS average_market_cap
FROM crypto.coin_prices
GROUP BY coin_name
ORDER BY average_market_cap DESC
LIMIT 10;