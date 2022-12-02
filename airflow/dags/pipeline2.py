import pandas as pd
import datetime
import pyspark
import sqlalchemy
import pendulum
from airflow.decorators import dag, task

kst = pendulum.timezone("Asia/Seoul")
yesterday = datetime.datetime.now(tz=kst) - datetime.timedelta(days=1)

@dag(dag_id='store_to_postgres', schedule_interval='@daily', start_date=yesterday, tags=['batch','hdfs','rdb'])
def batch_to_rdb():
    @task
    def get_logs_from_hdfs():
        sc = pyspark.SparkContext(master='local', conf=pyspark.SparkConf())
        sqlContext = pyspark.sql.SQLContext(sc)
        df = sqlContext.read.parquet(f'hdfs://hadoop-spark:9000/warehouse/{yesterday.strftime("%Y%m%d")}.parquet')
        df.write.parquet('data.parquet')
    
    @task
    def transform():
        """remove, rename columns"""
        df = pd.read_parquet('data.parquet', engine='pyarrow')
        df = df.rename(
            columns = {
                "clientgeoip.geo.country_name" : "country_name",
                "clientgeoip.geo.region_name" : "region_name",
                "clientgeoip.geo.city_name" : "city_name",
                "user_agent.name" : "browser",
                "user_agent.device.name" : "device",
                "user_agent.os.name" : "os_name",
                "user_agent.os.version" : "os_version"
            }
        )
        df['timestamp'] = pd.to_datetime(df['time_local'], format='%d/%b/%Y:%H:%M:%S +0900').dt.strftime('%Y-%m-%dT%H:%M:%S')
        df = df[
            ['timestamp','UA','body_bytes_sent','country_name','httpversion','message','method','referrer','remote_addr','remote_user','request','response_time','status','device','browser','os_name','os_version','city_name','region_name']
        ]

        df_yesterday = df.loc[(df['timestamp'] >= yesterday.strftime('%Y-%m-%d')+'T0:0:0') & (df['timestamp'] <= yesterday.strftime('%Y-%m-%d')+'T23:59:59')]
        df_today = df.loc[(df['timestamp'] > yesterday.strftime('%Y-%m-%d')+'T23:59:59')]
        df_yesterday.to_parquet('yesterday.parquet', engine='pyarrow', compression=None, index=False)
        df_today.to_parquet('today.parquet', engine='pyarrow', compression=None, index=False)
    
    @task
    def store_to_postgres():
        engine = sqlalchemy.create_engine('postgresql://root:root@postgres/mart')
        df_yesterday = pd.read_parquet('yesterday.parquet', engine='pyarrow')
        df_today = pd.read_parquet('today.parquet', engine='pyarrow')

        df_yesterday.to_sql(name=f'mart_{yesterday.strftime("%Y%m%d")}', con=engine, if_exists='append', index=False)
        df_today.to_sql(name=f'mart_{(yesterday + datetime.timedelta(days=1)).strftime("%Y%m%d")}', con=engine, if_exists='append', index=False)
        engine.dispose()

    get_logs_from_hdfs() >> transform() >> store_to_postgres()
    
pipeline = batch_to_rdb()
