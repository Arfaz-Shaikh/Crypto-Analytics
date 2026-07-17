SELECT
    coin_name,
    current_price,
    RANK() OVER(ORDER BY current_price DESC) AS rank_number
FROM crypto.coin_prices;