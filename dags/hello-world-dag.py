from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Define DAG
with DAG(
    dag_id="hello_world_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,  # Trigger manually
    catchup=False,
    tags=["example"],
) as dag:

    # Simple task
    hello_task = BashOperator(
        task_id="print_hello",
        bash_command="echo 'Hello, World! from Airflow 🎉'"
    )
