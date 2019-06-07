#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json


# In[23]:

def pull_data(cate):
    apiKey = "2a8e84d984e747bb83dc02dcc52860de"
    country = "in"
    category = cate
    pageSize = 100


    # In[24]:


    response = requests.get('https://newsapi.org/v2/top-headlines?country={0}&category={1}&pageSize={2}&apiKey={3}'.format(country, category, pageSize, apiKey))
    #res_str = 'https://newsapi.org/v2/top-headlines?country={0}&category={1}&pageSize={2}&apiKey={3}'.format(country, category, pageSize, apiKey)
    #print(res_str)


    # In[25]:


    print(response.status_code)


    # In[26]:


    obj = open('{}-test.txt'.format(category), 'w')
    resp = json.loads(response.content.decode('utf-8'))
    #print(resp)


    # In[27]:


    #print(type(resp['articles'][0]['description']))
    #print(resp)
    
    #if resp['articles'][0]['description'] == None:
    #    continue
    #print(resp['articles'][0]['description'] + "\n")
    #print(resp['totalResults'])


    # In[28]:


    for index in range(resp['totalResults']):
        if resp['articles'][index]['description'] == None:
            continue
        data = str(resp['articles'][index]['description']) + "\n"
        data = data.encode('ascii', 'ignore').decode('ascii')
        obj.write(data)
