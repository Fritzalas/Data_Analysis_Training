#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# URL to the CSV file
url = "https://storage.googleapis.com/courses_data/Python%20Data/Data%20Analysis%20-%20Python%20Examples/sports_betting_data.csv"

# Load the data into a DataFrame
sports_betting_df = pd.read_csv(url)

# Display the first few rows of the DataFrame
print(sports_betting_df)


# In[5]:


# Convert 'Date' column to datetime format
sports_betting_df['event_date'] = pd.to_datetime(sports_betting_df['event_date'])

# Extract month and year columns
sports_betting_df['Month'] = sports_betting_df['event_date'].dt.month
sports_betting_df['Year'] = sports_betting_df['event_date'].dt.year
print(sports_betting_df)


# In[7]:


# Filter the DataFrame to include only rows where 'win' is present
win_df = sports_betting_df[sports_betting_df['bet_outcome'] == 'win']

# Group by 'bet_type' and count occurrences of 'win'
win_counts_by_bet_type = win_df.groupby('bet_type').size()

# Display the result
print(win_counts_by_bet_type)


# In[8]:


# Group by 'bet_type' and count occurrences of 'win'
counts_by_bet_type = sports_betting_df.groupby('bet_type').size()
# Display the result
print(counts_by_bet_type)


# In[9]:


# Element-wise division
result_df = win_counts_by_bet_type / counts_by_bet_type

# Display the result
print(result_df)


# In[10]:


# Filter the DataFrame to include only rows where 'win' is present
win_df = sports_betting_df[sports_betting_df['bet_outcome'] == 'win']
print(win_df)


# In[34]:


# Use .loc to assign values without triggering the warning
win_df.loc[:, 'betting_return'] = ((win_df['odds']-1) * (win_df['bet_amount']))
print(win_df)


# In[35]:


# Group by 'bet_type' and count occurrences of 'win'
win_counts_by_bet_type = win_df.groupby('bet_type')['betting_return'].sum().reset_index()

# Display the result
print(win_counts_by_bet_type)


# In[36]:


# Filter the DataFrame to include only rows where 'loss' is present
loss_df = sports_betting_df[sports_betting_df['bet_outcome'] == 'loss']
print(loss_df)


# In[38]:


# Use .loc to assign values without triggering the warning
loss_df.loc[:, 'betting_return'] =  (-loss_df['bet_amount'])
print(loss_df)


# In[39]:


# Group by 'bet_type' and count occurrences of 'win'
loss_counts_by_bet_type = loss_df.groupby('bet_type')['betting_return'].sum().reset_index()

# Display the result
print(loss_counts_by_bet_type)


# In[41]:


print(loss_counts_by_bet_type['betting_return']+win_counts_by_bet_type['betting_return'])


# In[42]:


# Filter the winning bets
winning_bets = sports_betting_df[sports_betting_df['bet_outcome'] == 'win']
# Set up the histogram
plt.hist(winning_bets['odds'], bins=20, edgecolor='black')
plt.xlabel("Odds")
plt.ylabel("Frequency")
plt.title("Distribution of Winning Odds")
# Display the histogram
plt.show()


# In[ ]:




