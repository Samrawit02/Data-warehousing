from datetime import timedelta
from airflow import DAG
from airflow.operators.mysql_operator import MySqlOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime,timedelta  


default_arg = {'owner': 'airflow', 'start_date': '2022-09-01'}


dag = DAG(
    'create_tables',
    default_args=default_arg,
    description='An Airflow DAG to create tables',
    schedule_interval='@daily',
)

check_file = BashOperator(
    task_id="check_file",
    bash_command= "shasum  ~ /data/data.csv",
    retries=2,
    retry_delay=timedelta(seconds=15),
    dag=dag
)
test = MySqlOperator(
    task_id='test',
    mysql_conn_id="mysql_conn_id",
    sql='SHOW VARIABLES LIKE "secure_file_priv";',
    dag=dag
)

create_table = MySqlOperator(
    task_id='create_table',
    mysql_conn_id='mysql_conn_id',
    sql='./mysql_schema/create_table.sql',
    dag=dag,
)
load_data = MySqlOperator(dag=dag,
                           mysql_conn_id='mysql_conn_id', 
                           task_id='load_data',
                            sql='./mysql_schema/load_data.sql')

check_file>> create_table >> load_data