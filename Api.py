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
    Models_Config_Data = request.get_json()
    frame = Modelz(Models_Config_Data)
    rendered_model = ModelData(Models_Config_Data,frame)
    return {'Config': Models_Config_Data, 'StatisticsModel': rendered_model}

# host='0.0.0.0'
# app.run(host='localhost',port=5001,debug=True)