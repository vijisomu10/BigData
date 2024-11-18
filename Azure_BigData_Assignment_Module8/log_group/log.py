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

# Function to generate a random date and time in a given year
def random_datetime_in_year(year):
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)
    
    # Generate random date
    delta_days = (end_date - start_date).days
    random_days = random.randint(0, delta_days)
    random_date = start_date + timedelta(days=random_days)
    
    # Generate random time
    random_time = random_time_in_range()
    
    # Combine date and time
    return random_date.replace(hour=random_time[0], minute=random_time[1], second=random_time[2])

# Function to generate a random time
def random_time_in_range():
    return (random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))


# Function to simulate log entries for each year from 1982 to 2015
def generate_fake_logs(num_entries_per_year=100):
    for year in range(1982, 2016):
        for _ in range(num_entries_per_year):
            log_level = random.choice(log_levels)
            log_message = random.choice(log_messages)
            log_date = random_datetime_in_year(year)

            # Create the log entry with the random date
            log_entry = f"{log_date} - {log_level} {log_message}"

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
    generate_fake_logs(100)  # Generate 100 log entries for each year

print(f"Fake log file '{log_file_path}' generated successfully!")
