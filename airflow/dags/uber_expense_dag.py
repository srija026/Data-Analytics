from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'uber_expense_dag',
    default_args=default_args,
    description='ETL pipeline for Uber expenses',
    schedule_interval=timedelta(days=1),
)

def extract_data():
    # Dummy implementation for data extraction
    # Replace this with actual data extraction logic
    pass

def transform_data():
    # Dummy implementation for data transformation
    # Replace this with actual data transformation logic
    pass

def load_data():
    redshift_hook = PostgresHook(postgres_conn_id='redshift')
    # Dummy implementation for data loading
    # Replace this with actual data loading logic
    redshift_hook.run("SQL_STATEMENT")

extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag,
)

extract_task >> transform_task >> load_task
