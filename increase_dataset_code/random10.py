import csv
import random

# Read the list of cities from an existing file
with open('us_cities.txt', 'r') as city_file:
    cities = [line.strip() for line in city_file]

# Iterate 10 times to create 10 different CSV files
for i in range(10):
    # Create a new file name based on the iteration number
    new_csv_filename = f'new_data_{i+1}.csv'

    # Open the original CSV file and create a new file for writing data with additional columns
    with open('dataset_newv2.csv', 'r', encoding='utf-8') as original_csv, open(new_csv_filename, 'w', newline='', encoding='utf-8') as new_csv:
        reader = csv.reader(original_csv)
        writer = csv.writer(new_csv)

        # Read the header from the original CSV file and add two new headers
        header = next(reader)
        header.extend(["profit", "city"])
        writer.writerow(header)

        # Read each data row from the original CSV file, add random profit and city values
        for row in reader:
            profit = random.randint(1, 5000)
            city = random.choice(cities)

            # Handle invalid characters in the data
            row = [cell.replace('\ufffd', '') for cell in row]

            row.extend([profit, city])
            writer.writerow(row)

    print(f"Created a new file '{new_csv_filename}' with 2 columns: profit and city.")
