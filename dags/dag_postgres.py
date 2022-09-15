from datetime import timedelta
from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime,timedelta  


default_arg = {'owner': 'airflow', 'start_date': '2022-09-01'}


dag = DAG(
    'postgres_create_tables',
    default_args=default_arg,
    description='An Airflow DAG to create tables',
    schedule_interval='@daily',
)

check_file = BashOperator(
    task_id="postgres_check_file",
    bash_command="shasum ~/dags/data.csv",
    retries=2,
    retry_delay=timedelta(seconds=15),
    dag=dag
)
test = PostgresOperator(
    task_id='postgres_test',
    postgres_conn_id="postgres_conn_id",
    sql='SHOW VARIABLES LIKE "secure_file_priv";',
    dag=dag
)

create_table = PostgresOperator(
    task_id='postgres_create_table',
    postgres_conn_id='postgres_conn_id',
    sql='./postgres_schema/create_table.sql',
    dag=dag,
)
load_data = PostgresOperator(dag=dag,
                           postgres_conn_id='postgres_conn_id', 
                           task_id='load_data',
                            sql='./postgres_schema/load_data.sql')

check_file>> create_table >> load_data