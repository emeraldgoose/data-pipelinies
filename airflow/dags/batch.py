import datetime
from airflow.decorators import dag
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.providers.ssh.hooks.ssh import SSHHook


@dag(dag_id='batch_to_rdb', schedule_interval='@daily', start_date=datetime.datetime.now())
def batch_to_rdb():
    hook = SSHHook(
        remote_host='hadoop-spark',
        username='root',
        key_file='/root/.ssh/id_rsa.pub'
    )

    run_script = SSHOperator(
        task_id='run_script',
        ssh_hook=hook,
        command=f'/spark/bin/spark-submit /spark/logs_redis_to_hdfs.py --start_date 2022-11-29',
    )
    
    run_script
    
batch = batch_to_rdb()
