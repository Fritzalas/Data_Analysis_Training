#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# URL to the CSV file
url = "https://storage.googleapis.com/courses_data/Python%20Data/Data%20Analysis%20-%20Python%20Examples/weather_data.csv"

# Load the data into a DataFrame
weather_df = pd.read_csv(url)

# Display the first few rows of the DataFrame
print(weather_df)


# In[2]:


# Convert 'Date' column to datetime type
weather_df['date'] = pd.to_datetime(weather_df['date'])

# Extract the month from the 'Date' column
weather_df['month'] = weather_df['date'].dt.month
print(weather_df)


# In[4]:


# Calculating the average temperature for each day
weather_df["avg_temp"] = (weather_df["min_temp"] + weather_df["max_temp"]) / 2
print(weather_df)


# In[5]:


# Group by 'Month' and calculate the average temperature
average_temperature_by_month = weather_df.groupby('month')['avg_temp'].mean()

# Display the result
print(average_temperature_by_month)


# In[7]:


most_cold_month = weather_df.groupby('month')['avg_temp'].min()
print(most_cold_month)
most_hot_month = weather_df.groupby('month')['avg_temp'].max()
print(most_hot_month)


# In[15]:


# Create a histogram for the temperature distribution
plt.figure(figsize=(10, 6))
plt.hist(weather_df['avg_temp'], bins=20, color='blue', edgecolor='black')
plt.title('Temperature Distribution')
plt.xlabel('Temperature')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show()


# In[20]:


import seaborn as sns

# Create a distribution plot for the temperature
plt.figure(figsize=(10, 6))
sns.histplot(weather_df['avg_temp'], bins=20, color='blue', edgecolor='black', kde=True)
plt.title('Temperature Distribution with Seaborn')
plt.xlabel('Temperature')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show()


# In[ ]:




