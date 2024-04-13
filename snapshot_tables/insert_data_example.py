import sqlite3
import pandas as pd

# Connect to the SQLite database (will create a new one if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor
cursor = conn.cursor()

# Define the table schema
create_table_query = '''
    CREATE TABLE IF NOT EXISTS event_sample_data (
        id INTEGER PRIMARY KEY,
        event_timestamp TIMESTAMP,
        user_id TEXT,
        event_name TEXT
    )
'''

# Execute the query to create the table
cursor.execute(create_table_query)

# Read data from the CSV file
data = pd.read_csv('event_sample_data.csv')
data['event_timestamp'] = pd.to_datetime(data['event_timestamp'])

# Prepare data for insertion
records_to_insert = data.to_records(index=False)

# Insert data into the table using executemany
insert_query = "INSERT INTO event_sample_data (id, event_timestamp, user_id, event_name) VALUES (?, ?, ?, ?)"
cursor.executemany(insert_query, records_to_insert)

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()
