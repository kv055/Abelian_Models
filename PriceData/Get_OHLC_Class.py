"""
This is the object oriented version of the "Price data" folder
One benefit of using these class calls can be seen in app.py
wherein the bin_url can be inserted later on
This allows for any data source to be used at runtime.
"""
from datetime import datetime

import numpy
# import talib
import pandas as pd
import requests

from PriceData.Request_URL_Generators import generate_request


# from Database_SQL.query_assets import return_all_asset_URLs
class Import_OHLC_Data:
    """Fetching OHLC Data from various api's"""
    def __init__(self, ohlc_config):
        self.fetch_config = ohlc_config
        self.request_args = generate_request(ohlc_config)


    def get_historical_OHLC(self, asset):
        if asset['data_provider'] == 'Alpaca':
            Alpaca_to_fetch = self.request_args.Alpaca(asset['URL'])
            url_to_fetch = Alpaca_to_fetch[0]
            req_body = Alpaca_to_fetch[1]
            self.response_raw = requests.get(url_to_fetch,req_body)
            self.json = self.response_raw.json()

        if asset['Data_Provider'] == 'Binance':
            url_to_fetch = self.request_args.Binance(asset['URL'])
            response_raw = requests.get(url_to_fetch)
            self.nformated_dataset = self.response_raw.json()
            # Change the weird timestamps from Binanace to propper 
            # ones that actually work
            for ohlc in self.unformated_dataset:
                new_time_stamp = round(ohlc[0] / 1000)
                ohlc[0] = new_time_stamp

        if asset['Data_Provider'] == 'Kraken':
            url_to_fetch = self.request_args.Kraken(asset['URL'])
            response_raw = requests.get(url_to_fetch)
            json = response_raw.json()
            keys = list(json['result'].keys())
            self.unformated_dataset = json['result'][keys[0]]


    def format_data(self):
        """
        It can be advantageous to determine whether data has been formatted already
        This has the benefit of code readability wherein "format_data" is always called,
        but the system doesn't have to re-run the format if not required
        """
        self.formatted = []

        for element in self.unformated_dataset:
            # op = round(float(element[1]), 3)
            # hi = round(float(element[2]), 3)
            # lo = round(float(element[3]), 3)
            # cl = round(float(element[4]), 3)
            op = float(element[1])
            hi = float(element[2])
            lo = float(element[3])
            cl = float(element[4])
            self.formatted.append([element[0], op, hi, lo, cl])

        return self.formatted


class ImportData:
    """Class"""
    def __init__(self):
        self.bin_url = 'https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=70'
        self.formatted = []
        self.json = None
        self.connect_data()
        self.is_formatted = False

    def connect_data(self, url=None):
        """if we want to load data other than the url specified in __init__"""
        if url is not None:
            self.bin_url = url
        response = requests.get(self.bin_url)
        self.json = response.json()
        # new data has been loaded, thus not formatted
        self.is_formatted = False

    def format_data(self):
        """
        It can be advantageous to determine whether data has been formatted already
        This has the benefit of code readability wherein "format_data" is always called,
        but the system doesn't have to re-run the format if not required
        """
        if self.is_formatted:
            return True

        for element in self.json:
            op = round(float(element[1]), 3)
            hi = round(float(element[2]), 3)
            lo = round(float(element[3]), 3)
            cl = round(float(element[4]), 3)
            # op = float(element[1])
            # hi = float(element[2])
            # lo = float(element[3])
            # cl = float(element[4])
            self.formatted.append([round(element[0] / 1000), op, hi, lo, cl])
        self.is_formatted = True
        return True

    def get_format_data(self):
        """Method"""
        if len(self.formatted) < 1:
            self.format_data()
        return self.formatted

    def reset_format_data(self):
        """Method"""
        self.formatted = []

    def convert_to_numpy_array(self):
        """Method"""
        # creating empty lists
        date = []
        op = []
        hi = []
        lo = []
        cl = []

        # pushing data into lists
        for element in self.formatted:
            date.append(element[0])
            op.append(element[1])
            hi.append(element[2])
            lo.append(element[3])
            cl.append(element[4])

        # converting list to array (for talib)
        
        open = numpy.array(op)
        high = numpy.array(hi)
        low = numpy.array(lo)
        close = numpy.array(cl)
        self.numpy_array = {
            
        }

    # def calc_average(self):
    #     """Method"""
    #     for averaged_price in talib.AVGPRICE(op, hi, lo, cl).tolist():
    #         self.average[1].append(averaged_price)

    def get_average(self):
        """Method"""
        if len(self.average[0]) == 0 or len(self.average[1]) == 0:
            self.calc_average()
        return self.average

    def create_pandas_dataframe(self):
        self.PriceDataFrame = pd.DataFrame(
            # arrayListe()
            # arrayListe,
            columns=(
            'TimeStamp','Open','High','Low','Close'
            # ,'Volume','Close time',
            # 'Quote asset volume','Number of trades','Taker buy base asset volume',
            # 'Taker buy quote asset volume','ignore'
            )
        )



        
    def average(self, name):
        # self.PriceDataFrame['TimeStamp']= pd.to_datetime(self.PriceDataFrame['TimeStamp'], unit='ms')
        # self.PriceDataFrame.set_index("TimeStamp", inplace = True)
        self.PriceDataFrame["Close"] = pd.to_numeric(self.PriceDataFrame["Close"])

        del self.PriceDataFrame['Open']
        del self.PriceDataFrame['High']
        del self.PriceDataFrame['Low']
        # del self.PriceDataFrame['Volume']
        # del self.PriceDataFrame['Close time']
        # del self.PriceDataFrame['Quote asset volume']
        # del self.PriceDataFrame['Number of trades']
        # del self.PriceDataFrame['Taker buy base asset volume']
        # del self.PriceDataFrame['Taker buy quote asset volume']
        # del self.PriceDataFrame['ignore']

        self.PriceDataFrame.rename(columns = {'Close':name}, inplace = True) 

    def ohlc(self):
        # self.PriceDataFrame['TimeStamp']= pd.to_datetime(self.PriceDataFrame['TimeStamp'], unit='ms')
        self.PriceDataFrame.set_index("TimeStamp", inplace = True)
    
        self.PriceDataFrame['Open'] = pd.to_numeric(self.PriceDataFrame['Open'])
        self.PriceDataFrame['High'] = pd.to_numeric(self.PriceDataFrame['High'])
        self.PriceDataFrame['Low'] = pd.to_numeric(self.PriceDataFrame['Low'])
        self.PriceDataFrame['Close'] = pd.to_numeric(self.PriceDataFrame["Close"])    
        

    def MergeDataFrames(self, MergeDataFramesArray):
       self.merged = pd.concat(MergeDataFramesArray,axis=1, join='inner')

    def Creator(self, priceDataSets) -> None:
        self.Frames2Merge = []
        for element in priceDataSets:
            temp = self.create_pandas_dataframe(element['OHLC'])
            # ,element['config']['assetPair']
            temp.average(element['config']['assetPair'])
            temp.PriceDataFrame.set_index("TimeStamp", inplace = True)
            self.Frames2Merge.append(temp.PriceDataFrame)
        Frame = self.MergeDataFrames(self.Frames2Merge)
        self.PriceData = Frame.merged