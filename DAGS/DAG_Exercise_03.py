import time
import akey
from airflow import DAG 
from airflow.operators.python_operator import PythonOperator 
from airflow.operators.python import BranchPythonOperator 
from airflow.operators.dummy import DummyOperator
from datetime import datetime, timedelta
import pandas as pd 
import numpy as np 
import os
import requests
import json


def get_data():
    headers ={
        'X-CMC_PRO_API_KEY': akey.API,
        'Accepts' :'application/json'    
    }

    params = {
        'start' : '1',
        'limit' : '10',
        'convert': 'USD'
    }

    url1='https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    json = requests.get(url1,params=params,headers=headers).json()
    coins= json['data']
    return coins

def get_prices(coins):
    
    for x in coins: 
            print(x['symbol'],round(x['quote']['USD']['price'],2))


default_dag_args = { 
    'start_date': datetime(2022, 9, 1), 
    'email_on_failure': False, 
    'email_on_retry': False, 
    'retries': 1, 
    'retry_delay': timedelta(minutes=5), 
    'project_id': 1 }


with DAG(dag_id="DAG_Exercise_03", 
         schedule_interval = None, 
         default_args = default_dag_args,
         catchup=False
) as dag_python:

    get_data= PythonOperator(task_id="get_data",
                            python_callable=get_data

    )
    get_prices= PythonOperator(task_id="get_prices",
                            python_callable=get_prices

    )

get_data>>get_prices