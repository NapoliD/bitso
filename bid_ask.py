import requests
import hmac
import hashlib
import time
import pandas as pd

#https://docs.bitso.com/bitso-api/docs/authentication
BITSO_API_KEY = "YOUR_API_KEY"  # Replace with your own API key
BITSO_API_SECRET = "YOUR_API_SECRET"  # Replace with your own API secret

OUTPUT_DIR = "data_lake"

# Function to fetch order book data for a given trading pair
def fetch_order_book(pair):
    nonce = str(int(time.time()))  # Generate a unique timestamp
    message = nonce + 'GET/api/v3/order_book?book=' + pair  # Construct the message for the request
    signature = hmac.new(BITSO_API_SECRET.encode(), message.encode(), hashlib.sha256).hexdigest()  # Generate the signature using HMAC-SHA256
    headers = {
        'Authorization': f'Bitso {BITSO_API_KEY}:{nonce}:{signature}',  # Construct the Authorization header
        'Content-Type': 'application/json'
    }
    response = requests.get(f'https://api.bitso.com/api/v3/order_book?book={pair}', headers=headers)  # Make the GET request
    return response.json()  # Return the response JSON

# Function to calculate the spread between best bid and best ask
def calculate_spread(order_book):
    best_bid = float(order_book['payload']['bids'][0]['price'])  # Get the best bid price
    best_ask = float(order_book['payload']['asks'][0]['price'])  # Get the best ask price
    spread = (best_ask - best_bid) * 100 / best_ask  # Calculate the spread percentage
    return spread  # Return the spread

# Function to write records to a CSV file
def write_to_csv(records, filename):
    csv_columns = ['timestamp', 'pair', 'bid', 'ask', 'spread']  # Define the CSV column names
    with open(filename, 'w', newline='') as f:  # Open the file for writing
        writer = csv.DictWriter(f, fieldnames=csv_columns)  # Create a CSV DictWriter object
        writer.writeheader()  # Write the CSV header
        writer.writerows(records)  # Write the records to the CSV file

# Function to continuously monitor order books for a given pair
def monitor_order_books(pair):
    records = []  # Initialize an empty list to store records
    start_time = time.time()  # Record the start time
    while True:
        current_time = time.time()  # Get the current time
        if current_time - start_time >= 600:  #approximately 10 minutes
            filename = f"{OUTPUT_DIR}/{pair}order_book{int(current_time)}.csv"  # Generate the filename with timestamp
            write_to_csv(records, filename)  # Write records to CSV
            print(f"File {filename} has been stored.")  # Print a message indicating the file has been stored
            start_time = current_time  # Update the start time
            records = []  # Clear the records list
        
        order_book = fetch_order_book(pair)  # Fetch the order book data
        spread = calculate_spread(order_book)  # Calculate the spread
        timestamp = int(time.time())  # Get the current timestamp
        records.append({  # Append the record to the records list
            'timestamp': timestamp,
            'pair': pair,
            'bid': order_book['payload']['bids'][0]['price'],
            'ask': order_book['payload']['asks'][0]['price'],
            'spread': spread
        })
        
        time.sleep(1)  # Wait for 1 second between iterations
