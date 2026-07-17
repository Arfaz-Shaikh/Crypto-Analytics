CREATE OR REPLACE VIEW crypto.vw_coin_history AS

SELECT
    f.snapshot_time,
    d.coin_name,
    d.symbol,
    f.current_price,
    f.market_cap,
    f.total_volume,
    f.price_change_percentage_24h
FROM crypto.fact_market_snapshot f
JOIN crypto.dim_coin d
ON f.coin_id = d.coin_id;