SELECT
    coin_name,
    current_price,
    LAG(current_price)
    OVER(ORDER BY current_price DESC) AS previous_price
FROM crypto.coin_prices;