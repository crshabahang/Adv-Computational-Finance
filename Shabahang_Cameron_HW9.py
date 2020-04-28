#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web
import datetime as dt

#Function for candlestick plot with short and long moving average window
def candlestick_plot(ticker, short=5, long=15):
    #Exception handling framework to return error if conditions not met
    #try:
        current = dt.date.today()
        delta = dt.timedelta(days=60)
        interval = current - delta
        #Import raw data
        rawdata = web.get_data_yahoo(ticker,start=interval.strftime("%m-%d-%Y"),end=current.strftime("%m-%d-%Y"))
        #Set candlestick attributes
        size = np.arange(len(rawdata.index))
        #Intraday stock price movement initialized
        data_open = rawdata['Open']
        data = rawdata['Close'] - rawdata['Open']
        #print(data)
        scaled =10*size
        #Arrays to store intraday movements
        high = []
        low = []
        #Loop to capture intraday stock movement
        for i in range(len(data)):
            if rawdata['Open'][i]>rawdata['Close'][i]:
                #If intraday movement is positive, record total positive difference from open minus total movement as high 
                high.append(rawdata['High'][i]-rawdata['Open'][i]-data[i])
                low.append(rawdata['Close'][i]-rawdata['Low'][i])
            else:
                #Else record total negative difference from close plus total movement as low
                high.append(rawdata['High'][i]-rawdata['Open'][i])
                low.append(rawdata['Close'][i]-rawdata['Low'][i]+data[i])
        #Calculate moving average
        moving = rawdata['Close'][0]
        
        #Short moving average
        close = []
        for i in range(short-1):
            close.append(moving)
        #Shape is analogy to length for 2-D array
        for i in range(rawdata.shape[0]):
            close.append(rawdata['Close'][i])
        
        SMA = []
        
        #Calculates a simple moving average
        for i in range(rawdata.shape[0]):
            avg = np.asarray(close[i:i+short])
            avg = np.sum(avg)
            avg = avg/short
            SMA.append(avg)
        
        #Long moving average
        close = []
        for i in range(long-1):
            close.append(moving)
        for i in range(rawdata.shape[0]):
            close.append(rawdata['Close'][i])
        
        LMA = []
        
        for i in range(rawdata.shape[0]):
            avg = np.asarray(close[i:i+long])
            avg = np.sum(avg)
            avg = avg/long
            LMA.append(avg)
            
        extrema = [low,high]
        #print(extrema)
        
        #Implementation of candlestick plot using matplotlib
        plt.figure(figsize=(10,6))
        cstick = plt.bar(size, data, bottom=data_open, yerr=extrema)
        plt.minorticks_on()
        
        plt.grid(b=True, which='major', color='b', linestyle='-')
        plt.grid(b=True, which='minor', color='r', linestyle='--')
        
        plt.xlabel('Date :'+interval.strftime("%m-%d-%Y")+' - '+ current.strftime("%m-%d-%Y"))
        plt.ylabel('Price ($)')
        plt.plot(size, SMA, label=str(short)+'-day Moving Average')
        plt.plot(size, LMA, label=str(long)+'-day Moving Average')
        plt.legend()
        
        #Sets the colors with green for profit and red for loss
        for i in range(len(data)):
            if rawdata['Open'][i]>rawdata['Close'][i]:
                cstick[i].set_color('r')
            else:
                cstick[i].set_color('g')
        
        plt.figure(figsize=(10,6))
        vol = plt.bar(size, rawdata['Volume']/1000000)
        plt.xlabel('Date :'+interval.strftime("%m-%d-%Y")+' - '+ current.strftime("%m-%d-%Y"))
        plt.ylabel('Volume ($M)')
        
        
    #except:
        #print('Error')
candlestick_plot('DISH', short=5, long=15)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




