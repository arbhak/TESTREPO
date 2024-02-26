#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Pandas is a software library written for the Python programming language for data manipulation and analysis.
import pandas as pd
#NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
import numpy as np


# In[2]:


df=pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_1.csv")
df.head(10)


# In[3]:


df.isnull().sum()/len(df)*100


# In[4]:


df.dtypes


# In[5]:


# Calculating the total no launches on each site 
launch_site_counts = df['LaunchSite'].value_counts()
print(launch_site_counts)


# In[9]:


#Calculate the number and occurrence of each orbit
orbit_counts = df['Orbit'].value_counts()
print(orbit_counts)



# In[10]:


# Calculate the number and occurence of mission outcome of the orbits
landing_outcomes = df['Outcome'].value_counts()
print(landing_outcomes)


# In[12]:


### Create a landing outcome label from Outcome column
bad_outcome = {'failure', 'precluded', 'partial failure'}

landing_class = df['Outcome'].apply(lambda x: 0 if x in bad_outcome else 1).tolist()


# In[13]:


df['Class']=landing_class
df[['Class']].head(8)


# In[14]:


df.head(5)


# In[15]:


df["Class"].mean()


# In[ ]:




