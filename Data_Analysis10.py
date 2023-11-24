#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math

# URL of the CSV file
url = "https://storage.googleapis.com/courses_data/Python%20Data/Data%20Analysis%20-%20Python%20Examples/vgsales.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(url)

# Display the first few rows of the DataFrame
print(df)


# In[43]:


# Check the data types of each column in the DataFrame
data_types = df.dtypes

# Display the data types
print(data_types)


# In[44]:


# Check for missing values in the DataFrame
missing_values = df.isnull().sum()

# Display the number of missing values for each column
print(missing_values)
# drop rows with missing values
df.dropna(inplace=True)
print(df)


# In[45]:


# Group by "Name" and sum the global sales
sales_by_name = df.groupby("Name")["Global_Sales"].sum()

# Display the result
print(sales_by_name)


# In[46]:


# Sort the DataFrame by "Total_Global_Sales" in descending order
sales_by_name_df_sorted = sales_by_name.sort_values(ascending=False)

# Display the sorted DataFrame
print(sales_by_name_df_sorted.head(10))


# In[47]:


# Group by "Platform" and count the occurrences
platform_counts = df.groupby("Platform")["Global_Sales"].sum()

# Display the result
print(platform_counts)


# In[48]:


platform_counts.sort_values(ascending=False,inplace=True)
print(platform_counts)


# In[49]:


# Group by "Genre" and count the occurrences
genre_counts = df.groupby("Genre")["Global_Sales"].sum()

# Display the result
print(genre_counts)


# In[50]:


genre_counts.sort_values(ascending=False,inplace=True)
print(genre_counts)


# In[51]:


# Specify the columns you want to sum
columns_to_sum = ["NA_Sales", "EU_Sales", "JP_Sales","Other_Sales"]

# Sum the values across the specified columns
sum_of_columns = df[columns_to_sum].sum()

# Display the result
print(sum_of_columns)


# In[52]:


# Plotting the bar chart
# Plotting the bar chart
ax = sum_of_columns.plot(kind='bar', color='skyblue', edgecolor='black')

# Adding grid
ax.yaxis.grid(True, linestyle='--', which='major', color='gray', alpha=0.7)


# Adding labels and title
plt.xlabel('Columns')
plt.ylabel('Sum')
plt.title('Sum of Values Across Columns')

# Display the plot
plt.show()


# In[53]:


import matplotlib.pyplot as plt

# Scatter plot
plt.scatter(df['Year'], df['Global_Sales'])

# Adding labels and title
plt.xlabel('Year of Release')
plt.ylabel('Global Sales ')
plt.title('Relationship Between Year of Release and Global Sales')

# Display the plot
plt.show()


# In[54]:


# group data by publisher and sum global sales
publisher_sales = df.groupby('Publisher')['Global_Sales'].sum()
# sort by global sales
publisher_sales = publisher_sales.sort_values(ascending=False)
# create a bar chart showing top publishers by global sales
publisher_sales.head(10).plot(kind='bar')
plt.title('Top Publishers by Global Sales')
plt.xlabel('Publisher')
plt.ylabel('Global Sales (millions)')
plt.show()


# In[55]:


# calculate mean and variance of global sales data
mean_sales = df['Global_Sales'].mean()
var_sales = df['Global_Sales'].var()

# calculate expected mean and variance of Poisson distribution
exp_mean = mean_sales
exp_var = var_sales

# compare mean and variance to expected values for Poisson distribution
print('Mean of global sales data:', mean_sales)
print('Variance of global sales data:', var_sales)
print('Expected mean of Poisson distribution:', exp_mean)
print('Expected variance of Poisson distribution:', exp_var)


# In[56]:


def poisson_probability(k, lam):
    return (lam ** k) * math.exp(-lam) / math.gamma(k + 1)

# compute the mean of the global sales data
mean_sales = np.mean(df['Global_Sales'])
# generate a histogram of the global sales data
n, bins, patches = plt.hist(df['Global_Sales'], bins=50, density=True, alpha=0.5)
# calculate the Poisson distribution for the mean
poisson_dist = [poisson_probability(b, mean_sales) for b in bins]
# plot the Poisson distribution over the histogram
plt.plot(bins, poisson_dist, 'r-', linewidth=2)
# label the plot
plt.title('Global Sales Data and Poisson Distribution')
plt.xlabel('Global Sales (millions)')
plt.ylabel('Probability')


# In[ ]:




