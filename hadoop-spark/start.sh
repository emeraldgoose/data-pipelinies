#!/bin/bash
service ssh start
sleep 5

# hadoop start
$HADOOP_HOME/sbin/start-all.sh
$HADOOP_HOME/bin/hdfs dfs -mkdir hdfs://hadoop-spark:9000/warehouse

# spark start
$SPARK_HOME/sbin/start-all.sh
$SPARK_HOME/sbin/start-history-server.sh

# running loop
tail -f /dev/null