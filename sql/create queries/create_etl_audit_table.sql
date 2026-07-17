CREATE TABLE crypto.etl_audit (
    audit_id BIGSERIAL PRIMARY KEY,
    pipeline_name VARCHAR(100),
    run_start TIMESTAMP,
    run_end TIMESTAMP,
    records_extracted INTEGER,
    records_loaded_dimension INTEGER,
    records_loaded_fact INTEGER,
    status VARCHAR(20),
    error_message TEXT,
    duration_seconds NUMERIC(10,2)
);