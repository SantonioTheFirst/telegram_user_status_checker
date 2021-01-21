#!/usr/bin/env python
# coding: utf-8

# In[131]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# get_ipython().run_line_magic('matplotlib', 'inline')


# In[132]:


data = pd.read_csv('data.csv', header = 0, sep = ';')


# In[147]:


data.head()


# In[148]:


data.describe()


# In[149]:


data.info()


# In[150]:


data['Was_online_1'] = data['Was_online_1'].apply(pd.to_datetime)
data['Was_online_2'] = data['Was_online_2'].apply(pd.to_datetime)
data['time'] = data['time'].apply(pd.to_datetime)


# In[151]:


data.info()


# In[152]:


plt.plot(data['time'], data['User_1'], color = 'red')
plt.plot(data['time'], data['User_2'], color = 'blue')
plt.show()


# In[153]:


plt.scatter(data['time'], data['User_1'])
plt.scatter(data['time'], data['User_2'])
plt.show()


# In[154]:


plt.hist(data[data['User_1'] == 1]['time'])
plt.show()


# In[155]:


sns.heatmap(data.drop('ID', axis = 1).corr(), annot = True)
plt.show()
