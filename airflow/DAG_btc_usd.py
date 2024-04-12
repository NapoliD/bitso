from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from monitor_order_books import monitor_order_books

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'monitor_bitcoin_order_books',
    default_args=default_args,
    description='Monitor Bitcoin order books',
    schedule_interval=timedelta(minutes=10),  # Adjust the interval as needed
)

def run_monitoring():
    monitor_order_books("btc_usd")

run_monitoring_task = PythonOperator(
    task_id='run_monitoring',
    python_callable=run_monitoring,
    dag=dag,
)

run_monitoring_task
