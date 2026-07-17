CREATE OR REPLACE VIEW crypto.vw_top_market_cap AS
SELECT *
FROM crypto.vw_latest_market_snapshot
ORDER BY market_cap DESC;