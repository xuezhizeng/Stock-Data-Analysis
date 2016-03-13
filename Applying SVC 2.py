
# coding: utf-8

# In[1]:

import pandas as pd
import os
from Quandl import Quandl
import time


# In[2]:

auth_tok = open("auth.txt","r").read()


# In[5]:

data = Quandl.get("WIKI/KO",trim_start="2000-12-12",
                  trim_end="2014-12-12",authtoken=auth_tok)


# In[8]:

print data["Adj. Close"]



# In[9]:

path = "intraQuarter/"


# In[ ]:

def stock_prices():
    print "Begin..."
    df = pd.DataFrame()
    statspath = path + "/_KeyStats"
    stock_list =  [x[0] for x in os.walk(statspath)]
    print stock_list[0]
    for each_dir in stock_list[1:]:
        try:
            ticker = each_dir.split("//")[0]
            print ticker
            name = "WIKI/"+ticker.upper()
            data = Quandl.get(name,trim_start="2000-12-12",
                      trim_end="2014-12-12",authtoken=auth_tok)
            data[ticker.upper()] = data["Adj. Close"]
            df = pd.concat([df,data[ticker.upper()]],axis = 1)
        
        except Exception as e:
            print str(e)
            try:
                ticker = each_dir.split("//")[0]
                print ticker
                name = "WIKI/"+ticker.upper()
                data = Quandl.get(name,trim_start="2000-12-12",
                          trim_end="2014-12-12",authtoken=auth_tok)
                data[ticker.upper()] = data["Adj. Close"]
                df = pd.concat([df,data[ticker.upper()]],axis = 1)
            except Exception as e:
                print str(e)
                
        df.to_csv("stock_prices.csv")


# In[ ]:

stock_prices()


# In[ ]:



