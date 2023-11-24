#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# URL to the CSV file
url = "https://storage.googleapis.com/courses_data/Python%20Data/Data%20Analysis%20-%20Python%20Examples/air_quality_data.csv"

# Load the data into a DataFrame
air_quality_df = pd.read_csv(url)

# Display the first few rows of the DataFrame
print(air_quality_df)


# In[2]:


# Convert 'Date' column to datetime format
air_quality_df['date'] = pd.to_datetime(air_quality_df['date'])
print(air_quality_df)


# In[4]:


# Extract month and year columns
air_quality_df['Month'] = air_quality_df['date'].dt.month
air_quality_df['Year'] = air_quality_df['date'].dt.year
air_quality_df['Day'] = air_quality_df['date'].dt.day

# Display the DataFrame with the new columns
print(air_quality_df)


# In[6]:


# Group by 'City' and calculate the mean for a specific column, e.g., 'Value'
mean_value_by_city = air_quality_df.groupby('city')['pm25'].mean()

# Display the result
print(mean_value_by_city)


# In[7]:


# Function to calculate AQI based on PM2.5 concentration
def calculate_aqi_pm25(pm25):
    if pm25 <= 12:
        aqi = (50 - 0) / (12 - 0) * (pm25 - 0) + 0
    elif pm25 <= 35.4:
        aqi = (100 - 51) / (35.4 - 12.1) * (pm25 - 12.1) + 51
    else:
        aqi = 101
    return aqi

# Apply the function to the 'Value' column
air_quality_df['AQi'] = air_quality_df['pm25'].apply(calculate_aqi_pm25)

# Display the DataFrame with the new column
print(air_quality_df)


# In[8]:


# Group by 'City' and calculate the mean for a specific column, e.g., 'Value'
mean_value_by_city = air_quality_df.groupby('city')['AQi'].mean()

# Display the result
print(mean_value_by_city)


# In[9]:


# Select columns of interest
columns_of_interest = ['pm25', 'no2', 'so2', 'co', 'o3']
subset_df = air_quality_df[columns_of_interest]

# Calculate the correlation matrix
correlation_matrix = subset_df.corr()

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Matrix Heatmap')
plt.show()


# In[ ]:




