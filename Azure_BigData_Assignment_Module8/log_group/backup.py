import pandas as pd
import logging
import random
from datetime import datetime, timedelta

# File path for the uploaded CSV file
csv_file_path = 'car_prices.csv'

# Set up logging configuration to generate the log file
log_file_path = 'fake_car_prices_log_1982_2015.log'
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(message)s',  # Changed to log only the message
)

# Define possible log levels and messages
log_levels = ['INFO', 'WARNING', 'ERROR', 'DEBUG']
log_messages = [
    "File uploaded successfully.",
    "Data processing started.",
    "Missing data in the 'price' column.",
    "User logged in.",
    "User logged out.",
    "Connection established.",
    "File downloaded successfully.",
    "Processing completed.",
    "Low disk space warning.",
    "Out of memory error.",
    "File not found.",
    "Data validation successful.",
    "System rebooted.",
    "Connection timed out.",
    "Record updated in the database.",
    "Transaction successful.",
    "Error while processing payment.",
    "User registration completed.",
    "System performance metrics logged.",
    "Backup completed successfully.",
]

# Function to generate a random date between 1982 and 2015
def random_date(start_year=1982, end_year=2015):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# Function to simulate log entries
def generate_fake_logs(num_entries=1000):
    for _ in range(num_entries):
        log_level = random.choice(log_levels)
        log_message = random.choice(log_messages)
        log_date = random_date(1982, 2015)

        # Create the log entry with the random date
        log_entry = f"{log_date} - {log_message}"

        # Log the entry based on the chosen level
        if log_level == 'INFO':
            logging.info(log_entry)
        elif log_level == 'WARNING':
            logging.warning(log_entry)
        elif log_level == 'ERROR':
            logging.error(log_entry)
        elif log_level == 'DEBUG':
            logging.debug(log_entry)

# Main function
if __name__ == "__main__":
    # Load the CSV file to check its contents (optional)
    df = pd.read_csv(csv_file_path)
    print(df.head())  # Display the first few rows of the dataframe for inspection
    generate_fake_logs(1000)  # Generate 1000 log entries

print(f"Fake log file '{log_file_path}' generated successfully!")
