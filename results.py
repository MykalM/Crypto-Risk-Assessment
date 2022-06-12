#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import sqlalchemy
import requests
import locale
import json
import numpy as np
import hvplot.pandas
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date
import time
import csv
import statistics
import pandas_datareader.data as pdr


# In[2]:


# Create a temporary sqlite database
database_connection_string = 'sqlite:///'

# Create an engine to interact with the database
engine = sqlalchemy.create_engine(database_connection_string)


# In[3]:


def get_data(tickers, start_date, end_date):
    
    """Read in daily price(adjusted close) of asset from CSV files for a given set of dates."""
    
    # download daily price data for each of the stocks in the portfolio
    df = pdr.get_data_yahoo(stocks, start=start_date, end = end_date)['Adj Close']
    df.sort_index(inplace = True)
    
    return df


# In[4]:


with open('test.csv') as csvfile:
    # Return a reader object which will
    # iterate over lines in the given csvfile.
    readCSV = csv.reader(csvfile)
    for row in readCSV:
      results1 = row[0]
      #print(results1)
        
outputDict = {}
with open("test6.csv", newline="") as csvfile:
    data = csv.reader(csvfile, delimiter=",")
    for row in data:
        outputDict[row[0]] = row[1:] if len(row) > 1 else []
        
with open('test7.csv') as csvfile:
    # Return a reader object which will
    # iterate over lines in the given csvfile.
    readCSV = csv.reader(csvfile)
    for row in readCSV:
      Investmentamount = row[:]
     # print(Investmentamount)

#print(Investmentamount)
#type(Investmentamount)


# In[5]:


stocks = ['BTC-USD','ETH-USD','USDT-USD','BNB-USD','ADA-USD','XRP-USD','SOL-USD','DOGE-USD','DOT-USD','UNI-USD','BTT2-USD','TRX-USD','NEO-USD', 'XVG-USD','XMR-USD']


# In[6]:


crypto_prices = get_data(stocks, '06/01/2021', '06/01/2022' )

#print(crypto_prices.head())
#print(crypto_prices.tail())


# In[7]:


def get_historical_data(ticker, start_date, end_date):
    # Pull Historical Data
    data = yf.download(ticker, start=start_date, end=end_date,progress=False)
    # Calculate Daily Returns
    data['Daily Return'] = data['Adj Close'].pct_change()   
    return data.dropna()


# In[8]:


def std_dev(data):
    # Get number of observations
    n = len(data)
    # Calculate mean
    mean = sum(data) / n
    # Calculate deviations from the mean
    deviations = sum([(x - mean)**2 for x in data])
    # Calculate Variance & Standard Deviation
    variance = deviations / (n - 1)
    s = variance**(1/2)
    return s


# In[9]:


# Sharpe Ratio From Scratch
def annualize_sharpe_ratio(data, risk_free_rate=0.0):
    # Calculate Average Daily Return
    mean_daily_return = sum(data) / len(data)
    # Calculate Standard Deviation
    s = std_dev(data)
    # Calculate Daily Sharpe Ratio
    daily_sharpe_ratio = (mean_daily_return - risk_free_rate) / s
    # Annualize Daily Sharpe Ratio
    sharpe_ratio = 252**(1/2) * daily_sharpe_ratio
    
    return sharpe_ratio


# In[10]:


# Sharpe Ratio From Scratch
def sharpe_ratio(data, risk_free_rate=0.0):
    # Calculate Average Daily Return
    mean_daily_return = sum(data) / len(data)
    # Calculate Standard Deviation
    s = std_dev(data)
    # Calculate Daily Sharpe Ratio
    daily_sharpe_ratio = (mean_daily_return - risk_free_rate) / s
    # Annualize Daily Sharpe Ratio
    sharpe_ratio = 252**(1/2) * daily_sharpe_ratio
    
    return sharpe_ratio


# In[11]:


btc_df = get_historical_data('BTC-USD', start_date='2021-06-01', end_date='2022-06-01')
eth_df = get_historical_data('ETH-USD', start_date='2021-06-01', end_date='2022-06-01')
usdt_df = get_historical_data('USDT-USD', start_date='2021-06-01', end_date='2022-06-01')
bnb_df = get_historical_data('BNB-USD', start_date='2021-06-01', end_date='2022-06-01')
ada_df = get_historical_data('ADA-USD', start_date='2021-06-01', end_date='2022-06-01')
xrp_df = get_historical_data('XRP-USD', start_date='2021-06-01', end_date='2022-06-01')
sol_df = get_historical_data('SOL-USD', start_date='2021-06-01', end_date='2022-06-01')
doge_df = get_historical_data('DOGE-USD', start_date='2021-06-01', end_date='2022-06-01')
dot_df = get_historical_data('DOT-USD', start_date='2021-06-01', end_date='2022-06-01')
uni_df = get_historical_data('UNI-USD', start_date='2021-06-01', end_date='2022-06-01')
btt2_df = get_historical_data('BTT2-USD', start_date='2021-06-01', end_date='2022-06-01')
trx_df = get_historical_data('TRX-USD', start_date='2021-06-01', end_date='2022-06-01')
xmr_df = get_historical_data('XMR-USD', start_date='2021-06-01', end_date='2022-06-01')
neo_df = get_historical_data('NEO-USD', start_date='2021-06-01', end_date='2022-06-01')
xvg_df = get_historical_data('XVG-USD', start_date='2021-06-01', end_date='2022-06-01')


