# Highway Traffic Data Integration and Stream Processing Project
ETL and Data Pipelines with Shell, Airflow and Kafka

## Project Scenario
I am a data engineer at a data analytics consulting company. I have been assigned to a project that aims to de-congest the national highways by analyzing the road traffic data from different toll plazas. Each highway is operated by a different toll operator with different IT setups that use various file formats. As a vehicle passes a toll plaza, the vehicle's data like vehicle_id, vehicle_type, toll_plaza_id, and timestamp are streamed to Kafka. 

My task involves aligning diverse datasets to extract valuable insights, ultimately aiding in the optimization of traffic flow. Subsequently, I will establish a data pipeline to capture timestamped data streamed through Kafka and efficiently integrate it into a database.

The following tasks are to: 

- Collect data available in different formats and consolidate it into a single file.
- Create a data pipeline that collects the streaming data and loads it into a database.

## Objectives
- Build an ETL Pipeline using Airflow
- Build a Streaming ETL Pipeline using Kafka

## Directions

### Final Assignment (Part 1) - Creating ETL Data Pipelines with Apache Airflow

#### Create a python script `ETL_toll_data.py` as the Apache Airflow DAG

1. Define the DAG arguments as per the following details:

    | Parameter | Value |
    | --------- | ----- |
    | owner | \<You may use any dummy name> |
    | start_date | today |
    | email | \<You may use any dummy email> |
    | email_on_failure | True |
    | email_on_retry | True |
    | retries | 1 |
    | retry_delay | 5 minutes |

1. Create a DAG as per the following details:

    | Parameter | Value |
    | --------- | ----- |
    | DAG id | `ETL_toll_data` |
    | Schedule | Daily once |
    | default_args | as you have defined in the previous step |
    | description | Apache Airflow Final Assignment |

   #### Create a shell script `Extract_Transform_data.sh` and add the following commands to your tasks:

3. Write a command to unzip the data. Use the downloaded data from the url given and uncompress it into the destination directory.
1. Update the shell script to add a command to extract data from csv file. You should extract the fields: `Rowid`, `Timestamp`, `Anonymized Vehicle number`, and `Vehicle type` from the `vehicle-data.csv` file and save them into a file named `csv_data.csv`.
1. Update the shell script to add a command to extract data from tsv file. You should extract the fields: `Number of axles`, `Tollplaza id`, and `Tollplaza code` from the `tollplaza-data.tsv` file and save it into a file named `tsv_data.csv`.
1. Update the shell script to add a command to extract data from fixed width file. You should extract the fields: `Type of Payment code`, and `Vehicle Code` from the fixed width file `payment-data.txt` and save it into a file named `fixed_width_data.csv`.
1. Update the shell script to add a command to consolidate data extracted from previous tasks. You should create a single csv file named `extracted_data.csv` by combining data from the following files:<br>
    * `csv_data.csv`
    * `tsv_data.csv`
    * `fixed_width_data.csv`

    The final csv file should use the fields in the order given below:<br>
    `Rowid`, `Timestamp`, `Anonymized Vehicle number`, `Vehicle type`, `Number of axles`, `Tollplaza id`, `Tollplaza code`, `Type of Payment code`, and `Vehicle Code`
1. Update the shell script to add a command to transform and load the data. You should transform the `Vehicle type` field in `extracted_data.csv` into capital letters and save it into a file named `transformed_data.csv`.
1. Create a task `extract_transform_load` in the `ETL_toll_data.py` to call the shell script.
1. Submit the DAG.
1. Unpause the DAG.
1. Monitor the DAG.

### Final Assignment (Part 2) - Creating Streaming Data Pipelines using Kafka

1. Start a MySQL Database server.
1. Create a table to hold the toll data.
1. Start Zookeeper server.
1. Start Kafka server.
1. Create a Kafka topic named `toll`.
1. Download the Toll Traffic Simulator `toll_traffic_generator.py` program.
1. Configure the Toll Traffic Simulator and set the topic to `toll`.
1. Run the Toll Traffic Simulator program.
1. Download the Streaming Data Consumer `streaming_data_reader.py` program.
1. Customize the consumer program to write into a MySQL database table.
1. Run the Streaming Data Consumer program.
1. Verify that streamed data is being collected in the database table.

2. ## Setup

Install the required libraries using the provided `requirements.txt` file. The command syntax is:

```bash
python3 -m pip install -r requirements.txt
```

Create a directory structure for staging area as follows:

```bash
sudo mkdir -p /home/project/airflow/dags/finalassignment/staging
```

Execute the provided commands to prevent any permission-related issues:

```bash
# bash
sudo chown -R 100999 /home/project/airflow/dags
sudo chmod -R g+rw /home/project/airflow/dags

# python
sudo chown -R 100999 /home/project/airflow/dags/finalassignment
sudo chmod -R g+rw /home/project/airflow/dags/finalassignment  
sudo chown -R 100999 /home/project/airflow/dags/finalassignment/staging
sudo chmod -R g+rw /home/project/airflow/dags/finalassignment/staging
```

Utilize the terminal command to download the necessary dataset to the designated destination:

```bash
# bash
sudo wget -P /home/project/airflow/dags https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz

Download Toll Traffic Simulator program:

```bash
sudo wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/toll_traffic_generator.py
```

Download Streaming Data Consumer program:

```bash
sudo wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/streaming_data_reader.py
```
