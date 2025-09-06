# 📌 Context

This DAG is part of the Tunisian-Ligue-1-Analytics project. After loading the data into PostgreSQL, Apache Airflow orchestrates a series of automated transformations to enrich the tables and prepare the data for visualizations and decision-making analyses.

# 🛠️ DAG Objective

Update player contributions (goals + assists).

Calculate team goal differences.

Update goal difference in the standings.

# 🔄 Task Dependencies

transform_players → transform_team_stats → transform_standings

# 📅 Scheduling

The DAG runs daily.
