from alpaca.data.historical import CryptoHistoricalDataClient ,StockHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest ,StockBarsRequest

from alpaca.data.timeframe import TimeFrame

import datetime
from dateutil.relativedelta import relativedelta

import os
from dotenv import load_dotenv

load_dotenv()

month = datetime.datetime.now().month-6
time = datetime.date.today()-relativedelta(month=month)
time = str(time)

clientscrypto = CryptoHistoricalDataClient()
clientsstock = StockHistoricalDataClient(api_key=os.getenv("API_KEY"), secret_key=os.getenv("SECRET_KEY"))

def req_objectcrypto(token):
    request = CryptoBarsRequest(
        symbol_or_symbols=[token],
        timeframe=TimeFrame.Day,
        start=datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month,int(time[8:10])-1),
        end=datetime.datetime(int(time[0:4]),int(time[5:7]),int(time[8:10]))
    )
    req_bars = clientscrypto.get_crypto_bars(request)
    return req_bars.df

def req_objectstock(token):
    request = StockBarsRequest(
        symbol_or_symbols=[token],
        timeframe=TimeFrame.Hour,
        start=datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month,int(time[8:10])-1),
        end=datetime.datetime(int(time[0:4]),int(time[5:7]),int(time[8:10]))
    )
    req_bars = clientsstock.get_stock_bars(request)
    return req_bars.df
print(req_objectcrypto("BTC/USD"))
print(req_objectstock("AAPL"))