CREATE OR REPLACE VIEW crypto.vw_top_gainers AS

SELECT
    coin_name,
    symbol,
    current_price,
    price_change_24h,
    price_change_percentage_24h,
    market_cap
FROM crypto.vw_latest_market_snapshot
ORDER BY price_change_percentage_24h DESC;