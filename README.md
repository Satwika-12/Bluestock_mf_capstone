# Mutual Fund Analytics Capstone Project - Bluestock Fintech

## Overview
This repository contains an end-to-end data analytics and risk evaluation pipeline for Mutual Fund performance analysis.

## Key Features & Deliverables
- **Data Ingestion & Cleaning:** Standardized NAV history, transactions, and scheme metrics into SQLite database.
- **Performance Ratios:** Computed CAGR (1yr, 3yr, 5yr), Sharpe Ratio ($R_f = 6.5\%$), Sortino Ratio, and Max Drawdown.
- **Benchmark Analytics:** Evaluated Alpha & Beta metrics using OLS Regression against Nifty 100 benchmark.
- **Scorecards:** Generated fund risk-return scorecards and benchmark comparison visual charts.

## Folder Structure
bluestock_mf_capstone/
├── Data/
│   ├── raw/
│   └── processed/
├── Notebooks/
│   └── 04_performance_analytics.ipynb
├── Sql/
│   └── schema.sql
├── data_cleaning.py
└── README.md
## How to Run
1. Install requirements: `pip install pandas numpy scipy matplotlib ipykernel`
2. Run database setup in `Sql/schema.sql`
3. Execute analytics in `Notebooks/04_performance_analytics.ipynb`
   > **Disclaimer:** This repository uses publicly available AMFI Mutual Fund market data for analytical learning and portfolio showcase. No private company credentials or internal APIs are included.
