from Config.BinanceFetchFrontend import PriceDataFetch as BinanceOHLCFetch
from Config.MarketStackFetchFrontend import PriceDataFetch as MarketStackOHLCFetch

def OHLCData(OhlcConfig):
    if OhlcConfig['exchange'] == 'Binance':
        return BinanceOHLCFetch(OhlcConfig["assetPair"], OhlcConfig['candleSize'])
    elif OhlcConfig['exchange'] == 'Bitstamp':
        return BinanceOHLCFetch(OhlcConfig["assetPair"], OhlcConfig['candleSize'])
    elif OhlcConfig['exchange'] == 'Bitfinex':
        return BinanceOHLCFetch(OhlcConfig["assetPair"], OhlcConfig['candleSize'])
    elif OhlcConfig['exchange'] == 'Coinbase':
        return BinanceOHLCFetch(OhlcConfig["assetPair"], OhlcConfig['candleSize'])
    elif OhlcConfig['exchange'] == 'FTX':
        return BinanceOHLCFetch(OhlcConfig["assetPair"], OhlcConfig['candleSize'])
    elif OhlcConfig['exchange'] == 'Gemini':
        return BinanceOHLCFetch(OhlcConfig["assetPair"], OhlcConfig['candleSize'])
    elif OhlcConfig['exchange'] == 'Kraken':
        return BinanceOHLCFetch(OhlcConfig["assetPair"], OhlcConfig['candleSize'])
    else:
        return MarketStackOHLCFetch(OhlcConfig["assetPair"])