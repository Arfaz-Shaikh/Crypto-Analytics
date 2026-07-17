CREATE INDEX idx_coin_time

ON crypto.fact_market_snapshot
(
    coin_id,
    snapshot_time DESC
);