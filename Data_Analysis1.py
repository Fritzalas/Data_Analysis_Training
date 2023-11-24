#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://storage.googleapis.com/courses_data/Python%20Data/Data%20Analysis%20-%20Python%20Examples/sales_data1.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(url)

# Display the DataFrame
print(df)


# In[7]:


# Check for missing data
missing_data = df.isnull().sum()

# Display the count of missing values for each column
print("Missing Data:")
print(missing_data)

# Παρατηρούμε στο Παραπάνω Dataset δεν έχουμε κάποια missing value
# In[8]:


# Convert the 'date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Check the data types after conversion
print("\nAfter conversion:")
print(df)


# In[12]:


# Add a day of the week column
df["Day_of_Week"] = df['Date'].dt.day_name()
print(df)


# In[14]:


# Check the summary statistics
print("\nSummary Statistics:\n", df.describe())


# In[18]:


# Group by 'product' and calculate the total revenue and quantity for each product
product_summary = df.groupby('Product').agg({'Revenue': 'sum', 'Quantity': 'sum'}).reset_index()

# Display the total revenue and quantity for each product
print(product_summary)


# In[27]:


# Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(product_summary['Product'], product_summary['Revenue'], color='skyblue')
plt.xlabel('Product')
plt.ylabel('Total Revenue')
plt.title('Total Revenue by Product')
# Annotate the product with the biggest revenue
max_revenue_index = product_summary[product_summary['Product'] == max_revenue_product].index[0]


plt.annotate(f'Max Revenue\n{max_revenue_product}: ${max_revenue:.2f}',
             xy=(max_revenue_index, max_revenue),
             xytext=(10, 20),
             textcoords='offset points',
             arrowprops=dict(facecolor='red', arrowstyle='wedge,tail_width=0.7', alpha=0.5))


# Show the plot
plt.tight_layout()
plt.show()


# In[ ]:




