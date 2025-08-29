#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


# In[2]:


df = pd.read_csv('mymoviedb.csv', lineterminator = '\n')


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


df.duplicated().sum()


# In[6]:


df['Genre'].head()


# In[7]:


df.describe()


# # Exploration Summary
# - we have a dataframe consisting of 9827 rows and 9 coumns
# - our dataset looks a bit tidy with no NaNs nor dulplicated values.
# - Release_Date column needs to be casted into date time and to extract only the year value.
# - Overview , Original_Language and Poster-Url wouldn't be so useful during analysis, so we'll drop them.
# - there is noticable outliers in popularity column.
# - genre column has comma seperated values and white spaces that needs to be handled and casted into category. 

# In[8]:


df


# In[9]:


df['Release_Date'] = pd.to_datetime(df['Release_Date'])
print(df['Release_Date'].dtypes)


# In[10]:


df['Release_Date'] = df['Release_Date'].dt.year
df['Release_Date'].dtypes


# In[11]:


df.head()


# ### Dropping the column

# In[12]:


cols = ['Overview','Original_Language', 'Poster_Url']
df.drop(cols , axis=1 ,inplace = True)
df.columns


# In[13]:


df.head()


# In[14]:


def categorize_col(df, col , lables):
    edges = [df[col].describe()['min'],
             df[col].describe()['25%'],
             df[col].describe()['50%'],
             df[col].describe()['75%'],
             df[col].describe()['max']]
    df[col] = pd.cut(df[col],edges,labels = labels , duplicates = 'drop')
    return df


# In[15]:


labels = ['not_popular', 'below_avg', 'average' , 'popular']
categorize_col(df , 'Vote_Average', labels)
df['Vote_Average'].unique()


# In[16]:


df.head()


# In[17]:


df['Vote_Average'].value_counts()


# In[18]:


df.isnull().sum()


# In[19]:


df.dropna(inplace =True)
df.isnull().sum()


# In[20]:


df.nunique()


# ## Data Visualization

# ### what is the most frequent genre of movies released on Netflix

# In[21]:


df['Genre'].describe()


# In[41]:


sns.(y= 'Genre' , data= df, kind='count',
           order = df['Genre'].value_counts().index,
           color ='#4287f5')
plt.title('Genre distribution')
plt.show()


# # which has highest votes in vote avg column

# In[22]:


sns.catplot(y= 'Vote_Average' , data= df, kind='count',
           order = df['Vote_Average'].value_counts().index,
           color ='#4287f5')
plt.title('Votes distribution')
plt.show()


# ### what movie got the highest popularity? what's its genre?

# In[23]:


df[df['Popularity']==df['Popularity'].max()]


# ### what movie got the lowest popularity? what's its genre?

# In[25]:


df[df['Popularity']==df['Popularity'].min()]


# ### which year has the most filmmed movies?

# In[26]:


df['Release_Date'].hist()
plt.title ("Release date column")
plt.show()


# # CONCLUSION

# In[ ]:


get_ipython().run_line_magic('pinfo', 'dataset')
Drama genre is the most frequent genre in our dataset and has appeared more than 14% of the times among 19 other genres.

Q2: What genres has highest votes ?
we have 25.5% of our dataset with popular vote (6520 rows). Drama again gets the highest popularity among fans by being having more than 18.5% of movies popularities.

Q3: What movie got the highest popularity ? what's its genre ?
Spider-Man: No Way Home has the highest popularity rate in our dataset and it has genres of Action , Adventure and Sience Fiction .

Q3: What movie got the lowest popularity ? what's its genre ?
The united states, thread' has the highest lowest rate in our dataset and it has genres of music , drama , 'war', 'sci-fi' and history`.

Q4: Which year has the most fillmmed movies?
year 2020 has the highest filmming rate in our dataset.

