WITH ranked_coins AS
(
    SELECT
        coin_name,
        market_cap
    FROM crypto.vw_latest_market_snapshot
)

SELECT *
FROM ranked_coins
ORDER BY market_cap DESC
LIMIT 10;