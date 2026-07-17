# Crypto-Analytics
│   .env
│   readme.md
│   runfile
│   
├───.vscode
│       launch.json
│       
├───config
│   │   config.py
│   │   database.py
│   │   logging_config.py
│   │   mongodb.py
│   │   __init__.py
│   │   
│   └───__pycache__
│           config.cpython-313.pyc
│           database.cpython-313.pyc
│           logging_config.cpython-313.pyc
│           mongodb.cpython-313.pyc
│           __init__.cpython-313.pyc
│           
├───dashboards
│       Crypto-Analytics.pbix
│       
├───data
│   ├───processed
│   └───raw
│       ├───csv
│       │       crypto_raw.csv
│       │       
│       └───json
│               crypto_raw.json
│               
├───images
│       ERD.png
│       
├───logs
│       pipeline.log
│       
├───mongodb
│   │   mongo_loader.py
│   │   
│   └───__pycache__
│           mongo_loader.cpython-313.pyc
│           
├───reports
│   └───excel
│           Crypto_Report_20260716_222959.xlsx
│           Crypto_Report_20260716_223131.xlsx
│           Crypto_Report_20260716_223214.xlsx
│           Crypto_Report_20260716_230514.xlsx
│           Crypto_Report_20260717_154050.xlsx
│           
├───scripts
│   │   audit.py
│   │   extract.py
│   │   load_dimension.py
│   │   load_fact.py
│   │   load_mongodb.py
│   │   load_postgres.py
│   │   report_excel.py
│   │   run_pipeline.py
│   │   transform.py
│   │   __init__.py
│   │   
│   └───__pycache__
│           audit.cpython-313.pyc
│           extract.cpython-313.pyc
│           load_dimension.cpython-313.pyc
│           load_fact.cpython-313.pyc
│           load_mongodb.cpython-313.pyc
│           load_postgres.cpython-313.pyc
│           report_excel.cpython-313.pyc
│           run_pipeline.cpython-313.pyc
│           transform.cpython-313.pyc
│           __init__.cpython-313.pyc
│           
├───sql
│   ├───Business Questions
│   │       Average price of each cryptocurrency.sql
│   │       Categorize cryptocurrencies based on their current price..sql
│   │       dense_rank.sql
│   │       Find all cryptocurrencies priced above the average price..sql
│   │       Highest recorded price for each cryptocurrency.sql
│   │       How many cryptocurrencies are in our latest snapshot.sql
│   │       How many snapshots do we have for each cryptocurrency.sql
│   │       How many unique cryptocurrencies are we tracking.sql
│   │       lag_query.sql
│   │       lead_query.sql
│   │       percentage change.sql
│   │       previous price.sql
│   │       price difference.sql
│   │       q1.sql
│   │       q2.sql
│   │       rank_query.sql
│   │       Row_query.sql
│   │       Show only the Top 10 cryptocurrencies by market cap.sql
│   │       Top 10 cryptocurrencies by average market cap.sql
│   │       Top 10 Most Expensive Coins.sql
│   │       Total trading volume for each cryptocurrency.sql
│   │       What is the average cryptocurrency price.sql
│   │       What is the highest cryptocurrency price.sql
│   │       What is the lowest cryptocurrency price.sql
│   │       What is the total market capitalization of all tracked cryptocurrencies.sql
│   │       Which are the most expensive cryptocurrencies.sql
│   │       Which cryptocurrencies have a market cap greater than 10 billion.sql
│   │       
│   ├───create
│   │       01_create_schema.sql
│   │       02_create_dimension_tables.sql
│   │       03_create_fact_tables.sql
│   │       create index snapsho time.sql
│   │       create index time.sql
│   │       create index.sql
│   │       createdtable.sql
│   │       create_dimension_table.sql
│   │       create_etl_audit_table.sql
│   │       create_fact_table.sql
│   │       
│   ├───verify
│   │       check loader.sql
│   │       checkdata.sql
│   │       dump.sql
│   │       verify index snapshot time.sql
│   │       verify index.sql
│   │       verify_coin_history.sql
│   │       verify_crypto_dim_data.sql
│   │       verify_etl_audit_table.sql
│   │       verify_fact_market_snapshot_data.sql
│   │       verify_latest_market_snapshot.sql
│   │       verify_market_view_summary.sql
│   │       verify_tables.sql
│   │       verify_top_gainers.sql
│   │       verify_top_losers.sql
│   │       verify_top_market_view.sql
│   │       
│   └───view
│           views_market_summary.sql
│           view_coin_history.sql
│           view_latest_market_snapshot.sql
│           view_top_gainers.sql
│           view_top_losers.sql
│           view_top_market_cap.sql
│           
└───venv
