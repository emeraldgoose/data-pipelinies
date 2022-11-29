#!/bin/bash
python3.8 /root/producer.py &
/filebeat/filebeat -e -c /filebeat/filebeat.yml