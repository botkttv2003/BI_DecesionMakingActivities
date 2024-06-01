import pandas as pd

# Read data
data = pd.read_csv(r"G:\University\BI\Mid-project\midterm-dataset - Copy\dataset\dataset_full.csv")

# View information of dataset
data.info()

#View the first 5 rows of the data set
data.head()


# Check duplicated rows
if data.duplicated().sum() > 0:
    # Delete duplicated rows
    data = data.drop_duplicates()
    print("Sum of duplicated rows deleted : ", data.duplicated().sum())

# Convert the 'no_of_ratings' column to integers
data['no_of_ratings'] = data['no_of_ratings'].str.replace(',', '', regex=True)
data['no_of_ratings'] = pd.to_numeric(data['no_of_ratings'], errors='coerce')

# Convert the 'ratings' column to float64, but replace invalid values with NaN
data['ratings'] = pd.to_numeric(data['ratings'], errors='coerce')

# Calculate the mean rating excluding NaN values
mean_rating = data['ratings'].mean()

# Replace NaN values with the mean rating
data['ratings'].fillna(mean_rating, inplace=True)

# Check for rows where 'ratings' couldn't be converted to float
invalid_ratings = data[data['ratings'].isna()]


# Change type value for price columns
data['actual_price'] = data['actual_price'].str.replace("₹", '').str.replace(",", '')
data['discount_price'] = data['discount_price'].str.replace("₹", '').str.replace(",", '')
data['actual_price'] = data['actual_price'].astype('float64')
data['discount_price'] = data['discount_price'].astype('float64')

# Mean of actual_price
mean_actual_price = data['actual_price'].mean()
# Replace NaN with the average value
data['actual_price'].fillna(mean_actual_price, inplace=True)

# Mean discount_price
mean_discount_price = data['discount_price'].mean()
# Replace NaN with the average value
data['discount_price'].fillna(mean_discount_price, inplace=True)

# Calculate the average value (mean) of the no_of_ratings column, eliminating NaN
mean_no_of_ratings = data['no_of_ratings'].mean()

# Replace NaN with the average value
data['no_of_ratings'].fillna(mean_no_of_ratings, inplace=True)

# Save
data.to_csv('dataset_newv2.csv', index=False)
