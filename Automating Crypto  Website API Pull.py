#!/usr/bin/env python
# coding: utf-8

# In[64]:


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' 
#Original Sandbox Environment: 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'30',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '0ad53085-1cb2-4eb8-ad9e-3ffbd7e56509',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)


# In[2]:


type(data)


# In[65]:


import pandas as pd

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)


# In[66]:


df = pd.json_normalize(data['data'])
df['timestamp'] = pd.to_datetime('now')
df


# In[67]:


def api_runner():
    global df
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' 
    #Original Sandbox Environment: 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
  'start':'1',
  'limit':'30',
  'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': '0ad53085-1cb2-4eb8-ad9e-3ffbd7e56509',
    }

    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
    
    df = pd.json_normalize(data['data'])
    df['timestamp'] = pd.to_datetime('now')
    df
    
    if not os.path.isfile(r'C:\Users\Montalvo\OneDrive\Desktop\Data Analyst Project\API.csv'):
        df.to_csv(r'C:\Users\Montalvo\OneDrive\Desktop\Data Analyst Project\API.csv', header = 'column_names')
    else:
        df.to_csv(r'C:\Users\Montalvo\OneDrive\Desktop\Data Analyst Project\API.csv', mode = 'a', header = False)


# In[ ]:


import os 
from time import time
from time import sleep

for i in range (333):
    api_runner()
    print('API Runner Completed')
    sleep(60) #sleep for 1 minute
exit()


# In[21]:


df1= pd.read_csv(r'C:\Users\Montalvo\OneDrive\Desktop\Data Analyst Project\API.csv')
df1


# In[24]:


pd.set_option('display.float_format', lambda x: '%.5f' % x)


# In[25]:


df


# In[26]:


df2 = df.groupby('name', sort = False)[['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d']].mean()
df2


# In[28]:


df3 = df2.stack()
df3


# In[30]:


df4 = df3.to_frame(name = 'values')
df4


# In[31]:


df4.count()


# In[34]:


index = pd.Index(range(180))


df5 = df4.reset_index()
df5


# In[48]:


df6 = df5.rename(columns = {'level_1':'percent_change'})
df6


# In[49]:


df6['percent_change'] = df6['percent_change'].replace(['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d'],['1h','24h','7d','30d','60d','90d'])
df6


# In[52]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[56]:


sns.catplot(x='percent_change', y='values', hue='name', data = df6, kind= 'point')


# In[60]:


df7 = df[['name','quote.USD.price','timestamp']]
df7 = df7.query("name == 'Bitcoin'")
df7


# In[62]:


sns.set_theme(style='darkgrid')


# In[63]:


sns.lineplot(x = 'timestamp', y='quote.USD.price', data = df7)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




