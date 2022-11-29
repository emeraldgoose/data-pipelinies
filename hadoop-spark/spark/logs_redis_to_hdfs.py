from typing import Any
import json, argparse, datetime
import pandas as pd
import redis
from pyspark.sql import SparkSession

def get_logs_from_redis(key: Any):
    r = []
    rq = redis.Redis(host='redis', port=6379, db=0)
    while rq.llen(key):
        _, value = rq.brpop(key)
        value = json.loads(value)
        value = pd.json_normalize(value).to_dict(orient='records')[0]
        r.append(value)
    return r

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    start_date = parser.add_argument('--start_date', type=str, required=True)
    # interval = parser.add_argument('--interval', type=str, default='day', help='`minute` or `hour` or `day`')
    args = parser.parse_args()

    start_date = datetime.datetime.strptime(args.start_date, '%Y-%m-%d')
    key = start_date.strftime('%Y%m%d')
    data = get_logs_from_redis(key)

    spark = SparkSession.builder.appName('Warehouse').getOrCreate()
    df = spark.createDataFrame(data)
    df.write.parquet(f'hdfs://localhost:9000/warehouse/{key}.parquet',mode='append')
    spark.stop()
