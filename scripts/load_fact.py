import pandas as pd
from datetime import datetime
from config.database import engine

def load_fact():
    # Read CSV
    df = pd.read_csv("data/raw/csv/crypto_raw.csv")

    # Add snapshot timestamp
    df["snapshot_time"] = datetime.now()

    # Select fact columns
    fact_df = df[
        [
            "snapshot_time",
            "id",
            "current_price",
            "market_cap",
            "market_cap_rank",
            "total_volume",
            "high_24h",
            "low_24h",
            "price_change_24h",
            "price_change_percentage_24h",
        ]
    ]

    # Rename column
    fact_df.rename(
        columns={
            "id": "coin_id"
        },
        inplace=True
    )

    # Load into PostgreSQL
    fact_df.to_sql(
        "fact_market_snapshot",
        engine,
        schema="crypto",
        if_exists="append",
        index=False
    )

    print(f"Loaded {len(fact_df)} records")
    return len(fact_df)
if __name__ == "__main__":
    load_fact()