# In[12]:


#display(xmr_df)


# In[62]:


#display(annualize_sharpe_ratio(btc_df['Daily Return']))
#display(annualize_sharpe_ratio(eth_df['Daily Return']))
#display(annualize_sharpe_ratio(usdt_df['Daily Return']))
#display(annualize_sharpe_ratio(bnb_df['Daily Return']))
#display(annualize_sharpe_ratio(ada_df['Daily Return']))
#display(annualize_sharpe_ratio(xrp_df['Daily Return']))
#display(annualize_sharpe_ratio(sol_df['Daily Return']))
#display(annualize_sharpe_ratio(doge_df['Daily Return']))
#display(annualize_sharpe_ratio(dot_df['Daily Return']))
#display(annualize_sharpe_ratio(trx_df['Daily Return']))
#display(annualize_sharpe_ratio(xmr_df['Daily Return']))
#display(annualize_sharpe_ratio(btt2_df['Daily Return']))
#display(annualize_sharpe_ratio(uni_df['Daily Return']))
#display(annualize_sharpe_ratio(neo_df['Daily Return']))
#display(annualize_sharpe_ratio(xvg_df['Daily Return']))


# In[14]:


# Next, we'll define a function for calculating daily returns for our coins
def calc_daily_returns(df):
    return (df.pct_change())


# In[15]:


crypto_daily_rets = calc_daily_returns(crypto_prices)
#print(crypto_daily_rets.head())
#print(crypto_daily_rets.tail())


# In[16]:


# Define a function for creating covariance matrices
def create_covariance_matrix(daily_returns):
    return daily_returns.cov()


# In[17]:


#crypto_cov_matrix = create_covariance_matrix(crypto_daily_rets)
#round((crypto_cov_matrix),4)


# In[18]:


# Define a function for creating variance matrices
def create_variance_matrix(daily_returns):
    return daily_returns.var()


# In[19]:


#statistics.variance(cs)
#crypto_var_matrix = create_variance_matrix(crypto_daily_rets)
#round((crypto_var_matrix),5)


# In[20]:


BTC_variance = (btc_df['Daily Return']).var()
#BTC_variance


# In[21]:


ETH_variance = (eth_df['Daily Return']).var()
#ETH_variance


# In[22]:


# The Free Crypto API Call endpoint URLs for the held cryptocurrency assets
btc_url = "https://api.alternative.me/v2/ticker/Bitcoin/?convert=USD"
eth_url = "https://api.alternative.me/v2/ticker/Ethereum/?convert=USD"
usdt_url = "https://api.alternative.me/v2/ticker/Tether/?convert=USD"
bnb_url = "https://api.alternative.me/v2/ticker/BinanceCoin/?convert=USD"
ada_url = "https://api.alternative.me/v2/ticker/Cardano/?convert=USD"
xrp_url = "https://api.alternative.me/v2/ticker/Ripple/?convert=USD"
sol_url = "https://api.alternative.me/v2/ticker/Solana/?convert=USD"
doge_url = "https://api.alternative.me/v2/ticker/Dogecoin/?convert=USD"
dot_url = "https://api.alternative.me/v2/ticker/Polkadot/?convert=USD"
uni_url = "https://api.alternative.me/v2/ticker/Uniswap/?convert=USD"
btt2_url = "https://api.alternative.me/v2/ticker/bittorrent-2/?convert=USD"
trx_url = "https://api.alternative.me/v2/ticker/Tron/?convert=USD"
xmr_url = "https://api.alternative.me/v2/ticker/Monero/?convert=USD"
neo_url = "https://api.alternative.me/v2/ticker/Neo/?convert=USD"
xvg_url = "https://api.alternative.me/v2/ticker/Verge/?convert=USD"


# In[23]:


btc_response = requests.get(btc_url).json()
eth_response= requests.get(eth_url).json()
usdt_response= requests.get(usdt_url).json()
bnb_response= requests.get(bnb_url).json()
ada_response = requests.get(ada_url).json()
xrp_response = requests.get(xrp_url).json()
sol_response = requests.get(sol_url).json()
doge_response = requests.get(doge_url).json()
dot_response = requests.get(dot_url).json()
uni_response= requests.get(uni_url).json()
btt2_response = requests.get(btt2_url).json()
trx_response = requests.get(trx_url).json()
xmr_response = requests.get(xmr_url).json()
neo_response = requests.get(neo_url).json()
xvg_response= requests.get(xvg_url).json()


# In[24]:


#print(json.dumps(btc_response, indent=4, sort_keys=True))
#print(json.dumps(eth_response, indent=4, sort_keys=True))
#print(json.dumps(usdt_response, indent=4, sort_keys=True))
#print(json.dumps(bnb_response, indent=4, sort_keys=True))
#print(json.dumps(ada_response, indent=4, sort_keys=True))
#print(json.dumps(xrp_response, indent=4, sort_keys=True))
#print(json.dumps(sol_response, indent=4, sort_keys=True))
#print(json.dumps(doge_response, indent=4, sort_keys=True))
#print(json.dumps(dot_response, indent=4, sort_keys=True))
#print(json.dumps(uni_response, indent=4, sort_keys=True))
#print(json.dumps(btt2_response, indent=4, sort_keys=True))
#print(json.dumps(trx_response, indent=4, sort_keys=True))
#print(json.dumps(xmr_response, indent=4, sort_keys=True))
#print(json.dumps(neo_response, indent=4, sort_keys=True))
#print(json.dumps(xvg_response, indent=4, sort_keys=True))


# In[25]:


# Crypto names
btc_name = btc_response["data"]["1"]["name"]
eth_name = eth_response["data"]["1027"]["name"]
usdt_name = usdt_response["data"]["825"]["name"]
bnb_name = bnb_response["data"]["1839"]["name"]
ada_name = ada_response["data"]["2010"]["name"]
xrp_name = xrp_response["data"]["52"]["name"]
sol_name = sol_response["data"]["11733"]["name"]
doge_name = doge_response["data"]["74"]["name"]
dot_name = dot_response["data"]["11517"]["name"]
uni_name = uni_response["data"]["11968"]["name"]
btt2_name = btt2_response["data"]["3084"]["name"]
trx_name = trx_response["data"]["1958"]["name"]
xmr_name = xmr_response["data"]["328"]["name"]
neo_name = neo_response["data"]["1376"]["name"]
xvg_name = xvg_response["data"]["693"]["name"]


# In[26]:


# Crypto Symbol
btc_symbol = btc_response["data"]["1"]["symbol"]
eth_symbol = eth_response["data"]["1027"]["symbol"]
usdt_symbol = usdt_response["data"]["825"]["symbol"]
bnb_symbol = bnb_response["data"]["1839"]["symbol"]
ada_symbol = ada_response["data"]["2010"]["symbol"]
xrp_symbol = xrp_response["data"]["52"]["symbol"]
sol_symbol = sol_response["data"]["11733"]["symbol"]
doge_symbol = doge_response["data"]["74"]["symbol"]
dot_symbol = dot_response["data"]["11517"]["symbol"]
uni_symbol = uni_response["data"]["11968"]["symbol"]
btt2_symbol = btt2_response["data"]["3084"]["symbol"]
trx_symbol = trx_response["data"]["1958"]["symbol"]
xmr_symbol = xmr_response["data"]["328"]["symbol"]
neo_symbol = neo_response["data"]["1376"]["symbol"]
xvg_symbol = xvg_response["data"]["693"]["symbol"]


# In[27]:


# Crypto Category
btc_cat = 'BTC'
eth_cat = "Altcoins"
usdt_cat = "Stablecoin"
bnb_cat = "Stablecoin"
ada_cat = 'Altcoins'
xrp_cat = 'Altcoins'
sol_cat = 'Altcoins'
doge_cat = 'Meme coin'
dot_cat = 'Altcoins'
uni_cat = "Altcoins"
btt2_cat = "Altcoins"
trx_cat = "Altcoins"
xmr_cat = "Altcoins"
neo_cat = "Altcoins"
xvg_cat = "Altcoins"


# In[28]:


# Crypto price
btc_price = "${:,.2f}".format(btc_response["data"]["1"]["quotes"]["USD"]["price"])
eth_price = "${:,.2f}".format(eth_response["data"]["1027"]["quotes"]["USD"]["price"])
usdt_price = "${:,.2f}".format(usdt_response["data"]["825"]["quotes"]["USD"]["price"])
bnb_price = "${:,.2f}".format(bnb_response["data"]["1839"]["quotes"]["USD"]["price"])
ada_price = "${:,.2f}".format(ada_response["data"]["2010"]["quotes"]["USD"]["price"])
xrp_price = "${:,.2f}".format(xrp_response["data"]["52"]["quotes"]["USD"]["price"])
sol_price = "${:,.2f}".format(sol_response["data"]["11733"]["quotes"]["USD"]["price"])
doge_price = "${:,.2f}".format(doge_response["data"]["74"]["quotes"]["USD"]["price"])
dot_price = "${:,.2f}".format(dot_response["data"]["11517"]["quotes"]["USD"]["price"])
uni_price = "${:,.2f}".format(uni_response["data"]["11968"]["quotes"]["USD"]["price"])
btt2_price = "${:,.2f}".format(btt2_response["data"]["3084"]["quotes"]["USD"]["price"])
trx_price = "${:,.2f}".format(trx_response["data"]["1958"]["quotes"]["USD"]["price"])
xmr_price = "${:,.2f}".format(xmr_response["data"]["328"]["quotes"]["USD"]["price"])
neo_price = "${:,.2f}".format(neo_response["data"]["1376"]["quotes"]["USD"]["price"])
xvg_price = "${:,.2f}".format(xvg_response["data"]["693"]["quotes"]["USD"]["price"])


# In[29]:


# print(btc_price)


# In[30]:


# 24hr Volume
btc_vol = f"$ ""{:,}".format(btc_response["data"]["1"]["quotes"]["USD"]["volume_24h"])
eth_vol = f"$ ""{:,}".format(eth_response["data"]["1027"]["quotes"]["USD"]["volume_24h"])
usdt_vol = f"$ ""{:,}".format(usdt_response["data"]["825"]["quotes"]["USD"]["volume_24h"])
bnb_vol = f"$ ""{:,}".format(bnb_response["data"]["1839"]["quotes"]["USD"]["volume_24h"])
ada_vol = f"$ ""{:,}".format(ada_response["data"]["2010"]["quotes"]["USD"]["volume_24h"])
xrp_vol = f"$ ""{:,}".format(xrp_response["data"]["52"]["quotes"]["USD"]["volume_24h"])
sol_vol = f"$ ""{:,}".format(sol_response["data"]["11733"]["quotes"]["USD"]["volume_24h"])
doge_vol = f"$ ""{:,}".format(doge_response["data"]["74"]["quotes"]["USD"]["volume_24h"])
dot_vol = f"$ ""{:,}".format(dot_response["data"]["11517"]["quotes"]["USD"]["volume_24h"])
uni_vol = f"$ ""{:,}".format(uni_response["data"]["11968"]["quotes"]["USD"]["volume_24h"])
btt2_vol = f"$ ""{:,}".format(btt2_response["data"]["3084"]["quotes"]["USD"]["volume_24h"])
trx_vol = f"$ ""{:,}".format(trx_response["data"]["1958"]["quotes"]["USD"]["volume_24h"])
xmr_vol = f"$ ""{:,}".format(xmr_response["data"]["328"]["quotes"]["USD"]["volume_24h"])
neo_vol = f"$ ""{:,}".format(neo_response["data"]["1376"]["quotes"]["USD"]["volume_24h"])
xvg_vol = f"$ ""{:,}".format(xvg_response["data"]["693"]["quotes"]["USD"]["volume_24h"])


# In[31]:


# Market Cap
btc_cap = f"$ ""{:,}".format(btc_response["data"]["1"]["quotes"]["USD"]["market_cap"])
eth_cap = f"$ ""{:,}".format(eth_response["data"]["1027"]["quotes"]["USD"]["market_cap"])
usdt_cap = f"$ ""{:,}".format(usdt_response["data"]["825"]["quotes"]["USD"]["market_cap"])
bnb_cap = f"$ ""{:,}".format(bnb_response["data"]["1839"]["quotes"]["USD"]["market_cap"])
ada_cap = f"$ ""{:,}".format(ada_response["data"]["2010"]["quotes"]["USD"]["market_cap"])
xrp_cap = f"$ ""{:,}".format(xrp_response["data"]["52"]["quotes"]["USD"]["market_cap"])
sol_cap = f"$ ""{:,}".format(sol_response["data"]["11733"]["quotes"]["USD"]["market_cap"])
doge_cap =f"$ " "{:,}".format(doge_response["data"]["74"]["quotes"]["USD"]["market_cap"])
dot_cap = f"$ ""{:,}".format(dot_response["data"]["11517"]["quotes"]["USD"]["market_cap"])
uni_cap = f"$ ""{:,}".format(uni_response["data"]["11968"]["quotes"]["USD"]["market_cap"])
btt2_cap = f"$ ""{:,}".format(btt2_response["data"]["3084"]["quotes"]["USD"]["market_cap"])
trx_cap =f"$ " "{:,}".format(trx_response["data"]["1958"]["quotes"]["USD"]["market_cap"])
xmr_cap =f"$ " "{:,}".format(xmr_response["data"]["328"]["quotes"]["USD"]["market_cap"])
neo_cap = f"$ ""{:,}".format(neo_response["data"]["1376"]["quotes"]["USD"]["market_cap"])
xvg_cap = f"$ ""{:,}".format(xvg_response["data"]["693"]["quotes"]["USD"]["market_cap"])


# In[32]:


