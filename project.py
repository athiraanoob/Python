import pandas as pd
import numpy as np
import statistics

url = 'C:\\Users\\athir\\OneDrive\\Documents\\Athira Doc\\Airbnb_Open_Data.csv'
data = pd.read_csv(url)
print(f"length of data before dropping duplicates{len(data)}")
# print(data['price'].isnull().any())
# average= statistics.mean(data['price'])
# data['price'].replace(" ",average)
print(data['availability 365'].isnull().any())
columns_to_remove = ['host_identity_verified', 'lat', 'long', 'instant_bookable', 'Construction year', 'minimum nights',
                     'number of reviews', 'last review', 'reviews per month', 'calculated host listings count',
                     'license']
data.drop(columns=columns_to_remove, inplace=True)
data.drop_duplicates(inplace=True)
print(f"length of data after dropping duplicates {len(data)}")
column_name = 'id'
duplicates = data.duplicated(subset=column_name)
print(duplicates.any())
if duplicates.any():
    duplicated_rows = data[data.duplicated(subset=column_name, keep=False)]
    print("Duplicated rows:")
    print(len(duplicated_rows))
else:
    print("No duplicates found.")
data_types = data.dtypes
print(data_types)
data.dropna()
print(len(data))
data_price = data['price'].copy()
number = data_price.str.lstrip('$')
n1 = pd.to_numeric(number, errors='coerce')
# n1=number(int)
average = round(n1.mean(), 2)
number1 = str(average)
new_price = '$' + number1
print(new_price)
data['price'] = data['price'].fillna(average)
print(data['price'].isnull().any())

for i, j in zip(data['country'], data['country code']):
    if i == 'United States' and j != 'US':
        data['country code'] = 'US'
    # print(i,j)
    if i != 'United States' and j == 'US':
        # print(i,j)
        data['country'] = 'United States'

# print(data[data['country code'].isnull()])
# print(data['country'].head(200),data['country code'].head(200))
# data.columns=data.iloc[0]
# data=data[1:]
# data.reset_index(drop=True, inplace=True)
data.columns = data.columns.str.upper()
print(data)
