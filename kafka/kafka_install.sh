#!/bin/bash

#/*****************************************************************
# SCRIPT: kafka_install.sh
# AUTHOR: Jamila McCalla
# DATE: 06-01-2024
# DESCRIPTION: Exercise 1 - Prepare the lab environment
#              - Download Kafka 2.8.0 for Scala 2.12
#              - Extract Kafka
#******************************************************************/

# Download Kafka
wget https://archive.apache.org/dist/kafka/2.8.0/kafka_2.12-2.8.0.tgz

# Extract Kafka
tar -xzf kafka_2.12-2.8.0.tgz