# percent_change_1h
btc_1hr = "{:.2%}".format((btc_response["data"]["1"]["quotes"]["USD"]["percentage_change_1h"] / 100))
eth_1hr = "{:.2%}".format((eth_response["data"]["1027"]["quotes"]["USD"]["percentage_change_1h"] / 100))
usdt_1hr = "{:.2%}".format((usdt_response["data"]["825"]["quotes"]["USD"]["percentage_change_1h"] / 100))
bnb_1hr = "{:.2%}".format((bnb_response["data"]["1839"]["quotes"]["USD"]["percentage_change_1h"] / 100))
ada_1hr = "{:.2%}".format((ada_response["data"]["2010"]["quotes"]["USD"]["percentage_change_1h"] / 100))
xrp_1hr = "{:.2%}".format((xrp_response["data"]["52"]["quotes"]["USD"]["percentage_change_1h"] / 100))
ada_1hr = "{:.2%}".format((ada_response["data"]["2010"]["quotes"]["USD"]["percentage_change_1h"] / 100))
sol_1hr = "{:.2%}".format((sol_response["data"]["11733"]["quotes"]["USD"]["percentage_change_1h"] / 100))
doge_1hr = "{:.2%}".format((doge_response["data"]["74"]["quotes"]["USD"]["percentage_change_1h"] / 100))
dot_1hr = "{:.2%}".format((dot_response["data"]["11517"]["quotes"]["USD"]["percentage_change_1h"] / 100))
uni_1hr = "{:.2%}".format((uni_response["data"]["11968"]["quotes"]["USD"]["percentage_change_1h"] / 100))
btt2_1hr = "{:.2%}".format((btt2_response["data"]["3084"]["quotes"]["USD"]["percentage_change_1h"] / 100))
trx_1hr = "{:.2%}".format((trx_response["data"]["1958"]["quotes"]["USD"]["percentage_change_1h"] / 100))
xmr_1hr = "{:.2%}".format((xmr_response["data"]["328"]["quotes"]["USD"]["percentage_change_1h"] / 100))
neo_1hr = "{:.2%}".format((neo_response["data"]["1376"]["quotes"]["USD"]["percentage_change_1h"] / 100))
xvg_1hr = "{:.2%}".format((xvg_response["data"]["693"]["quotes"]["USD"]["percentage_change_1h"] / 100))


# In[33]:


# percent_change_24h
btc_24hr = "{:.2%}".format((btc_response["data"]["1"]["quotes"]["USD"]["percentage_change_24h"] / 100))
eth_24hr = "{:.2%}".format((eth_response["data"]["1027"]["quotes"]["USD"]["percentage_change_24h"] / 100))
usdt_24hr = "{:.2%}".format((usdt_response["data"]["825"]["quotes"]["USD"]["percentage_change_24h"] / 100))
bnb_24hr = "{:.2%}".format((bnb_response["data"]["1839"]["quotes"]["USD"]["percentage_change_24h"] / 100))
ada_24hr = "{:.2%}".format((ada_response["data"]["2010"]["quotes"]["USD"]["percentage_change_24h"] / 100))
xrp_24hr = "{:.2%}".format((xrp_response["data"]["52"]["quotes"]["USD"]["percentage_change_24h"] / 100))
sol_24hr = "{:.2%}".format((sol_response["data"]["11733"]["quotes"]["USD"]["percentage_change_24h"] / 100))
doge_24hr= "{:.2%}".format((doge_response["data"]["74"]["quotes"]["USD"]["percentage_change_24h"] / 100))
dot_24hr = "{:.2%}".format((dot_response["data"]["11517"]["quotes"]["USD"]["percentage_change_24h"] / 100))
uni_24hr = "{:.2%}".format((uni_response["data"]["11968"]["quotes"]["USD"]["percentage_change_24h"] / 100))
btt2_24hr = "{:.2%}".format((btt2_response["data"]["3084"]["quotes"]["USD"]["percentage_change_24h"] / 100))
trx_24hr = "{:.2%}".format((trx_response["data"]["1958"]["quotes"]["USD"]["percentage_change_24h"] / 100))
xmr_24hr = "{:.2%}".format((xmr_response["data"]["328"]["quotes"]["USD"]["percentage_change_24h"] / 100))
neo_24hr = "{:.2%}".format((neo_response["data"]["1376"]["quotes"]["USD"]["percentage_change_24h"] / 100))
xvg_24hr = "{:.2%}".format((xvg_response["data"]["693"]["quotes"]["USD"]["percentage_change_24h"] / 100))


# In[34]:


