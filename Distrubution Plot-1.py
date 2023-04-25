#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


tips= sns.load_dataset('tips')


# In[3]:


tips.head()


# In[4]:


tips.info()


# #Displot

# In[9]:


sns.distplot(tips['total_bill'],color="red")


# In[13]:


sns.distplot(tips["total_bill"],kde=False,bins=30) 
#kde= true to make the curve visible


# In[16]:


sns.jointplot(x="total_bill",y='tip',data=tips,kind='scatter')


# In[17]:


sns.jointplot(x="total_bill",y='tip',data=tips,kind='hex')


# In[18]:


sns.jointplot(x="total_bill",y='tip',data=tips,kind='reg')


# In[19]:





# In[22]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
get_ipython().run_line_magic('matplotlib', 'inline')
import scipy.stats


# In[26]:


df=pd.read_csv("C:\\Users\\sanjay\\Downloads\\Sales and Advt Cost.csv")


# In[27]:


df


# In[29]:


sns.jointplot(x="Sales (in Lakhs)",y='Advt Cost ( '000),data=df,kind='reg')


# In[32]:


sns.pairplot(tips,hue="smoker",palette="icefire")


# In[33]:


sns.rugplot(tips["total_bill"])


# In[34]:


sns.barplot(x='sex',y='total_bill',data=tips)


# In[36]:


sns.boxplot(x='day',y='total_bill',data=tips,palette='rainbow')


# In[37]:


sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker',palette='rainbow')


# In[38]:


sns.boxplot(x='day',y='total_bill',data=tips,hue='day',palette='rainbow')


# In[39]:


sns.violinplot(x='day',y='total_bill',data=tips,hue='smoker',palette='rainbow')


# In[42]:


sns.violinplot(x='day',y='total_bill',data=tips,hue='sex', split=True ,palette='rainbow')


# # user defined functions or Module

# In[45]:


# A user defined module without return!
def greet(na):
    print("Welcome to the world of python:", na)


# In[46]:


greet('hari')


# In[48]:


def addval(n1,n2):
    ans=n1+n2
    return ans


# In[49]:


addval("hari", "virudhunagar")


# In[51]:


addval(12,54)


# In[67]:



def details(Name,Pr,Qty)
pa('ranjith',6000,2)
if Pr<= 5000:
    Pr=print("No discount")
elif Pr== 5000:10000):
    Pr=Pr*0.10
elif(Pr=> 10000):
    Pr=Pr*0.20
else
    print("invalid inputs")
    


# In[ ]:




