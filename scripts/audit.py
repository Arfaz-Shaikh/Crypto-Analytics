from sqlalchemy import text
from config.database import engine


def insert_audit(
    pipeline_name,
    run_start,
    run_end,
    records_extracted,
    records_dimension,
    records_fact,
    status,
    error_message,
    duration,
):

    query = text("""
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
            :records_dimension,
            :records_fact,
            :status,
            :error_message,
            :duration
        )
    """)

    with engine.begin() as conn:
        conn.execute(
            query,
            {
                "pipeline_name": pipeline_name,
                "run_start": run_start,
                "run_end": run_end,
                "records_extracted": records_extracted,
                "records_dimension": records_dimension,
                "records_fact": records_fact,
                "status": status,
                "error_message": error_message,
                "duration": duration,
            },
        )