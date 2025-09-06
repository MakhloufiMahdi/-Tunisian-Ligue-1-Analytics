from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime

def transform_players():
    hook = PostgresHook(postgres_conn_id="ligue1_postgres")
    conn = hook.get_conn()
    cur = conn.cursor()
    cur.execute("""
        UPDATE player_stats
        SET total_contributions = goals + assists;
    """)
    conn.commit()
    cur.close()
    conn.close()

def transform_team_stats():
    hook = PostgresHook(postgres_conn_id="ligue1_postgres")
    conn = hook.get_conn()
    cur = conn.cursor()
    cur.execute("""
        UPDATE team_stats
        SET goal_difference = goals_scored - goals_conceded;
    """)
    conn.commit()
    cur.close()
    conn.close()

def transform_standings():
    hook = PostgresHook(postgres_conn_id="ligue1_postgres")
    conn = hook.get_conn()
    cur = conn.cursor()
    cur.execute("""
        UPDATE standings
        SET goal_difference = goals_for - goals_against;
    """)
    conn.commit()
    cur.close()
    conn.close()

with DAG(
    dag_id='ligue1',
    start_date=datetime(2025, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=['el', 'liguéf', 'tunisie']
) as dag:

    t1 = PythonOperator(task_id='transform_players', python_callable=transform_players)
    t2 = PythonOperator(task_id='transform_team_stats', python_callable=transform_team_stats)
    t3 = PythonOperator(task_id='transform_standings', python_callable=transform_standings)

    t1 >> t2 >> t3

    

