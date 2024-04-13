# SQLite3 Database Creation and Query Example Project

This project consists of a set of Python scripts to create an SQLite3 database and perform SQL queries on the generated tables.

## Files

1. **create_db.py**: This script takes CSV files named `deposit_sample_data.csv`, `withdrawals_sample_data.csv`,`user_id_sample_data`, and `event_sample_data.csv` and saves them into an SQLite3 database named `sample.db`.

2. **answer_1.py**: How many users were active on a given day (they made a deposit or withdrawal).

3. **answer_2.py**: Identify users haven't made a deposit.

4. **answer_3.py**: Identify on a given day which users have made more than 5 deposits historically.

## Usage

1. Make sure you have Python installed on your system.
2. Run the `create_db.py` script to generate the SQLite3 database and load data from the CSV files.
   ```bash
   python create_db.py
   ```
3. Once the database is created, you can execute any of the `answer_x.py` scripts to perform SQL queries on the tables and obtain specific answers.

## CSV File Structure


The CSV files used to load data into the database must respect the names informed and be in the same folder path, if in another directory update it in the create_db.py file


- `deposit_sample_data.csv`: Contains deposit data.
- `withdrawals_sample_data.csv`: Contains withdrawal data.
- `event_sample_data.csv`: Contains event data.
- `user_id_sample_data.csv`: Contains user_id data.

## TO create a ETL process daily batches

If we need to create an ETL so that it automatically saves data, we can use the example insert_data_example.py and replicate for n tables.

## Requirements

- Python 3.x
- Python `sqlite3` library (comes included in the standard Python installation)
- Pandas

