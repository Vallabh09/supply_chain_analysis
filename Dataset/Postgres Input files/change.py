# Import necessary libraries
import pandas as pd

# Load the uploaded CSV file to inspect the data
file_path = 'fact_order_line.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the data to understand its structure
data.head()

# Convert the 'order_placement_date' column to the desired format (yyyy-mm-dd)
data['order_placement_date'] = pd.to_datetime(data['order_placement_date'], format='%d-%m-%Y').dt.strftime('%Y-%m-%d')
data['agreed_delivery_date'] = pd.to_datetime(data['agreed_delivery_date'], format='%d-%m-%Y').dt.strftime('%Y-%m-%d')
data['actual_delivery_date'] = pd.to_datetime(data['actual_delivery_date'], format='%d-%m-%Y').dt.strftime('%Y-%m-%d')

# Save the updated file to review changes
updated_file_path = 'fact_aggregate_updated.csv'
data.to_csv(updated_file_path, index=False)

