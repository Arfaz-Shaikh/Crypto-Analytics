SELECT
    coin_name,
    current_price,
    CASE
        WHEN current_price > 50000 THEN 'Very High'
        WHEN current_price > 1000 THEN 'High'
        WHEN current_price > 100 THEN 'Medium'
        ELSE 'Low'
    END AS price_category
FROM crypto.coin_prices
ORDER BY current_price DESC;