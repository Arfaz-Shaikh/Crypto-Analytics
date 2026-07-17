CREATE OR REPLACE VIEW crypto.vw_latest_market_snapshot AS

SELECT
    f.snapshot_time,
    d.coin_name,
    d.symbol,
    f.current_price,
    f.market_cap,
    f.market_cap_rank,
    f.total_volume,
    f.high_24h,
    f.low_24h,
    f.price_change_24h,
    f.price_change_percentage_24h

FROM crypto.fact_market_snapshot f

JOIN crypto.dim_coin d
ON f.coin_id = d.coin_id

WHERE f.snapshot_time = (
    SELECT MAX(snapshot_time)
    FROM crypto.fact_market_snapshot
);