#!/bin/bash

#/*****************************************************************
# SCRIPT: start_kafka.sh
# AUTHOR: Jamila McCalla
# DATE: 06-01-2024
# DESCRIPTION: Start Kafka message broker service.
#******************************************************************/

# Start Kafka message broker service
cd kafka_2.12-2.8.0
bin/kafka-server-start.sh config/server.properties
