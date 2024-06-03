#!/bin/bash

#/*****************************************************************
# SCRIPT: create_topic_toll.sh
# AUTHOR: Jamila McCalla
# DATE: 06-01-2024
# DESCRIPTION: Create a topic named 'toll'.

#******************************************************************/

# Create a topic named toll
cd kafka_2.12-2.8.0
bin/kafka-topics.sh --create --topic toll --bootstrap-server localhost:9092
