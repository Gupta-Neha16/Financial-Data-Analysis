#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
color = sns.color_palette()
import sklearn.metrics as metrics
import warnings
warnings.filterwarnings("ignore")


# In[48]:


data =pd.read_csv('/Users/gup9905/Desktop/Default.csv')


# In[49]:


data.columns


# In[ ]:





# In[7]:


data.head()


# In[9]:


data.shape


# In[10]:


data.describe()


# In[20]:


plt.figure(figsize = (15,8))
plt.subplot(1,2,1)
sns.boxplot(y = data['balance'])

plt.subplot(1,2,2)
sns.boxplot(y = data['income'])
plt.show()


# In[19]:


plt.figure(figsize = (20,8))
plt.subplot(1,2,1)
sns.countplot(data['student'])

plt.subplot(1,2,2)
sns.countplot(data['default'])
plt.show()


# In[21]:


data["student"].value_counts()


# In[22]:


data["default"].value_counts()


# In[24]:


data["student"].value_counts(normalize=True)


# In[27]:


plt.figure(figsize = (15,8))
plt.subplot(1,2,1)
sns.boxplot(data['default'], data['balance'])

plt.subplot(1,2,2)
sns.boxplot(data['default'], data['income'])
plt.show()


# In[28]:


pd.crosstab(data['student'], data['default'], normalize ='index').round(2)


# In[33]:


data.isnull().sum()


# In[37]:


A1, A3 = data['balance'].quantile([.25,.75])
IQR = A3 - A1
LL = A1 - 1.5*(IQR)
UL = A3 + 1.5*(IQR)


# In[38]:


fd = data[data['balance'] > UL]


# In[39]:


fd['default'].count()


# In[41]:


fd['default'].value_counts(normalize = True)


# In[45]:


data['balance'] = np.where(data['balance'] > UL, UL, data['balance'])


# In[47]:


sns.boxplot(y = data['balance'])
plt.show()

