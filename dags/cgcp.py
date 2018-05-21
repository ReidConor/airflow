import os
from datetime import datetime
from airflow import DAG
from airflow.configuration import conf
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

testFile = os.environ["AIRFLOW_CGCP_FILE_LOCATION_TEST"]
buildFile = os.environ["AIRFLOW_CGCP_FILE_LOCATION_BUILD"]

dag = DAG(
    'cgcp',
    description='DAG for dissertation scripts',
    schedule_interval=None,
    start_date=datetime(2018, 5, 20),
    catchup=False
)

dummy_operator = DummyOperator(
    task_id='dummy_task',
    retries=3,
    dag=dag
)

test_proj = BashOperator(
    task_id= 'test',
    bash_command=testFile,
    dag=dag
)

build_proj = BashOperator(
    task_id= 'build',
    bash_command=buildFile,
    dag=dag
)

dummy_operator >> test_proj >> build_proj