# percent_change_7d
btc_7d =  "{:.2%}".format((btc_response["data"]["1"]["quotes"]["USD"]["percentage_change_7d"] / 100))
eth_7d =  "{:.2%}".format((eth_response["data"]["1027"]["quotes"]["USD"]["percentage_change_7d"] / 100))
usdt_7d =  "{:.2%}".format((usdt_response["data"]["825"]["quotes"]["USD"]["percentage_change_7d"] / 100))
bnb_7d =  "{:.2%}".format((bnb_response["data"]["1839"]["quotes"]["USD"]["percentage_change_7d"] / 100))
ada_7d = "{:.2%}".format((ada_response["data"]["2010"]["quotes"]["USD"]["percentage_change_7d"] / 100))
xrp_7d = "{:.2%}".format((xrp_response["data"]["52"]["quotes"]["USD"]["percentage_change_7d"] / 100))
sol_7d = "{:.2%}".format((sol_response["data"]["11733"]["quotes"]["USD"]["percentage_change_7d"] / 100))
doge_7d = "{:.2%}".format((doge_response["data"]["74"]["quotes"]["USD"]["percentage_change_7d"] / 100))
dot_7d = "{:.2%}".format((dot_response["data"]["11517"]["quotes"]["USD"]["percentage_change_7d"] / 100))
uni_7d =  "{:.2%}".format((uni_response["data"]["11968"]["quotes"]["USD"]["percentage_change_7d"] / 100))
btt2_7d = "{:.2%}".format((btt2_response["data"]["3084"]["quotes"]["USD"]["percentage_change_7d"] / 100))
trx_7d = "{:.2%}".format((trx_response["data"]["1958"]["quotes"]["USD"]["percentage_change_7d"] / 100))
xmr_7d = "{:.2%}".format((xmr_response["data"]["328"]["quotes"]["USD"]["percentage_change_7d"] / 100))
neo_7d = "{:.2%}".format((neo_response["data"]["1376"]["quotes"]["USD"]["percentage_change_7d"] / 100))
xvg_7d =  "{:.2%}".format((xvg_response["data"]["693"]["quotes"]["USD"]["percentage_change_7d"] / 100))


# In[35]:


stocks_dataframe = pd.DataFrame({'Coins': [btc_name,eth_name,usdt_name,bnb_name,ada_name,xrp_name,sol_name,doge_name,dot_name, trx_name, xmr_name,btt2_name,uni_name, neo_name, xvg_name], 'Symbol': [btc_symbol,eth_symbol,usdt_symbol,bnb_symbol,ada_symbol,xrp_symbol,sol_symbol,doge_symbol,dot_symbol,trx_symbol,xmr_symbol,btt2_symbol, uni_symbol, neo_symbol,xvg_symbol],'Category': [btc_cat,eth_cat,usdt_cat,bnb_cat,ada_cat,xrp_cat,sol_cat,doge_cat,dot_cat,trx_cat,xmr_cat,btt2_cat, uni_cat, neo_cat, xvg_cat], 'Price': [btc_price,eth_price,usdt_price,bnb_price,ada_price,xrp_price,sol_price,doge_price,dot_price,trx_price,xmr_price, btt2_price, uni_price, neo_price, xvg_price],'24Hr Volume': [btc_vol,eth_vol,usdt_vol,bnb_vol,ada_vol,xrp_vol,sol_vol,doge_vol,dot_vol,trx_vol,xmr_vol, btt2_vol, uni_vol, neo_vol, xvg_vol], 'Market Caplization':[btc_cap,eth_cap,usdt_cap,bnb_cap,ada_cap,xrp_cap,sol_cap,doge_cap,dot_cap,trx_cap, xmr_cap, btt2_cap, uni_cap, neo_cap, xvg_cap],'1hr % Change': [btc_1hr,eth_1hr,usdt_1hr,bnb_1hr,ada_1hr,xrp_1hr,sol_1hr,doge_1hr, dot_1hr,trx_1hr,xmr_1hr, btt2_1hr, uni_1hr, neo_1hr, xvg_1hr], '24hrs %Change': [btc_24hr,eth_24hr,usdt_24hr,bnb_24hr,ada_24hr,xrp_24hr,sol_24hr,doge_24hr,dot_24hr,trx_24hr,xmr_24hr, btt2_24hr, uni_24hr, neo_24hr, xvg_24hr],'7days %Change': [btc_7d,eth_7d,usdt_7d,bnb_7d,ada_7d,xrp_7d,sol_7d,doge_7d,dot_7d,trx_7d, xmr_7d,btt2_7d, uni_7d, neo_7d, xvg_7d], 'Sharpe Ratio': [0.03511, -0.02513, -0.07216,0.16141,-0.51536,-0.39877,0.68934,-0.70023,-0.11434,0.45510,0.16614,-1.04729,1.43817,-0.75020,-0.69200],'Variance': [0.00130,0.00186,0.00000,0.00188,0.00283,0.00255,0.00419,0.00322,0.00307,0.15813,0.00510,0.00215,0.00266, 0.00317,0.00377] })
stocks_dataframe.to_sql('Crypto', engine)
engine.table_names()


# In[36]:


query = """
SELECT "Coins" FROM Crypto;
"""
results = engine.execute(query)
#list(results)


# In[37]:


stocks_dataframe


# In[38]:


