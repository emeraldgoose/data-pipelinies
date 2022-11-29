#!/bin/bash
/etc/init.d/ssh start
$HADOOP_HOME/sbin/start-all.sh
$SPARK_HOME/sbin/start-all.sh
$SPARK_HOME/sbin/start-history-server.sh