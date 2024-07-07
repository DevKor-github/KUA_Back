import pendulum
from datetime import timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

from src.nickname_algo import *


# from src.stock_algo import

kst = pendulum.timezone('Asia/Seoul')
dag_name = "KU_A"

default_args = {
    'owner': 'kua',
    'retries': 3,
    'retry_delay': timedelta(minutes=1)
}
with DAG(
    dag_id=dag_name,
    default_args=default_args,
    description='Random Nickname Pipeline',
    schedule_interval=timedelta(hours=12),
    start_date = pendulum.datetime(2024, 7, 2, 9, 0, 0, tz=kst),
    catchup=False,
    tags=['nicknames', 'KUA', 'KU&A']
) as dag:
    make_random_number_task = PythonOperator(
        task_id='make_random_number_task',
        python_callable=make_random_number_list,
    )
    make_random_nickname_task = PythonOperator(
        task_id = 'make_random_nickname_task',
        python_callable=make_random_nickname,
    )
    set_nickname_task = PythonOperator(
        task_id = 'set_nickname_task',
        python_callable=set_nickname,
    )
    make_random_number_task >> make_random_nickname_task >> set_nickname_task