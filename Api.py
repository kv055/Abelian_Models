from copy import deepcopy
from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS


from Models.Models import Modelz
from Models.SelectModels import ModelData

from PriceData.Querry_Assets_OHLC_DB_Class import Querry_Assets_OHLC_from_DB

app = Flask(__name__)
CORS(app)
api = Api(app)
# Statistics Data ---------------------


@app.route('/Statistics', methods=['POST'])
def statistics():
    """Return an ex-parrot."""
    data = request.get_json()
    ohlc_config = data['OHLCConfig']
    model_config = data['ModelConfig']
    StatisticsPriceData = []
    get_OHLC_db = Querry_Assets_OHLC_from_DB()
    for config_set in ohlc_config:
        ohlc_data = get_OHLC_db.return_historical_ohlc_from_db(config_set['assetPair'])
        average_price_data = get_OHLC_db.return_historical_average_from_db(config_set['assetPair'])
        StatisticsPriceData.append({
            'config':config_set,
            'OHLC': ohlc_data,
            'Average': average_price_data
        })
        
    frame = Modelz(StatisticsPriceData)
    rendered_model = ModelData(model_config,frame)
    return {'Config': model_config, 'StatisticsModel': rendered_model}

# host='0.0.0.0'
# app.run(host='localhost',port=5001,debug=True)