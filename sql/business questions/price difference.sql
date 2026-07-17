SELECT
    coin_name,
    snapshot_time,
    current_price,

    LAG(current_price) OVER(
        PARTITION BY coin_name
        ORDER BY snapshot_time
    ) AS previous_price,

    current_price -
    LAG(current_price) OVER(
        PARTITION BY coin_name
        ORDER BY snapshot_time
    ) AS price_difference

FROM crypto.vw_coin_history;