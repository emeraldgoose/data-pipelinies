import datetime
import pendulum
from airflow.decorators import dag
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.providers.ssh.hooks.ssh import SSHHook

kst = pendulum.timezone('Asia/Seoul')
now = datetime.datetime.now().strftime('%Y-%m-%d')
one_day_ago = datetime.datetime.now(tz=kst) - datetime.timedelta(days=1)

@dag(dag_id='logs_redis_to_hdfs', schedule_interval='@daily', start_date=one_day_ago, tags=['batch','redis','hdfs'])
def parquet_to_hdfs_from_logstash():
    hook = SSHHook(
        remote_host='hadoop-spark',
        username='root',
        key_file='/root/.ssh/id_rsa.pub'
    )

    run_script = SSHOperator(
        task_id='run_script',
        ssh_hook=hook,
        command=f'/spark/bin/spark-submit /spark/logs_redis_to_hdfs.py --start_date {now}',
    )
    
    run_script
    
pipeline = parquet_to_hdfs_from_logstash()
