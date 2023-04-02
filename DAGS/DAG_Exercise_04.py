from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.postgres import PostgresOperator

default_args= {
        'owner':'minemisu',
        'retries':0,
        
}
delete_table= """ 
        DROP table employee                 
"""
create_table=""" 
                create table employee (
                        id int PRIMARY KEY AUTO INCREMENT,
                        dt date NOT NULL,
                        dag_id character varying,
                        name varchar(255)  NOT NULL,
                        age int  NOT NULL)
                
                """
insert_to_table=""" 
                insert into employee (dt, dag_id, name, age) values ('{{ds}}','{{dag.dag_id}}', 'Mine', 32), ('{{ds}}','{{dag.dag_id}}', 'Barış', 34), ('{{ds}}','{{dag.dag_id}}', 'Oğul', 29)
                
                """
AVG_age= """ 
                SELECT AVG(emp.age) FROM employee AS emp
                
                """

with DAG (
    dag_id='DAG_with_postgres_v01',
    default_args=default_args,
    start_date=datetime(2023,4,1),
    schedule_interval='0 0 * * *',
    catchup= False
) as dag:
       
        delete_table=PostgresOperator(
                task_id='Delete_Table',
                postgres_conn_id='Postgres_localhost',
                sql= delete_table )
        create_table=PostgresOperator(
                task_id='Create_Table',
                postgres_conn_id='Postgres_localhost',
                sql= create_table)
        
        insert_to_table=PostgresOperator(
                task_id='Insert_to_table',
                postgres_conn_id='Postgres_localhost',
                sql= insert_to_table
        )


        AVG_age=PostgresOperator(
                task_id='average_age',
                postgres_conn_id='Postgres_localhost',
                sql= AVG_age
                )
        
delete_table>>create_table>>insert_to_table>>AVG_age




