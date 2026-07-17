SELECT
    coin_name,
    current_price,
    ROW_NUMBER() OVER(ORDER BY current_price DESC) AS row_num
FROM crypto.coin_prices;