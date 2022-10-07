from copy import deepcopy
from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS

from Config.OHLCDataFrontend import OHLCData
from PriceData.AveragePrices import getAveragePrice
from Models.AllModelsFrontend import AllModels
from Models.Models import Modelz
from Models.SelectModels import ModelData

app = Flask(__name__)
CORS(app)
api = Api(app)
# Statistics Data ---------------------

@app.route('/AllModels', methods=['GET'])
def get_all_models():
    """Return an ex-parrot."""
    return{'Metadata':AllModels()}

@app.route('/Statistics', methods=['POST'])
def statistics():
    """Return an ex-parrot."""
    data = request.get_json()
    ohlc_config = data['OHLCConfig']
    model_config = data['ModelConfig']
    StatisticsPriceData = []
    for config_set in ohlc_config:
        return_ohlc_data = OHLCData(config_set)
        price_data = deepcopy(getAveragePrice({'config':config_set,'OHLC': return_ohlc_data}))
        StatisticsPriceData.append({
            'config':config_set,
            'OHLC': return_ohlc_data,
            'Average': price_data
        })
        
    frame = Modelz(StatisticsPriceData)
    rendered_model = ModelData(model_config,frame)
    return {'Config': model_config, 'StatisticsModel': rendered_model}

# host='0.0.0.0'
# app.run(host='localhost',port=5001,debug=True)