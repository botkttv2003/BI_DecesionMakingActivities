import csv

# Function to compare the values of the "no_of_ratings" and "profit" columns
def compare_columns(filename):
    count = 0

    with open(filename, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        no_of_ratings_index = header.index("no_of_ratings")
        profit_index = header.index("profit")

        # Read the first row
        prev_row = next(reader)
        prev_no_of_ratings = int(float(prev_row[no_of_ratings_index]))
        prev_profit = int(prev_row[profit_index])

        # Iterate through the remaining rows in the CSV file
        for row in reader:
            current_no_of_ratings = int(float(row[no_of_ratings_index]))
            current_profit = int(row[profit_index])

             # Compare the values of the "no_of_ratings" and "profit" columns for two rows
            if abs(current_no_of_ratings - prev_no_of_ratings) <= 100 or current_no_of_ratings == prev_no_of_ratings:
                if abs(current_profit - prev_profit) <= 100 or current_profit == prev_profit:
                    count += 1

            # Update the previous row
            prev_row = row
            prev_no_of_ratings = current_no_of_ratings
            prev_profit = current_profit

    return count

# Create a list of CSV files you want to compare
filenames = ['new_data_1.csv', 'new_data_2.csv', 'new_data_3.csv', 'new_data_4.csv', 'new_data_5.csv','new_data_6.csv', 'new_data_7.csv', 'new_data_8.csv','new_data_9.csv','new_data_10.csv']

# Initialize variables to store the filename with the highest count value and the corresponding count value
max_count_filename = None
max_count = float('-inf')

# Iterate through each file and calculate the count value
for filename in filenames:
    count = compare_columns(filename)

    # Compare with the current highest count value
    if count > max_count:
        max_count = count
        max_count_filename = filename

# In ra tên tệp có giá trị count cao nhất
print(f"Tệp có giá trị profit hợp lý nhất là '{max_count_filename}'")

