SELECT
    coin_name,
    current_price,
    DENSE_RANK() OVER(ORDER BY current_price DESC) AS dense_rank
FROM crypto.coin_prices;