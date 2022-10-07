import requests

def Tickers(exchange):
    params = {
    'access_key': 'ba7ca8e055c2c866659a548df9fdb01a'
    }
    tickers = {
        'name': exchange['name'],
        'assetPairs':[],
        'candleSize' : [
            '1min',
            '5min',
            '10min',
            '15min',
            '30min',
            '1hour', 
            '3hour',
            '6hour',
            '12hour',
            '24hour'
        ] 
    }

    tickersRaw = requests.get('https://api.marketstack.com/v1/exchanges/'+exchange['mic']+'/tickers?access_key=ba7ca8e055c2c866659a548df9fdb01a')
    # tickersRaw = requests.get('https://api.marketstack.com/v1/exchanges/XNAS/tickers?access_key=ba7ca8e055c2c866659a548df9fdb01a')
    tickersJson = tickersRaw.json()
    for stock in tickersJson['data']['tickers']:
       tickers['assetPairs'].append(
        {'symbol':stock['symbol'],'name':stock['name']}
        ) 

    return tickers


     # 'candleSize' :{
        #     'Minute1' : '1min',
        #     'Minutes5': '5min',
        #     'Minutes10': '10min',
        #     'Minutes15' : '15min',
        #     'Minutes30' : '30min',
        #     '1Hour': '1hour', 
        #     '3Hours': '3hour',
        #     '6Hours' : '6hour',
        #     '12Hours' : '12hour',
        #     '1Day': '24hour'
        # }