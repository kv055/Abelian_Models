import find_parent
from Config.MarketStackFetchExchanges import MarketStackData

def DataSources():
    Sources = [
        {'name': 'Binance', 'mic': 'Binance'},
        {'name': 'Bitfinex', 'mic': 'Binance'},
        {'name': 'FTX', 'mic': 'Binance'},
        {'name': 'Kraken', 'mic': 'Binance'},
        {'name': 'Coinbase', 'mic': 'Binance'},
        {'name': 'Gemini', 'mic': 'Binance'},
        {'name': 'Bitstamp', 'mic': 'Binance'}
    ]

    # for element in MarketStackData()['Exchanges']:
    #     Sources.append(element)

    return Sources
