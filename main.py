
#from src import getdata as gd
import pandas as pd
import seaborn as sns
import json
import requests
import numpy as np

# config

# with open("config/config.json", "r") as file:
#     config = json.load(file)
#
# # get the data
#
# #rlt = gd.get_quandl_data(
#     dataset=config["dataset"],
#     start_date=config["start_date"],
#     end_date=config["end_date"],
#     api_key=config["api_key"],
#     store=True
# )

# objective- create a meyer multiple/band trading system

# get bitcoin price data ex glassnode


# insert your API key here
API_KEY = '1x47MovoeRzfbb7YPk49E4lxLxq'

# make API request
res = requests.get('https://api.glassnode.com/v1/metrics/market/price_usd_close',
    params={'a': 'BTC', 'api_key': API_KEY})

# convert to pandas dataframe
df = pd.read_json(res.text, convert_dates=['t'])

# mayer multiple calcs
df["v_log"] = np.log(df["v"])
df['200dma'] = df["v"].rolling(window=200).mean()
df["200dma_log"] = np.log(df["200dma"])
df['mayermultiple'] = df["v"]/df['200dma']

# mayer band calcs

df['mayermultiple']

sns.histplot(data=df, x="mayermultiple", bins=30, binrange=[0,6])
sns.ecdfplot(data=df, x="mayermultiple")

# create dateframe columns that represent the bands and plot them

# make magic lines

sns.lineplot(data=df, x="t", y="v_log")
#sns.lineplot(data=df, x="t", y="v")
sns.lineplot(data=df, x="t", y="mayermultiple")
sns.lineplot(data=df, x="t", y="200dma_log")



# make mayer multiple
# check our math

# make graphs

# backtesting


#











# if __name__ == '__main__':
#
#     pass