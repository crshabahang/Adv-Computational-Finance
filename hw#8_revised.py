#!/usr/bin/env python
# coding: utf-8

# # Stock Historical Price and Return Study

# In[3]:


import pandas as pd
import numpy as np
import scipy.stats as stat
import matplotlib.pyplot as plt
import math
import scipy as sp


# 1. Use pandas to read the attached data file 'SP100_adjcose_hist.csv' into a DataFrame with the 'date' column as its index. 
# 
# 2. There are missing data in this file. Make a decision on how you would handle these **NaN**s. Display the first 2 rows of your DataFrame

# In[4]:


#Create a dataframe to store the raw data
rawdata = pd.read_csv('InputFileHW8.csv')
#Create a dataframe to set dates as indices
finaldata = rawdata.set_index('Dates')
finaldata = finaldata.interpolate()
finaldata.head(2)


# 3. For each stock, find the date of stock historical high and historical low prices and put the results in a DataFrame where the index is the stock tickers and columns are 'date_low' and 'date_high'. **Display** the DataFrame 

# In[5]:


#For each stock, find historical high and low dates
#Empty dictionaries
High = {}
Low = {}
# For loop to iterate through each column
for column in finaldata:
    #Find index of the high and low dates and store
    #Fill empty dictionary with ticker names as key
    a = finaldata.loc[finaldata[column]==max(finaldata[column])].index
    b = finaldata.loc[finaldata[column]==min(finaldata[column])].index
    #print(a[0])
    #[0] chooses the dates and fills the empty dictionaries 
    High[column] = a[0]
    Low[column] = b[0]
#One-d array with axis labels
highDate = pd.Series(High)
lowDate = pd.Series(Low)
maxMinDate = pd.DataFrame({'date_high':highDate,'date_low':lowDate})
print(maxMinDate)


# 4. Build a DataFrame where the index is stock ticker and columns are historical high price and low price: 'hi price' and 'lo_price'. **Display** the DataFrame

# In[6]:


#For each stock, find historical high and low prices
#Empty dictionaries
HighPrice = {}
LowPrice = {}
for column in finaldata:
    #Find index of the high and low prices and store
    #Fill empty dictionary with ticker names as key
    a = finaldata.loc[finaldata[column]==max(finaldata[column])]
    b = finaldata.loc[finaldata[column]==min(finaldata[column])]
    #print(a[column])
    #Keys become the new indices and the [0] chooses the price
    HighPrice[column] = a[column][0]
    LowPrice[column] = b[column][0]
#One-d array with axis labels
high = pd.Series(HighPrice)
low = pd.Series(LowPrice)
maxMin = pd.DataFrame({'high_price':high,'low_price':low})
print(maxMin)


# 5. Calculate daily price return series and store the results in dataFrame named 'returns'. Decide on how you would handle the 'NaNs' in the resulting dataFrame. **Display** the first couple of rows of the dataFrame

# In[7]:


#Calculate daily price return series without the use of loops

#Indexes the stock price data by date
date_index = rawdata.set_index('Dates')
StockData1 = date_index
#Drops the first column in a second stock price dataframe
StockData2 = date_index.drop(date_index.index[0])
indices = StockData1.index
indices  = indices.tolist()
#Offset the indices by one 
indices.remove(indices[len(indices)-1])
#StockData3 contains the next day price
StockData3 = pd.DataFrame(StockData2.values,index=indices)
StockData3.columns = StockData2.columns
#Remove the last row of StockData1 for element match
StockData4 = StockData1.drop(date_index.index[len(date_index)-1])
#Calculation of returns
returns = (StockData3-StockData4)/StockData4
returns.head(3)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# 6. Calculate the **annualized** price return covariance matrix of these 100 stocks, assuming there are 252 trading days in a year

# In[11]:


#Annualized price return covariance matrix
AnnCov = 252*returns.cov()
print(AnnCov)


# In[ ]:





# 7. Calculate the **annualized** price return correlation matrix of these 100 stocks, assuming there are 252 trading days in a year

# In[12]:


#Annualized price return correlation matrix
AnnCorr = 252*returns.corr()
print(AnnCorr)


# In[ ]:





# 8. Generate the cumulative return price series and store the result in 'cum_returns' dataFrame. Display the last 2 rows of the dataFrame

# In[10]:


#Cumulative sum
cum_returns =returns.cumsum()
cum_returns.head()


# In[ ]:





# 9. Find the top 10 performers for the year 2017 based on the cumulative returns of that year. Dispaly your results in descending order along with their total return for the year

# In[ ]:





# 10. Construct a fully invested long only portfolio with minimal return volatility( the $\sigma_P$ below). Use the covariance matrix you calculated in problem 6 above.
# 
# **Theoretical Background**
# 
# For a portfolio of $N$ stocks, where percentage investment in stock-$i$ is $w_i$. Let $\sigma_{ij}$ be the covariance between the returns of stock-$i$ and stock-$j$. The portfolio return variance is then
# 
# $\sigma_P^2 = \sum_{i,j}w_iw_j\sigma_{ij}$
# 
# <br>
# 
# The return of the portfolio is 
# 
# $r_P = \sum_i^Nw_ir_i$,
# 
# where $r_i$ is the return of stock-$i$

# In[ ]:




