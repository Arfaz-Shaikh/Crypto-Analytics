WITH avg_price AS
(
    SELECT AVG(current_price) AS average_price
    FROM crypto.coin_prices
)

SELECT
    cp.coin_name,
    cp.current_price
FROM crypto.coin_prices cp
CROSS JOIN avg_price
WHERE cp.current_price > avg_price.average_price
ORDER BY cp.current_price DESC;