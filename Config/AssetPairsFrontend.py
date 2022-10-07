from Config.BinanceFetchTickers import BinanceMetaData
from Config.MarketStackFetchTickers import Tickers
def AssetPairs(exchange):
    if exchange['name'] == 'Binance':
        return BinanceMetaData()
    elif exchange['name'] == 'Bitstamp':
        return BinanceMetaData()
    elif exchange['name'] == 'Bitfinex':
        return BinanceMetaData()
    elif exchange['name'] == 'Coinbase':
        return BinanceMetaData()
    elif exchange['name'] == 'FTX':
        return BinanceMetaData()
    elif exchange['name'] == 'Gemini':
        return BinanceMetaData()
    elif exchange['name'] == 'Kraken':
        return BinanceMetaData()
    else:
        return Tickers(exchange)

