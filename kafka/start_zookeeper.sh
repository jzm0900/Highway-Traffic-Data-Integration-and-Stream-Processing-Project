#!/bin/bash

#/*****************************************************************
# SCRIPT: start_zookeeper.sh
# AUTHOR: Jamila McCalla
# DATE: 06-01-2024
# DESCRIPTION: Start Zookeeper server
#******************************************************************/

# Start Zookeeper server
cd kafka_2.12-2.8.0
bin/zookeeper-server-start.sh config/zookeeper.properties
