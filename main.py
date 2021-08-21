
from src import getdata as gd
import pandas as pd
import seaborn as sns
import json

# config

with open("config/config.json", "r") as file:
    config = json.load(file)

# get the data

rlt = gd.get_quandl_data(
    dataset=config["dataset"],
    start_date=config["start_date"],
    end_date=config["end_date"],
    api_key=config["api_key"],
    store=True
)

#

# sns.lineplot(data=rlt, x=rlt.index, y="LT Real Average (>10Yrs)")











# if __name__ == '__main__':
#
#     pass