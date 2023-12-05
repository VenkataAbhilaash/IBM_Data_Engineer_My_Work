from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago
#defining DAG arguments
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'Abhilaash Annamreddi',
    'start_date': days_ago(0),
    'email': ['ramesh@somemail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
# defining the DAG
# define the DAG
dag = DAG(
    'process_web_log',
    default_args=default_args,
    description='My first DAG',
    schedule_interval=timedelta(days=1),
)

extracted_data= BashOperator(
task_id ='extract_1',
bash_command='cut -d"-" -f1 /home/project/accesslog.txt > /home/project/extracted_data.txt',
dag=dag,
)

transformed_data=BashOperator(
    task_id ='transform_1',
    bash_coomand='cat /home/project/extracted_data.txt > /home/project/transformed_data.txt',
    dag=dag,
)

load_data =BashOperator(
    task_id = 'load_1',
    bash_command= 'tar -cvf /home/project/weblog.tar /home/project/transformed_data.txt',
    dag=dag,
)

extract_1 >> transform_1 >> load_1