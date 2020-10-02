#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[9]:


# Create the bin dividers
bins = [0, 60, 70, 80, 90, 100]
# Create names for the four groups
group_names = ['F', 'D', 'C', 'B', 'A']


# In[10]:


df['lettergrade'] = pd.cut(df['grade'], bins, labels=group_names)
df


# In[11]:


pd.value_counts(df['lettergrade'])


# In[12]:


bins = [ 80, 90, 100]
group_names = ['B', 'A']
df['Master'] = pd.cut(df['grade'], bins, labels=group_names)
df.head()


# In[13]:


df['Master'] = pd.cut(df['grade'], bins, labels=group_names)
df


# In[ ]:




