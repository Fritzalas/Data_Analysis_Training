#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
column_names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
df = pd.read_csv(url, names=column_names, delim_whitespace=True)
print(df)


# In[3]:


# Check for null values in the entire DataFrame
null_values = df.isnull().sum()

# Display the result
print(null_values)


# In[4]:


# Display the variable types for each column
variable_types = df.dtypes

# Display the result
print(variable_types)


# In[5]:


# Replace "?" with NaN in the specified column
df['horsepower'] = df['horsepower'].replace('?', np.nan)

# Display the DataFrame after replacement
print(df)


# In[6]:


# Display the variable types for each column
variable_types = df.dtypes

# Display the result
print(variable_types)


# In[7]:


df['horsepower'] = df['horsepower'].astype(float)
# Display the variable types for each column
variable_types = df.dtypes

# Display the result
print(variable_types)


# In[8]:


df.dropna(inplace=True)
print(df)


# In[9]:


plt.scatter(df['weight'], df['mpg'])
plt.xlabel('Weight')
plt.ylabel('Miles Per Gallon')
plt.title('Weight vs. MPG')
plt.show()


# In[ ]:




