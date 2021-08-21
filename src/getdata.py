import quandl
import pandas as pd


def get_quandl_data(dataset, start_date, end_date, api_key, store=False):

    # api sey setup
    quandl.ApiConfig.api_key = api_key

    # import quandl data
    df = quandl.get(dataset=dataset, start_date=start_date, end_date=end_date)

    # write to hdf5
    if store:
        pd.HDFStore('data/rlt.h5', 'w')

    return df


def get_glassnode_data():
    # TODO
    pass

