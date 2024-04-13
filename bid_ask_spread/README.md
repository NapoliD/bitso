
# Cryptocurrency Order Book Monitor

This Python program allows you to monitor cryptocurrency order books and save the data locally as CSV files and in Amazon S3.

## Requirements

- Python 3.x installed on your system.
- Bitso API Key and API Secret credentials to access the order books.
- AWS Access Key ID and Secret Access Key credentials to save the data in Amazon S3.

## Installation

1. Clone this repository or download the `bid_ask.py` file.
2. Install the necessary dependencies using `pip`:
Dependencies:

requests
hmac
hashlib
time
pandas
csv

   ```
   
   pip install ...
   ```

## Configuration

1. Open the `bid_ask.py` file in a text editor.
2. Replace the following variables with your own credentials:

   - `BITSO_API_KEY`: Your Bitso API Key.
   - `BITSO_API_SECRET`: Your Bitso API Secret.
   - `AWS_ACCESS_KEY_ID`: Your AWS Access Key ID.
   - `AWS_SECRET_ACCESS_KEY`: Your AWS Secret Access Key.
   - `S3_BUCKET_NAME`: The name of your Amazon S3 bucket where you want to store the files.
   - `monitor_order_books("-----".lower())`

## Usage

1. Make sure you have the `bid_ask.py` file . This file contains the necessary functions for the main program.
   
2. Run the `bid_ask.py` program with the trading pair you want to monitor as an argument.

   This will start monitoring the order book for example `btc_mxn` trading pair and save the data locally as CSV files and in Amazon S3.

3. The program will run continuously and update every 10 seconds, collecting data from the order book and saving it to the files.

4. To stop the program, you can press `Ctrl+C` in the terminal where it is running.

## Generated Files

- The data is saved locally in CSV files in the following directory structure:

  ```
  pair/year-month/pair_order_book_timestamp.csv
  ```

  For example: `BTC_USD/2024-04/BTC_USD_order_book_1618401697.csv`

- CSV files are also saved in your Amazon S3 bucket with the same directory structure.

## For Airflow
-  For Airflow, there are two example DAGs in the Airflow folder.
## Alerts and Reporting
-  Alerts can be configured to be sent to Slack or via email with prepared reports.

## Justification of partition in S3
- Here's a revised version:

- Organizing files into subfolders by year and month not only streamlines data management and access but also simplifies data lifecycle   management on S3, especially for automated transitions to Glacier storage. I would recommend storing daily data in CSV format initially and later archiving historical data in .parquet format. This format is efficient for storage and processing, compatible with Spark, Athena, and Redshift. Additionally, it optimizes data partitioning, enhancing performance in queries and analysis.
