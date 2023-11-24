#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import the necessary libraries and read the CSV file.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file
# URL to the CSV file
url = "https://storage.googleapis.com/courses_data/Python%20Data/Data%20Analysis%20-%20Python%20Examples/sales_data2.csv"

# Load the data into a DataFrame
df = pd.read_csv(url)

# Display the first few rows of the DataFrame
print(df)


# In[2]:


# Display the data types of each column
print(df.dtypes)


# In[3]:


# Check for missing values in the entire DataFrame
missing_values = df.isnull()

# Check for missing values in each column
column_missing_values = df.isnull().sum()

# Display the results
print("Missing values in the entire DataFrame:")
print(missing_values)

print("\nMissing values in each column:")
print(column_missing_values)


# In[4]:


# Create a new 'revenue' column
df['revenue'] = df['price'] * df['quantity']

# Display the updated DataFrame
print(df)


# In[6]:


# Calculate the sum of the 'revenue' column
total_revenue = df['revenue'].sum()

# Format total revenue as dollars
formatted_total_revenue = '${:,.2f}'.format(total_revenue)

# Display the total revenue
print(f'Total Revenue: {formatted_total_revenue}')


# In[16]:


# Group by 'order_id' and calculate the sum of 'price' for each group
total_price_by_order = df.groupby('order_id')['price'].sum().mean()

# Display the result
print(total_price_by_order)


# In[17]:


# Group by 'order_id' and calculate the sum of 'price' for each group
total_sales = df.groupby('product_id')['quantity'].sum()

# Display the result
print(total_sales)


# In[24]:


# Group by 'order_id' and calculate the sum of 'price' for each group
total_sales = df.groupby('product_id')['quantity'].sum()
# Sort the DataFrame in descending order based on the 'price' column
df_sorted = total_sales.sort_values( ascending=False)

# Display the sorted DataFrame
print(df_sorted.head(3))


# In[ ]:




