#!/bin/bash
airflow users create \
    --username airflow \
    --firstname FIRST_NAME \
    --lastname LAST_NAME \
    --role Admin \
    --email admin@example.org \
    --password airflow

nohup airflow scheduler &

airflow webserver -p 8080