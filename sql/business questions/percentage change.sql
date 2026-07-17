SELECT
    coin_name,
    snapshot_time,
    current_price,

    ROUND(
        (
            current_price -
            LAG(current_price) OVER(
                PARTITION BY coin_name
                ORDER BY snapshot_time
            )
        )
        /
        LAG(current_price) OVER(
            PARTITION BY coin_name
            ORDER BY snapshot_time)
        * 100,
        2
    ) AS percentage_change

FROM crypto.vw_coin_history;