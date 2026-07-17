WITH average_market_cap AS
(
    SELECT AVG(market_cap) AS avg_market_cap
    FROM crypto.vw_latest_market_snapshot
)

SELECT
    coin_name,
    market_cap
FROM crypto.vw_latest_market_snapshot
WHERE market_cap >
(
    SELECT avg_market_cap
    FROM average_market_cap
)
ORDER BY market_cap DESC;