from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from bid_ask import monitor_order_books

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,  # Set to 0 to disable retries
}

dag = DAG(
    'continuous_order_book_monitoring',
    default_args=default_args,
    description='Periodically monitor order books continuously',
    schedule_interval=timedelta(minutes=10),  # Set the interval as needed
)

monitor_task = PythonOperator(
    task_id='run_order_book_monitoring',
    python_callable=monitor_order_books,
    op_args=["btc_usd"],  # Pass any arguments needed by the function
    dag=dag,
)

monitor_task

