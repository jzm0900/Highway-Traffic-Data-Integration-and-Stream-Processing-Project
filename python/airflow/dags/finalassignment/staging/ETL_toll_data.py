# import the libraries

from datetime import timedelta
from airflow import DAG 
from airflow.operators.bash.operators import BashOperator 
from airflow.utils.dates import days_ago


# defining DAG arguments 

default_args = {
    'owner': 'Jamila',
    'start_date': days_ago(0),
    'email': ['jmac@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# define the DAG 

dag = DAG(
    dag_id='ETL_toll_data',
    schedule_interval=timedelta(days=1) ,
    default_args=default_args,
    description='Apache Airflow Final Assignment',
)

# define the tasks

# define the unzip data task

unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='tar -xzvf /home/project/tolldata.tgz -C /home/project/airflow/dags/finalassignment/staging',
    dag=dag,
)

# define extract csv data task
extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command='cut -f1-4 -d"#" vehicle-data.csv > /home/project/airflow/dags/finalassignment/staging/csv_data.csv',
    dag=dag,
)

# define extract tsv data task
extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command='cut -f5-7 -d$\'\t\'" tolldata-data.tsv > /home/project/airflow/dags/finalassignment/staging/tsv_data.csv',
    dag=dag,
)

# define extract data fixed width task
extract_data_from_fixed_width = BashOperator (
    task_id='extract_data_from_fixed_width',
    bash_command='cut -f6-7 -d" payment-data.txt > /home/project/airflow/dags/finalassignment/staging/fixed_width_data.csv',
    dag=dag,
)

# define consolidate_data task

consolidate_data = BashOperator (
    task_id='consolidate_data',
    bash_command='paste -d"," csv_data.csv tsv_data.csv fixed_width_data.csv | cut -f1-9 -d"," > /home/project/airflow/dags/finalassignment/staging/extracted_data.csv',
    dag=dag,
)

# define transform_data task

transform_data = BashOperator (
    task_id='transform_data',
    bash_command='tr "[a-z]" "[A-Z]" < /home/project/airflow/dags/finalassignment/staging/extracted_data.csv > /home/project/airflow/dags/finalassignment/staging/transformed_data.csv',
    dag=dag,
)

# pipeline task

unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data
