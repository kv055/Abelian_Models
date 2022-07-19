import pandas as pd

class BinanceDataFrame():
    def __init__(self,arrayListe) -> None:
        self.PriceDataFrame = pd.DataFrame(
            # arrayListe()
            arrayListe
            ,columns=(
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
        

class MergeDataFrames():
    def __init__(self, MergeDataFramesArray) -> None:
       self.merged = pd.concat(MergeDataFramesArray,axis=1, join='inner')


class Creator():
    def __init__(self, priceDataSets) -> None:
        self.Frames2Merge = []
        for element in priceDataSets:
            temp = BinanceDataFrame(element['OHLC'])
            # ,element['config']['assetPair']
            temp.average(element['config']['assetPair'])
            temp.PriceDataFrame.set_index("TimeStamp", inplace = True)
            self.Frames2Merge.append(temp.PriceDataFrame)
        Frame = MergeDataFrames(self.Frames2Merge)
        self.PriceData = Frame.merged
        
