#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# URL to the CSV file
url = "https://storage.googleapis.com/courses_data/Python%20Data/Data%20Analysis%20-%20Python%20Examples/hospital_admissions_data.csv"

# Load the data into a DataFrame
hospital_df = pd.read_csv(url)

# Display the first few rows of the original DataFrame
print("Original DataFrame:")
print(hospital_df)


# In[3]:


# Convert the 'Admission_Date' column to datetime format
hospital_df['admission_date'] = pd.to_datetime(hospital_df['admission_date'])
hospital_df['discharge_date'] = pd.to_datetime(hospital_df['discharge_date'])
print(hospital_df)


# In[4]:


# Calculate the difference in days
hospital_df['Days_Difference'] = (hospital_df['discharge_date'] - hospital_df['admission_date']).dt.days
print(hospital_df)


# In[5]:


# Group by 'diagnosis' and calculate the mean for 'Days_Difference'
mean_days_difference_by_diagnosis = hospital_df.groupby('diagnosis')['Days_Difference'].mean()

# Display the result
print(mean_days_difference_by_diagnosis)


# In[8]:


counts_of_diagnosis=hospital_df.groupby('diagnosis')['diagnosis'].count()
print("Top-3 diagnosis:")
print(counts_of_diagnosis.head(3))


# In[9]:


# Create a histogram for the age distribution
plt.figure(figsize=(10, 6))
plt.hist(hospital_df['age'], bins=20, color='blue', edgecolor='black')
plt.title('Age Distribution of Patients')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show()


# In[13]:


# Create a histogram for the age distribution with seaborn
plt.figure(figsize=(10, 6))
sns.histplot(hospital_df['age'], bins=20, kde=True, color='blue',edgecolor='black')
plt.title('Age Distribution of Patients')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# In[ ]:




