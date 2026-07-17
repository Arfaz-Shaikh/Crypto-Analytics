import pandas as pd
from sqlalchemy import text
from config.database import engine


def load_dimension():

    df = pd.read_csv("data/raw/csv/crypto_raw.csv")

    dim_df = (
        df[
            [
                "id",
                "symbol",
                "name",
                "image"
            ]
        ]
        .drop_duplicates()
        .rename(
            columns={
                "id": "coin_id",
                "name": "coin_name",
                "image": "image_url"
            }
        )
    )

    with engine.begin() as conn:

        for _, row in dim_df.iterrows():

            conn.execute(
                text("""
                    INSERT INTO crypto.dim_coin
                    (coin_id, symbol, coin_name, image_url)

                    VALUES
                    (:coin_id,:symbol,:coin_name,:image_url)

                    ON CONFLICT (coin_id)
                    DO UPDATE SET
                        symbol = EXCLUDED.symbol,
                        coin_name = EXCLUDED.coin_name,
                        image_url = EXCLUDED.image_url;
                """),
                {
                    "coin_id": row.coin_id,
                    "symbol": row.symbol,
                    "coin_name": row.coin_name,
                    "image_url": row.image_url,
                },
            )

    print(f"✅ Dimension Loaded : {len(dim_df)} records")

    return len(dim_df)


if __name__ == "__main__":
    load_dimension()