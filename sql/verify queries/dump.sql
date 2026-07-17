TRUNCATE TABLE
    crypto.fact_market_snapshot,
    crypto.dim_coin,
    crypto.etl_audit
RESTART IDENTITY CASCADE;