btc_cumulative_returns = (1 + btc_df["Daily Return"]).cumprod()
eth_cumulative_returns = (1 + eth_df["Daily Return"]).cumprod()
usdt_cumulative_returns = (1 + usdt_df["Daily Return"]).cumprod()
bnb_cumulative_returns = (1 + bnb_df["Daily Return"]).cumprod()
ada_cumulative_returns = (1 + ada_df["Daily Return"]).cumprod()
xrp_cumulative_returns = (1 + xrp_df["Daily Return"]).cumprod()
sol_cumulative_returns = (1 + sol_df["Daily Return"]).cumprod()
doge_cumulative_returns = (1 + doge_df["Daily Return"]).cumprod()
dot_cumulative_returns = (1 + dot_df["Daily Return"]).cumprod()
trx_cumulative_returns = (1 + trx_df["Daily Return"]).cumprod()
xmr_cumulative_returns = (1 + xmr_df["Daily Return"]).cumprod()
btt2_cumulative_returns = (1 + btt2_df["Daily Return"]).cumprod()
uni_cumulative_returns = (1 + uni_df["Daily Return"]).cumprod()
neo_cumulative_returns = (1 + neo_df["Daily Return"]).cumprod()
xvg_cumulative_returns = (1 + xvg_df["Daily Return"]).cumprod()


# In[39]:


btc_cumulative_returns = (1 + btc_df["Daily Return"]).cumprod(axis = 0, skipna = True)
#display(btc_cumulative_returns)


# In[40]:


#list to string conversion
a = Investmentamount
b = ''.join(str(a).split(','))
c = ((b).replace("'", ""))
new_lst = str(c)[1:-1] 
d = new_lst.replace(" ", "")
e = (int(d))
#print(e)


# In[41]:


btc_cumulative_returns2 = btc_cumulative_returns  * e

btc_cumulative = btc_cumulative_returns.hvplot(
    title="Bitcoin Cumulative Returns 06/01/2021 - 06/01/2022",
    x="Date",
    xlabel="Date",
    ylabel="Cumulative Returns"
)

#btc_cumulative

btc_cumulative2 = btc_cumulative_returns2.hvplot(
    title="Bitcoin Cumulative Returns 06/01/2021 - 06/01/2022",
    x="Date",
    xlabel="Date",
    ylabel=" Investment Made"
)

#btc_cumulative2


# In[42]:


eth_cumulative = eth_cumulative_returns.hvplot(
    title="Ethereum Cumulative Returns 06/01/2021 - 06/01/2022",
    x="Date",
    xlabel="Date",
    ylabel="Cumulative Returns"
)

low_risk_chart = eth_cumulative_returns + btc_cumulative_returns

low_risk = low_risk_chart.hvplot(
    title="Ethereum Cumulative Returns 06/01/2021 - 06/01/2022",
    x="Date",
    xlabel="Date",
    ylabel="Cumulative Returns"
)


# In[43]:


usdt_cumulative = usdt_cumulative_returns.hvplot(
    title="Tether Cumulative Returns 06/01/2021 - 06/01/2022",
    x="Date",
    xlabel="Date",
    ylabel="Cumulative Returns"
)

#usdt_cumulative


# In[44]:


bnb_cumulative = bnb_cumulative_returns.hvplot(
    title="Binance Coin Cumulative Returns 06/01/2021 - 06/01/2022",
    x="Date",
    xlabel="Date",
    ylabel="Cumulative Returns"
)

#bnb_cumulative


# In[45]:


ada_cumulative = ada_cumulative_returns.hvplot(
    title="Cardano Cumulative Returns 06/01/2021 - 06/01/2022",
    x="Date",
    xlabel="Date",
    ylabel="Cumulative Returns"
)

#ada_cumulative


# In[59]:


xrp_cumulative = xrp_cumulative_returns.hvplot(
    title="Ripple Cumulative Returns 06/01/2021 - 06/01/2022",
    x="Date",
    xlabel="Date",
    ylabel="Cumulative Returns"
)

#xrp_cumulative


# In[60]:


sol_cumulative = sol_cumulative_returns.hvplot(
    title="Solana Cumulative Returns 06/01/2021 - 06/01/2022",
    x="Date",
    xlabel="Date",
    ylabel="Cumulative Returns"
)

#sol_cumulative


# In[61]:


doge_cumulative = doge_cumulative_returns.hvplot(
    title="Dogecoin Cumulative Returns 06/01/2021 - 06/01/2022",
    x="Date",
    xlabel="Date",
    ylabel="Cumulative Returns"
)

#doge_cumulative


# In[49]:


dot_cumulative = dot_cumulative_returns.hvplot(
    title="Polkadot Cumulative Returns 06/01/2021 - 06/01/2022",
    x="Date",
    xlabel="Date",
    ylabel="Cumulative Returns"
)

#dot_cumulative


# In[50]:


trx_cumulative = trx_cumulative_returns.hvplot(
    title="Tron Cumulative Returns 06/01/2021 - 06/01/2022",
    x="Date",
    xlabel="Date",
    ylabel="Cumulative Returns"
)

