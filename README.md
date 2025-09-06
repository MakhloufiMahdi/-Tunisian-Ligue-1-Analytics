# -Tunisian-Ligue-1-Analytics
Welcome to the Tunisian Ligue 1 Analytics Project, a comprehensive data pipeline and analytics workflow covering players, teams, and match statistics from the Tunisian Ligue 1. This project demonstrates advanced web scraping, ETL, database management, Airflow orchestration, SQL analysis, and data visualization skills.
📂 Folder Overview

python/: Scraping scripts

data/: Raw Excel data

postgresql/: SQL scripts, database setup, and analysis

SSIS/: ETL workflow and proof

APACHE_AIRFLOW/: DAG script and execution 

dashboard/: Tableau dashboard

dashboard_analysis/: Analysis of insights
# 📝 Project Workflow
1. Data Collection (Web Scraping)

The project begins with web scraping scripts (ca.py, ess.py, est.py, usmo.py) that collect:

Top players from major clubs

Player performance statistics

Team stats and league standings

The scraped data is saved as Excel files in the data/ folder.
#  Database Setup (PostgreSQL)

A PostgreSQL database named ligue1 is created with 5 main tables:

player_stats – Detailed performance metrics for players

players – Player information and metadata

standings – League rankings and points

teams – Team-level information

team_stats – Team performance statistics

Scripts for table creation and  the database structure are located in postgresql/ folder.
# . ETL Pipeline (SSIS)

The ETL process is implemented using SQL Server Integration Services (SSIS):

Extract: Read data from Excel files 

Transform: Clean data, adjust types, and prepare for database insertion

Load: Insert data into PostgreSQL tables

Proofs of the ETL process are documented in SSIS/ folder 
# . Workflow Orchestration (Apache Airflow)

A DAG orchestrates the ETL and transformation tasks:
transform_players → transform_team_stats → transform_standings
Proofs process are documented in APACHE AIRFLOW/ folder 
# . Data Analysis (PostgreSQL)

SQL queries explore player performance, team comparisons,  and scoring trends.
Results  are stored in postgresql/analysis/.
# . Data Visualization (Tableau)

A Tableau dashboard summarizes the insights:

Player and team statistics

League standings and trends

Scoring analysis
Proofs process are documented in DASHBOARD/ folder and ANALYSE DASH/ folder
## 🛠️ Tools Used

# Programming & Data Collection

🐍 Python – Web scraping & data handling

📊 Pandas – Data cleaning & manipulation

🌐 Requests / BeautifulSoup – Web scraping libraries

# Database Management

🐘 PostgreSQL – Relational database for structured storage

🔑 SQL – Queries and analysis

# ETL & Data Integration

⚙️ SQL Server Integration Services (SSIS) – ETL workflows (Extract, Transform, Load)

📂 Excel – Intermediate storage of scraped data

# Workflow Orchestration

⏳ Apache Airflow – Automated DAGs for pipeline scheduling and monitoring

# Data Analysis & Visualization

🖥️ Tableau – Dashboard creation and visualization

📈 SQL Queries – Analytical insight
