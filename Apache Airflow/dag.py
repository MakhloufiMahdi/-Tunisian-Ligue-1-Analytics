from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import psycopg2

def transform_players():
    conn = psycopg2.connect(
        host="localhost",
        database="ligue1",
        user="postgres",
        password="******"
    )
    cur = conn.cursor()
    cur.execute("""
        UPDATE player_stats ps
        SET total_contributions = ps.goals + ps.assists;
    """)
    conn.commit()
    cur.close()
    conn.close()

def transform_team_stats():
    conn = psycopg2.connect(
        host="localhost",
        database="ligue1",
        user="postgres",
        password="******"
    )
    cur = conn.cursor()
    cur.execute("""
        UPDATE team_stats ts
        SET goal_difference = ts.goals_scored - ts.goals_conceded;
    """)
    conn.commit()
    cur.close()
    conn.close()

def transform_standings():
    conn = psycopg2.connect(
        host="localhost",
        database="ligue1",
        user="postgres",
        password="*******"
    )
    cur = conn.cursor()
    cur.execute("""
        UPDATE standings s
        SET goal_difference = s.goals_for - s.goals_against;
    """)
    conn.commit()
    cur.close()
    conn.close()

with DAG(
    'ligue1',
    start_date=datetime(2025, 1, 1),
    schedule='@daily',
    catchup=False,
    tags=['el','liguéf', 'tunisie']
) as dag:


    t1 = PythonOperator(task_id='transform_players', python_callable=transform_players)
    t2 = PythonOperator(task_id='transform_team_stats', python_callable=transform_team_stats)
    t3 = PythonOperator(task_id='transform_standings', python_callable=transform_standings)

    t1 >> t2 >> t3
