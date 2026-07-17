SELECT
    coin_name,
    current_price,
    LEAD(current_price)
    OVER(ORDER BY current_price DESC) AS next_price
FROM crypto.coin_prices;