#trx_cumulative


# In[51]:


xmr_cumulative = xmr_cumulative_returns.hvplot(
    title="Monero Cumulative Returns 06/01/2021 - 06/01/2022",
    x="Date",
    xlabel="Date",
    ylabel="Cumulative Returns"
)

#xmr_cumulative


# In[52]:


btt2_cumulative = btt2_cumulative_returns.hvplot(
    title="BitTorrent Token Cumulative Returns 06/01/2021 - 06/01/2022",
    x="Date",
    xlabel="Date",
    ylabel="Cumulative Returns"
)

#btt2_cumulative


# In[53]:


uni_cumulative = uni_cumulative_returns.hvplot(
    title="Uniswap Cumulative Returns 06/01/2021 - 06/01/2022",
    x="Date",
    xlabel="Date",
    ylabel="Cumulative Returns"
)

#uni_cumulative


# In[54]:


neo_cumulative = neo_cumulative_returns.hvplot(
    title="Neo Cumulative Returns 06/01/2021 - 06/01/2022",
    x="Date",
    xlabel="Date",
    ylabel="Cumulative Returns"
)

#neo_cumulative


# In[55]:


Verge_cumulative = xvg_cumulative_returns.hvplot(
    title="Verge Cumulative Returns 06/01/2021 - 06/01/2022",
    x="Date",
    xlabel="Date",
    ylabel="Cumulative Returns"
)

#Verge_cumulative


# In[56]:


key_list_keys = list(outputDict.keys())
key_list_values = list(outputDict.values())


data = {
       'BitTorrent': [320],
       'Binance Coin': [150],
       'TRON':[150],
       'XRP':[150],
       'DOGE':[800],
       'NEO':[150],
       'Verge':[700],
       'Cardano':[800]
      }
    
#print(key_list_keys) 
#print(key_list_values) 
#type(key_list_values)


#print(outputDict)
    
high_risk = pd.DataFrame(data,columns=['BitTorrent','Binance Coin','TRON'], index = ['Portfolio'])
medium_risk = pd.DataFrame(data,columns=['XRP','Binance Coin','TRON','DOGE'], index = ['Portfolio'])
#medium_risk = pd.DataFrame(key_list_keys,key_list_values,index = ['Portfolio'])
low_risk = pd.DataFrame(data,columns=['NEO','Verge','TRON','DOGE','Cardano'], index = ['Portfolio'])



    
    


# In[63]:


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


# In[67]:


if results1 == 'h': 
    high_risk.style.use('ggplot')
    high_risk.plot.barh(stacked=True, figsize=(20,2))
    plt.title('High Risk')
    plt.ylabel('Portfolio')
    plt.xlabel('Quantity')
    plt.show()
    chart = (1/(btt2_cumulative_returns + bnb_cumulative_returns + trx_cumulative_returns) * e)
    display_chart = chart.hvplot(
                title="Your Total Cumulative Returns 06/01/2021 - 06/01/2022",
                x="Date",
                xlabel="Date",
                ylabel="Cumulative Returns",
                rot = 90
            )
    print("This is total return if invested on 6/1/2021 830.27%")
elif results1 == 'm': 
    medium_risk .style.use('ggplot')
    medium_risk .plot.barh(stacked=True, figsize=(18,2))
    plt.title('Medium Risk')
    plt.ylabel('Portfolio')
    plt.xlabel('Quantity')
    plt.show()
    chart = (1/(xrp_cumulative_returns + bnb_cumulative_returns + trx_cumulative_returns + doge_cumulative_returns) * e)
    display_chart = chart.hvplot(
                title="Your Total Cumulative Returns 06/01/2021 - 06/01/2022",
                x="Date",
                xlabel="Date",
                ylabel="Cumulative Returns",
                rot = 90
            )
    print(color.RED + color.BOLD + "This is total return if invested on 6/1/2021 {:.2%}".format((chart[355]/chart[1]))+ color.END)
    
else:
    low_risk .style.use('ggplot')
    low_risk .plot.barh(stacked=True, figsize=(20,2))
    plt.title('Low Risk')
    plt.ylabel('Portfolio')
    plt.xlabel('Quantity')
    plt.show()
    chart = (1/(neo_cumulative_returns + xvg_cumulative_returns + trx_cumulative_returns + doge_cumulative_returns + ada_cumulative_returns) * e)
    display_chart = chart.hvplot(
                title="Your Total Cumulative Returns 06/01/2021 - 06/01/2022",
                x="Date",
                xlabel="Date",
                ylabel="Cumulative Returns",
                rot = 90
            )
    print(color.BLUE + color.BOLD +"This is total return if invested on 6/1/2021 {:.2%}".format((chart[355]/chart[1]))+ color.END)


# In[58]:


display_chart


# In[ ]:





# In[ ]:




