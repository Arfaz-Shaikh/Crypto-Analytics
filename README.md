# 🚀 Crypto Market Intelligence Pipeline | End-to-End Data Engineering & Data Analytics Project

An end-to-end Data Enginerring and Data Analytics project that collects live cryptocurrency market data from CoinGecko API, processes it through a PostgreSQL data wareshouse, stores data in MongoDB, automate the ETL pipeline, and visualize insights using Power BI.

---
# 📌 Project Overview

This project was built to simulate a real-world enterprise data pipeline used by organizations to collect, process, store, and analyze financial market data.

The pipeline automatically extracts live cryptocurrency market information from the CoinGecko API, transforms the data, loads it into a PostgreSQL data warehouse and MongoDB, and provides interactive dashboards in Power BI for business intelligence and market analysis.

The project demonstrates skills in:

* Data Engineering
* ETL Pipeline Development
* Data Warehousing
* SQL Analytics
* Business Intelligence
* Python Automation
* Database Design

---
# 🎯 Project Objectives

* Build a production-style ETL pipeline
* Consume live REST API data
* Design a relational data warehouse
* Store NoSQL data in MongoDB
* Perform SQL analytics
* Build interactive Power BI dashboards
* Automate the complete workflow
* Follow software engineering best practices

---
# 🏗️ Project Architecture

                 CoinGecko API
                       │
                 Extract (Python)
                       │
                 Transform (Python)
                       │
        ┌──────────────┴──────────────┐
        │                             │
        ▼                             ▼
    PostgreSQL Data Warehouse       MongoDB
        │
        ▼
    SQL Views & Analytics
        │
        ▼
     Power BI Dashboard
        │
        ▼
    Windows Task Scheduler Automation

---
# 🛠️ Technologies Used

| Category              | Technology             |
| --------------------- | ---------------------- |
| Programming Language  | Python 3.13            |
| Database              | PostgreSQL             |
| NoSQL Database        | MongoDB                |
| Data Analysis         | Pandas                 |
| Database Connectivity | SQLAlchemy             |
| API                   | CoinGecko API          |
| Visualization         | Power BI               |
| SQL                   | PostgreSQL SQL         |
| Automation            | Windows Task Scheduler |
| IDE                   | Visual Studio Code     |
| Version Control       | Git & GitHub           |

---
# ⚙️ ETL Pipeline Workflow

### Step 1 — Extract
- Connected to the CoinGecko REST API.
- Retrieved the Top 50 cryptocurrencies.
- Stored raw JSON.
- Converted JSON to CSV.
### Output:
- Raw JSON
- Raw CSV

### Step 2 — Transform 
Cleaned the dataset by :
- Selecting required columns
- Renaming columns
- Adding snapshot timestamps
- Preparing data for warehouse loading

### Step 3 — Load
Loaded data into : PostgreSQL

Tables:
- coin_prices
- dim_coin
- fact_market_snapshot
- etl_audit

### MongoDB
Stored raw market snapshots for NoSQL analytics.

---
# 🗄️ Data Warehouse Design
### Dimension Table - dim_coin
Stores cryptocurrency master data.
### Columns include:
- coin_id
- coin_name
- symbol
- image_url
- Fact Table
- fact_market_snapshot

Stores historical market snapshots.

### Includes:
- Current Price
- Market Cap
- Volume
- High 24h
- Low 24h
- Price Change
- Snapshot Timestamp
- Audit Table
- etl_audit

### Tracks:
- Pipeline start time
- End time
- Duration
- Records extracted
- Records loaded
- Status
- Error messages

---
# 📊 SQL Business Questions Solved

### Market Analysis
- What is the average cryptocurrency price?
- What is the highest price?
- What is the lowest price?
- Total market capitalization
- Total trading volume
- Ranking
- Top 10 cryptocurrencies by market capitalization
- Top 10 most expensive coins
- Top trading volume coins
- Historical Analysis

### Using Window Functions:
- ROW_NUMBER()
- RANK()
- DENSE_RANK()
- LAG()
- LEAD()

### Calculated:
- Previous price
- Price difference
- Percentage change
- Historical rankings
- Snapshot Analysis
- Latest market snapshot
- Coin history
- Market trends
- Average market cap
- Price movements

---
# 📈 Power BI Dashboard
- Executive Dashboard
<p align="center">
<img width="1307" height="731" alt="Executive Dasboard" src="https://github.com/user-attachments/assets/ffb8b42e-9091-4379-8044-b50e1cd0a191" />
  
- Market Performance
<p align="center">
<img width="1307" height="735" alt="Market Performance" src="https://github.com/user-attachments/assets/1c9bbeb9-011c-41dd-bf36-bb17e7cd25ae" />
  
- Coin Analysis
<p align="center">
<img width="1306" height="733" alt="Coin Analysis" src="https://github.com/user-attachments/assets/bf3ff222-268f-4092-a5e8-04e16fbd2ffc" />

- ETL Pipeline Monitoring
<p align="center">
<img width="1307" height="732" alt="ETL Pipeline Monitoring" src="https://github.com/user-attachments/assets/e3b29b1b-7df4-4478-bf4b-b52bb641e436" />

---
# 🤖 Automation
### The project automates:
- API Extraction
- Data Transformation
- PostgreSQL Loading
- MongoDB Loading
- Excel Report Generation
- Pipeline Execution

### Automation Tool:
- Windows Task Scheduler

---
# 📑 Excel Reporting
Automatically generates Excel reports containing:
- Market Summary
- Coin Prices
- Market Capitalization
- Trading Volume

---
# 🔍 Challenges Faced & Solutions
### 1. Python Module Import Errors
Problem - ModuleNotFoundError: No module named 'config' 

Solution :
- Added __init__.py
- Used module execution :
```text
python -m scripts.run_pipeline
```
Configured VS Code workspace correctly.

### 2. Power BI KPIs Not Updating
Problem

KPIs were not responding to slicers.

Solution :
- Corrected relationships
- Updated DAX measures
- Adjusted filter context
  
### 3. Historical Data Loss
Problem : Fact table always contained only the latest 50 records.

Root Cause : TRUNCATE TABLE crypto.dim_coin CASCADE also removed data from fact_market_snapshot because of the foreign key relationship.

Solution :
- Removed destructive loading logic.
- Switched to append-only loading for the fact table.
- Refactored the ETL toward a production-style design.
  
### 4. Power BI Relationship Errors
Problem : Duplicate values in coin_name after introducing historical snapshots.

Solution :
- Identified that historical data requires a proper star schema.
- Planned migration from view-to-view relationships to a dimension (dim_coin) and fact (fact_market_snapshot) model.
  
### 5. Pipeline Automation
Problem : Running scripts individually.

Solution : 
- Created:
```text
run_pipeline.py
```
Which executes the entire ETL process from extraction through reporting.

---
# 📚 Key SQL Concepts Practiced
- SELECT
- WHERE
- ORDER BY
- GROUP BY
- HAVING
- LIMIT
- Aggregate Functions
- CASE
- Common Table Expressions (CTEs)
- Window Functions
- JOINs
- Views
- Indexes
- Constraints
- Foreign Keys

---
# 🐍 Python Skills Demonstrated
- REST API Integration
- JSON Processing
- Pandas Data Cleaning
- SQLAlchemy
- Modular Programming
- Exception Handling
- Logging
- File Handling
- Automation
- ETL Development

---
# 📊 Power BI Skills Demonstrated
- Data Modeling
- DAX Measures
- KPIs
- Cards
- Tables
- Charts
- Slicers
- Drill-through
- Dashboard Design
- Interactive Filtering
  
---
# 🧠 Key Learnings
Through this project I learned:
- How to build an end-to-end ETL pipeline.
- How to consume live API data.
- How to design a PostgreSQL data warehouse.
- The difference between OLTP and OLAP structures.
- How to model dimension and fact tables.
- How to work with SQL window functions.
- How to automate ETL pipelines.
- How to troubleshoot Power BI data model issues.
- How to integrate relational and NoSQL databases in a single project.
- The importance of data modeling and relationship design in Business Intelligence.

---
# 🚀 Future Improvements
- Deploy PostgreSQL on a cloud platform.
- Use Apache Airflow for orchestration.
- Containerize the application with Docker.
- Deploy Power BI to the Power BI Service.
- Implement Slowly Changing Dimensions (SCD).
- Add incremental loading.
- Add automated data quality validation.
- Integrate CI/CD using GitHub Actions.

---
# 👨‍💻 Author
Arfaz Shaikh

Aspiring Data Analyst | Business Analyst | Data Engineer

Skills :
- SQL
- Python
- PostgreSQL
- MongoDB
- Power BI
- Excel
- ETL Pipelines
- Data Warehousing
- Data Visualization

---
# 📂 Project Structure
```text
Crypto-Analytics/
│
├── .vscode/
│   └── launch.json
│
├── config/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── logging_config.py
│   └── mongodb.py
│
├── dashboards/
│   └── Crypto-Analytics.pbix
│
├── data/
│   ├── raw/
│   │   ├── csv/
│   │   │   └── crypto_raw.csv
│   │   └── json/
│   │       └── crypto_raw.json
│   │
│   └── processed/
│
├── images/
│   └── ERD.png
│
├── logs/
│   └── pipeline.log
│
├── mongodb/
│   └── mongo_loader.py
│
├── reports/
│   └── excel/
│       ├── Crypto_Report_20260716_222959.xlsx
│       ├── Crypto_Report_20260716_223131.xlsx
│       ├── Crypto_Report_20260716_223214.xlsx
│       ├── Crypto_Report_20260716_230514.xlsx
│       └── ....
│
├── scripts/
│   ├── __init__.py
│   ├── audit.py
│   ├── extract.py
│   ├── load_dimension.py
│   ├── load_fact.py
│   ├── load_mongodb.py
│   ├── load_postgres.py
│   ├── report_excel.py
│   ├── run_pipeline.py
│   └── transform.py
│
├── sql/
│   ├── Business Questions/
│   │   ├── Average price of each cryptocurrency.sql
│   │   ├── Categorize cryptocurrencies based on their current price.sql
│   │   ├── dense_rank.sql
│   │   ├── Find all cryptocurrencies priced above the average price.sql
│   │   ├── Highest recorded price for each cryptocurrency.sql
│   │   ├── How many cryptocurrencies are in our latest snapshot.sql
│   │   ├── How many snapshots do we have for each cryptocurrency.sql
│   │   ├── How many unique cryptocurrencies are we tracking.sql
│   │   ├── lag_query.sql
│   │   ├── lead_query.sql
│   │   ├── percentage_change.sql
│   │   ├── previous_price.sql
│   │   ├── price_difference.sql
│   │   ├── q1.sql
│   │   ├── q2.sql
│   │   ├── rank_query.sql
│   │   ├── row_number_query.sql
│   │   ├── Show only the Top 10 cryptocurrencies by market cap.sql
│   │   ├── Top 10 cryptocurrencies by average market cap.sql
│   │   ├── Top 10 Most Expensive Coins.sql
│   │   ├── Total trading volume for each cryptocurrency.sql
│   │   ├── What is the average cryptocurrency price.sql
│   │   ├── What is the highest cryptocurrency price.sql
│   │   ├── What is the lowest cryptocurrency price.sql
│   │   ├── What is the total market capitalization of all tracked cryptocurrencies.sql
│   │   ├── Which are the most expensive cryptocurrencies.sql
│   │   └── Which cryptocurrencies have a market cap greater than 10 billion.sql
│   │
│   ├── create/
│   │   ├── 01_create_schema.sql
│   │   ├── 02_create_dimension_tables.sql
│   │   ├── 03_create_fact_tables.sql
│   │   ├── create_dimension_table.sql
│   │   ├── create_etl_audit_table.sql
│   │   ├── create_fact_table.sql
│   │   ├── create_index.sql
│   │   ├── create_index_snapshot_time.sql
│   │   ├── create_index_time.sql
│   │   └── createdtable.sql
│   │
│   ├── verify/
│   │   ├── check_loader.sql
│   │   ├── checkdata.sql
│   │   ├── dump.sql
│   │   ├── verify_coin_history.sql
│   │   ├── verify_crypto_dim_data.sql
│   │   ├── verify_etl_audit_table.sql
│   │   ├── verify_fact_market_snapshot_data.sql
│   │   ├── verify_index.sql
│   │   ├── verify_index_snapshot_time.sql
│   │   ├── verify_latest_market_snapshot.sql
│   │   ├── verify_market_view_summary.sql
│   │   ├── verify_tables.sql
│   │   ├── verify_top_gainers.sql
│   │   ├── verify_top_losers.sql
│   │   └── verify_top_market_view.sql
│   │
│   └── view/
│       ├── view_coin_history.sql
│       ├── view_latest_market_snapshot.sql
│       ├── view_top_gainers.sql
│       ├── view_top_losers.sql
│       ├── view_top_market_cap.sql
│       └── views_market_summary.sql
│
├── .env
└── README.md
```
⭐ If you found this project useful

If you like this project, consider giving it a ⭐ on GitHub.

It motivates me to continue building and sharing real-world Data Analytics and Data Engineering projects.
