import os
from datetime import datetime
from airflow import DAG
from airflow.configuration import conf
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

buildFileConf = conf['cgcp']['buildFile']
print(buildFileConf)

dag = DAG(
    'cgcp',
    description='DAG for dissertation scripts',
    schedule_interval=None,
    start_date=datetime(2018, 5, 20),
    catchup=False
)

dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)

build_proj = BashOperator(
    task_id= 'build',
    bash_command=buildFileConf,
    dag=dag
)

dummy_operator >> build_proj
