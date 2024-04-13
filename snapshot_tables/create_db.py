import pandas as pd
import sqlite3


# Step 1: Extract - Read data from CSV files
deposit_data = pd.read_csv('deposit_sample_data.csv')
withdrawal_data = pd.read_csv('withdrawals_sample_data.csv')
event_data = pd.read_csv('event_sample_data.csv')
user_id_sample_data = pd.read_csv('user_id_sample_data.csv')

# Step 2: Transform - Convert event_timestamp to datetime
deposit_data['event_timestamp'] = pd.to_datetime(deposit_data['event_timestamp'])
withdrawal_data['event_timestamp'] = pd.to_datetime(withdrawal_data['event_timestamp'])
event_data['event_timestamp'] = pd.to_datetime(event_data['event_timestamp'])

# Step 3: Load - Store data in SQLite database
conn = sqlite3.connect('data.db')

# Write data to SQLite tables
deposit_data.to_sql('deposits', conn, if_exists='replace', index=False)
withdrawal_data.to_sql('withdrawal', conn, if_exists='replace', index=False)
event_data.to_sql('events', conn, if_exists='replace', index=False)
user_id_sample_data.to_sql('user_id', conn, if_exists='replace', index=False)

# Close connection
conn.close()