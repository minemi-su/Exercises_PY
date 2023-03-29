from airflow import DAG 
from airflow.operators.python_operator import PythonOperator 
from datetime import datetime, timedelta

def python_first_function(): 
    now=datetime.now()
    print(f"current time is : {now}")


default_dag_args = { 
    'start_date': datetime(2022, 9, 1), 
    'email_on_failure': False, 
    'email_on_retry': False, 
    'retries': 1, 
    'retry_delay': timedelta(minutes=5), 
    'project_id': 1 }

with DAG(dag_id="DAG_Exercise_02", 
         schedule_interval = None, 
         default_args = default_dag_args
         catchup=False
) as dag:

    task_0 = PythonOperator(
        task_id = "first_python_task", python_callable = python_first_function)
