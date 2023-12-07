#!/usr/bin/env python
# coding: utf-8

# In[171]:


import pandas as pd
import numpy as np


# In[172]:


df= pd.read_csv('adidassales.csv')


# In[173]:


df.head(5)


# In[174]:


df.info()


# In[175]:


# there is no null value
#invoice date should be in time frame

df['Invoice Date']= df['Invoice Date'].replace('/','-')
#change the format of date
df['Invoice Date']= pd.to_datetime(df['Invoice Date'])

# Price per Unit, Units Sold, Total Sales, Operating Profit should be float number
# drop $,. from Price per Unit and change data type to float

df[['Price per Unit','Total Sales', 'Operating Profit','Units Sold']] = df[['Price per Unit','Total Sales', 'Operating Profit','Units Sold']].replace('[\$,]', '', regex=True).astype(float)
df['Operating Margin']= df['Operating Margin'].str.replace('%','').astype(float)

df.info()
df.head()



# In[179]:


##the value_counts()function helps to count distinct values in the specified years
df['Invoice Date'].dt.year.value_counts() 

