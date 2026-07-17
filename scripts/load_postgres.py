import pandas as pd
from datetime import datetime
from sqlalchemy import text

from config.database import engine


def load_data():
    """Load crypto data into PostgreSQL Star Schema."""

    run_start = datetime.now()

    print("=" * 60)
    print("🚀 Starting PostgreSQL ETL...")
    print("=" * 60)

    try:
        # -----------------------------
        # Read CSV
        # -----------------------------
        df = pd.read_csv("data/raw/csv/crypto_raw.csv")

        print(f"✅ CSV Loaded Successfully ({len(df)} records)")

        df["snapshot_time"] = run_start

        df = df[
            [
                "snapshot_time",
                "id",
                "symbol",
                "name",
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

        df.rename(
            columns={
                "id": "coin_id",
                "name": "coin_name",
            },
            inplace=True,
        )

        dim_count = 0
        fact_count = 0

        with engine.begin() as conn:

            # ============================================
            # LOAD DIMENSION TABLE
            # ============================================

            print("📦 Loading dim_coin...")

            for _, row in df.iterrows():

                exists = conn.execute(
                    text("""
                        SELECT 1
                        FROM crypto.dim_coin
                        WHERE coin_id = :coin_id
                    """),
                    {"coin_id": row.coin_id},
                ).fetchone()

                if exists is None:

                    conn.execute(
                        text("""
                            INSERT INTO crypto.dim_coin
                            (
                                coin_id,
                                symbol,
                                coin_name
                            )
                            VALUES
                            (
                                :coin_id,
                                :symbol,
                                :coin_name
                            )
                        """),
                        {
                            "coin_id": row.coin_id,
                            "symbol": row.symbol,
                            "coin_name": row.coin_name,
                        },
                    )

                    dim_count += 1

            print(f"✅ Dimension Loaded ({dim_count} new coins)")

            # ============================================
            # LOAD FACT TABLE
            # ============================================

            print("📊 Loading fact_market_snapshot...")

            for _, row in df.iterrows():

                conn.execute(
                    text("""
                        INSERT INTO crypto.fact_market_snapshot
                        (
                            snapshot_time,
                            coin_id,
                            current_price,
                            market_cap,
                            market_cap_rank,
                            total_volume,
                            high_24h,
                            low_24h,
                            price_change_24h,
                            price_change_percentage_24h
                        )

                        VALUES
                        (
                            :snapshot_time,
                            :coin_id,
                            :current_price,
                            :market_cap,
                            :market_cap_rank,
                            :total_volume,
                            :high_24h,
                            :low_24h,
                            :price_change_24h,
                            :price_change_percentage_24h
                        )
                    """),
                    row.to_dict(),
                )

                fact_count += 1

            print(f"✅ Fact Loaded ({fact_count} rows)")

            # ============================================
            # LOAD AUDIT TABLE
            # ============================================

            run_end = datetime.now()
            duration = (run_end - run_start).total_seconds()

            print("📝 Writing ETL Audit...")

            conn.execute(
                text("""
                    INSERT INTO crypto.etl_audit
                    (
                        pipeline_name,
                        run_start,
                        run_end,
                        records_extracted,
                        records_loaded_dimension,
                        records_loaded_fact,
                        status,
                        error_message,
                        duration_seconds
                    )

                    VALUES
                    (
                        :pipeline_name,
                        :run_start,
                        :run_end,
                        :records_extracted,
                        :records_loaded_dimension,
                        :records_loaded_fact,
                        :status,
                        :error_message,
                        :duration_seconds
                    )
                """),
                {
                    "pipeline_name": "CoinGecko ETL",
                    "run_start": run_start,
                    "run_end": run_end,
                    "records_extracted": len(df),
                    "records_loaded_dimension": dim_count,
                    "records_loaded_fact": fact_count,
                    "status": "SUCCESS",
                    "error_message": None,
                    "duration_seconds": duration,
                },
            )

            print("✅ Audit Record Inserted")

        print("=" * 60)
        print("🎉 PostgreSQL ETL Completed Successfully")
        print("=" * 60)

    except Exception as e:
        print("=" * 60)
        print("❌ ETL FAILED")
        print("=" * 60)
        print(type(e).__name__)
        print(e)
        raise


def main():
    load_data()


if __name__ == "__main__":
    main()