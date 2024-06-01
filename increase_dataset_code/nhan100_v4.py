import dask.dataframe as dd
import pandas as pd
import random

# Read data from the original CSV file using Dask
ddf = dd.read_csv('new_data_8.csv')

# Get the last "id" value from the original data
last_id = ddf['id'].max().compute()

# Multiply the data table by 100 times
ddf_multiplied = dd.concat([ddf] * 100, ignore_index=True)

# Randomly assign values to the "profit" column within the range from min_profit to max_profit
min_profit = 5  # Minimum value for the "profit" column
max_profit = 5000  # Maximum value for the "profit" column
ddf_multiplied['profit'] = ddf_multiplied['profit'].apply(lambda x: random.uniform(min_profit, max_profit), meta=('profit', 'f8'))

# Update the "id" column to continue from the last value of the original data
ddf_multiplied['id'] = ddf_multiplied['id'] + last_id + 1

# Create a dictionary to track the "id_by_category" value for each "main_category"
id_by_category_mapping = {}

# Update the "id_by_category" column based on the "main_category" to ensure unique values
def update_id_by_category(row):
    main_category = row['main_category']
    if main_category not in id_by_category_mapping:
        id_by_category_mapping[main_category] = 1
    else:
        id_by_category_mapping[main_category] += 1
    return id_by_category_mapping[main_category]

ddf_multiplied['id_by_category'] = ddf_multiplied.apply(update_id_by_category, axis=1, meta=('id_by_category', 'i8'))

# Save the resulting data table to a new CSV file using Dask
ddf_multiplied.to_csv('dulieu_100.csv', index=False, single_file=True)

# Read the original data and save it to a new data table using Dask
ddf_old = dd.read_csv('new_data_8.csv')

# Multiply the data table by 100 times (including both old and new data) using Dask
ddf_combined = dd.concat([ddf_old, ddf_multiplied], ignore_index=True)

# Save the new data table (including both old and new data) to a new CSV file using Dask
ddf_combined.to_csv('dulieu_100_v1.csv', index=False, single_file=True)
