SELECT *
FROM crypto.vw_coin_history
ORDER BY snapshot_time DESC
LIMIT 20;