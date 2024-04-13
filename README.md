
This repository contains two folders: `bid_ask_spread` addressing Challenge 1, and `snapshot_tables` addressing Challenge 2.

## Folder Structure

1. **bid_ask_spread**: This folder contains the solution for Challenge 1.
2. **snapshot_tables**: This folder contains the solution for Challenge 2.

## Solution Overview

### `bid_ask_spread`

The `bid_ask_spread` solution provides a versatile library, `bid_ask.py`, suitable for various environments such as Lambda, AWS Glue, EC2, or Airflow.

#### Usage Scenarios:
- **Lambda**: Deploy and orchestrate with EventBridge.
- **AWS Glue**: Compatible with AWS Glue for ETL jobs.
- **EC2 or Airflow**: Utilize in EC2 instances or Apache Airflow workflows.

### Data Querying

Processed data can be stored in RDS or linked with CSV files in S3 using Athena for querying. Integration with Amazon QuickSight allows creating interactive dashboards.

### `snapshot_tables`

In the `snapshot_tables` folder, an ERD was initially created to understand the relationships. Subsequently, a database was created with Python, and data was ingested using Pandas. SQL was used to answer questions, simulating a relational database. 

#### Production Environment Options:
For production, options like Athena linked to S3 or RDS MySQL can be utilized economically.

## Getting Started

To get started:

1. Navigate to the respective folders (`bid_ask_spread` or `snapshot_tables`) and review the solution files.
2. Import the required libraries into your environment.
3. For data querying, consider storing the processed data in RDS or linking CSV files in S3 using Athena.


## Requirements

- Python 3.x
