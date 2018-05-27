import os
from datetime import datetime
from airflow import DAG
from airflow.configuration import conf
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

testFile = os.environ["AIRFLOW_CGCP_FILE_LOCATION_TEST"]
buildFile = os.environ["AIRFLOW_CGCP_FILE_LOCATION_BUILD"]
loadFile = os.environ["AIRFLOW_CGCP_FILE_LOCATION_LOAD"]
dbManipulationsFile = os.environ["AIRFLOW_CGCP_FILE_LOCATION_DB_MANIP"]
completeCasesFile = os.environ["AIRFLOW_CGCP_FILE_LOCATION_COMPLETE_CASES"]
imputeFile = os.environ["AIRFLOW_CGCP_FILE_LOCATION_IMPUTE"]

dag = DAG(
    'cgcp',
    description='DAG for dissertation scripts',
    schedule_interval=None,
    start_date=datetime(2018, 5, 20),
    catchup=False
)

build = BashOperator(
    task_id= 'build',
    bash_command=buildFile,
    dag=dag
)

load = BashOperator(
    task_id= 'load',
    bash_command=loadFile,
    dag=dag
)

dbManipulations = BashOperator(
    task_id= 'dbManipulations',
    bash_command=dbManipulationsFile,
    dag=dag
)

completeCases = BashOperator(
    task_id= 'completeCases',
    bash_command=completeCasesFile,
    dag=dag
)

impute = BashOperator(
    task_id= 'impute',
    bash_command=imputeFile,
    dag=dag
)

build >> load >> dbManipulations >> completeCases >> impute
