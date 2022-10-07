# from PriceData.BinanceOHLCforIndicators import
# from PriceData.MarketStackOHLCforIndicators import 
def getOHLCforIndicatorPrice(PriceDataObject):
    if PriceDataObject['config']['exchange'] == 'Binance':
        OHLCforIndicators = BinanceAvg(PriceDataObject['OHLC'])
        return OHLCforIndicators
    else:
        OHLCforIndicators = MarketStackAvg(PriceDataObject['OHLC'])
        return OHLCforIndicators