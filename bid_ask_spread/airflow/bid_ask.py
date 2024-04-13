import requests
import hmac
import hashlib
import time
import pandas as pd
import csv
import boto3


#https://docs.bitso.com/bitso-api/docs/authentication
BITSO_API_KEY = "YOUR_API_KEY"  # Replace with your own API key
BITSO_API_SECRET = "YOUR_API_SECRET"  # Replace with your own API secret

AWS_ACCESS_KEY_ID = "YOUR_AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY = "YOUR_AWS_SECRET_ACCESS_KEY"
S3_BUCKET_NAME = "your-s3-bucket-name"

OUTPUT_DIR = "data_lake"

# Function to fetch order book data for a given trading pair
def fetch_order_book(pair):
    try:
        nonce = str(int(time.time()))  # Generate a unique timestamp
        message = nonce + 'GET/api/v3/order_book?book=' + pair  # Construct the message for the request
        signature = hmac.new(BITSO_API_SECRET.encode(), message.encode(), hashlib.sha256).hexdigest()  # Generate the signature using HMAC-SHA256
        headers = {
            'Authorization': f'Bitso {BITSO_API_KEY}:{nonce}:{signature}',  # Construct the Authorization header
            'Content-Type': 'application/json'
        }
        response = requests.get(f'https://api.bitso.com/api/v3/order_book?book={pair}', headers=headers)  # Make the GET request
        response.raise_for_status()  # Raise an exception if the request was not successful
        return response.json()  # Return the response JSON
    except requests.exceptions.RequestException as e:
        print(f"Error fetching order book for {pair}: {e}")
        return None

# Function to calculate the spread between best bid and best ask
def calculate_spread(order_book):
    try:
        best_bid = float(order_book['payload']['bids'][0]['price'])  # Get the best bid price
        best_ask = float(order_book['payload']['asks'][0]['price'])  # Get the best ask price
        spread = (best_ask - best_bid) * 100 / best_ask  # Calculate the spread percentage
        return spread  # Return the spread
    except (KeyError, IndexError, ValueError) as e:
        print(f"Error calculating spread: {e}")
        return None

# Function to write records to a CSV file
def write_to_csv(records, filename):
    csv_columns = ['timestamp', 'pair', 'bid', 'ask', 'spread']  # Define the CSV column names
    try:
        with open(filename, 'w', newline='') as f:  # Open the file for writing
            writer = csv.DictWriter(f, fieldnames=csv_columns)  # Create a CSV DictWriter object
            writer.writeheader()  # Write the CSV header
            writer.writerows(records)  # Write the records to the CSV file
    except IOError as e:
        print(f"Error writing to CSV file {filename}: {e}")

# Function to send alerts if spread exceeds custom thresholds
def send_alert(pair, spread, thresholds):
    for threshold in thresholds:
        if spread > threshold:
            return print(f"Alert: The spread for pair {pair} has exceeded {threshold}%")

def save_to_s3(records, filename):
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )
    try:
        s3.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=filename,
            Body=records
        )
        print(f"Archivo guardado en S3: {filename}")
    except Exception as e:
        print(f"Error al guardar archivo en S3: {e}")

# Function to continuously monitor order books for a given pair
def monitor_order_books(pair):
    records = []  # Initialize an empty list to store records
    start_time = time.time()  # Record the start time
    thresholds = [1.0, 0.5, 0.1]  # Custom thresholds for the spread percentage
    while True:
        current_time = time.time()  # Get the current time
        if current_time - start_time >= 5:  # Check if 50 seconds have elapsed (approximately 10 minutes)
            filename = f"{OUTPUT_DIR}/{pair}order_book{int(current_time)}.csv"  # Generate the filename with timestamp
            write_to_csv(records, filename)  # Write records to CSV
            # save_to_s3(csv_data, filename) # Write records to s3
            print(f"File {filename} has been stored.")  # Print a message indicating the file has been stored
            start_time = current_time  # Update the start time
            records = []  # Clear the records list
        
        order_book = fetch_order_book(pair)  # Fetch the order book data
        if order_book is not None:
            spread = calculate_spread(order_book)  # Calculate the spread
            if spread is not None:
                timestamp = int(time.time())  # Get the current timestamp
                records.append({  # Append the record to the records list
                    'timestamp': timestamp,
                    'pair': pair,
                    'bid': order_book['payload']['bids'][0]['price'],
                    'ask': order_book['payload']['asks'][0]['price'],
                    'spread': spread
                })
                send_alert(pair, spread, thresholds)  # Check if the spread exceeds any custom thresholds
        
        time.sleep(1)
