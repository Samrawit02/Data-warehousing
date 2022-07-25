from airflow import DAG
from airflow.operators.mysql_operator import MySqlOperator

default_arg = {'owner': 'airflow', 'start_date': '2022-07-23'}

dag = DAG('load-data',
          default_args=default_arg,
          schedule_interval='@once',
          template_searchpath=['/usr/local/airflow/include/'])

create_table = MySqlOperator(dag=dag,
                           mysql_conn_id='mysql-connect', 
                           task_id='create_table',
                            sql='./mysql_schema/create_table.sql')


load_data = MySqlOperator(dag=dag,
                           mysql_conn_id='mysql-connect', 
                           task_id='load_data',
                            sql='./mysql_schema/load_data.sql')

create_table >> load_data 