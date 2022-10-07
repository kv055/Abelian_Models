import requests
def BinanceMetaData():
    response = requests.get('https://api.binance.com/api/v3/exchangeInfo')
    json = response.json()

    Binance = {
        'name':'Binance',
        'assetPairs':[],
        'candleSize' : [
            '1m',
            '3m',
            '5m',
            '15m',
            '30m',
            '1h', 
            '2h',
            '4h',
            '6h',
            '8h',
            '12h',
            '1d',
            '3d',
            '1w',
            '1M'
        ]
    }

    for element in json['symbols']:
        Binance['assetPairs'].append({'symbol':element['symbol'],'name':element['symbol']})

    # Binance['assetPairs'].sort()
    
    return Binance

# 'candleSize' : {
#             'Minute1' : '1m',
#             'Minutes3' : '3m',
#             'Minutes5': '5m',
#             'Minutes15' : '15m',
#             'Minutes30' : '30m',
#             '1Hour': '1h', 
#             '2Hours': '2h',
#             '4Hours' : '4h',
#             '6Hours' : '6h',
#             '8Hours' : '8h',
#             '12Hours' : '12h',
#             '1Day': '1d',
#             '3Days' : '3d',
#             '1Week': '1w',
#             '1Month': '1M'
#         }