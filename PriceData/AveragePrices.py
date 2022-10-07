from PriceData.BinanceAveragePrice import AveragePrice as BinanceAvg
from PriceData.MarketStackAveragePrice import AveragePrice as MarketStackAvg

def getAveragePrice(PriceDataObject):
    if PriceDataObject['config']['exchange'] == 'Binance':
        AveragePrice = BinanceAvg(PriceDataObject['OHLC'])
        return AveragePrice
    else:
        AveragePrice = MarketStackAvg(PriceDataObject['OHLC'])
        return AveragePrice