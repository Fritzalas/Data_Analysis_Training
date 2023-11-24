#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data into a DataFrame
# URL to the CSV file
url = "https://storage.googleapis.com/courses_data/Python%20Data/Data%20Analysis%20-%20Python%20Examples/movies.csv"

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


# Remove any rows with missing values
df.dropna(inplace=True)
print(df)


# In[5]:


# Convert 'budget' and 'revenue' columns to numeric
df['budget'] = pd.to_numeric(df['budget'], errors='coerce')
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
# Check data types to verify the conversion
print("\nData types after conversion:")
print(df.dtypes)


# In[6]:


# Create a new column profit
df['profit'] = df['revenue'] - df['budget']
print(df)


# In[7]:


# Calculate summary statistics
summary_stats = df[['budget', 'revenue', 'profit']].describe()

# Display the summary statistics
print(summary_stats)


# In[9]:


# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(df['profit'], bins=20, color='blue', edgecolor='black')
plt.title('Histogram of Profit')
plt.xlabel('Profit')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show()


# In[10]:


# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['budget'], df['revenue'], color='green', alpha=0.5)
plt.title('Scatter Plot of Budget vs Revenue')
plt.xlabel('Budget')
plt.ylabel('Revenue')
plt.grid(True)
plt.show()


# In[ ]:




