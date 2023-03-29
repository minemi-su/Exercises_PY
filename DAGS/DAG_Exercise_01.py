from airflow import DAG 
from airflow.operators.bash_operator import BashOperator 
from datetime import datetime, timedelta

default_dag_args = { 
    'start_date': datetime(2022, 1, 1), 
    'email_on_failure': False, 
    'email_on_retry': False, 
    'retries': 1, 
    'retry_delay': timedelta(minutes=5), 
    'project_id': 1 }

with DAG(dag_id="DAG_Exercise_01", 
         schedule_interval = None, 
         default_args = default_dag_args
         catchup=False
) as dag:

        # here at this level we define our tasks of the DAG
        task_3 = BashOperator(
                task_id = 'bash_task_folder'
                bash_command="cd /Users/user/Desktop")
        task_0 = BashOperator(
                task_id = 'bash_task', 
                bash_command = "echo 'command executed from Bash Operator' >> result.txt")

        task_1 = BashOperator(
                task_id = 'bash_task_move_data', 
                bash_command = "copy /Users/user/Desktop/result.txt  /Users/user/Desktop/learn/develhope/DAG")

        task_2 = BashOperator(
                task_id = 'bash_task_remove_data', 
                bash_command = "delete /Users/user/Desktop/result.txt")


task_3 >> task_0 >> task_1 >> task_2