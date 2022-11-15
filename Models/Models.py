"""Module"""

# from scipy import stats
# import statsmodels.api as sm
import numpy as np
from Models.PriceData2DataFrame import Creator
from PriceData.Get_Price_Data_Class import Import_Price_Data

class Modelz():
    """Class"""
    def __init__(self, config_dict) -> None:
        self.price_data_instance = Import_Price_Data()
        self.list_of_asset_dicts = config_dict['OHLCConfig']
        self.model_config = config_dict['ModelConfig']
        self.data_frame_instance = self.price_data_instance.return_merged_average_price_data_frames(
            self.list_of_asset_dicts
            )

    def rates_of_logarithmic_volatility(self):
        """Method"""
        index_list = list(self.data_frame_instance.index.values)
        renedered_model = []
        for rowName, rowData in self.data_frame_instance.iteritems():
            self.data_frame_instance[rowName] = np.log(self.data_frame_instance[rowName] / self.data_frame_instance[rowName].shift(1))
            list_column = self.data_frame_instance[rowName].values.tolist()
            renedered_model.append({'Asset': rowName, 'Value': list_column, 'Time': index_list })
        return renedered_model

    def rates_of_simple_volatility(self):
        """Method"""
        index_list = list(self.data_frame_instance.index.values)
        renedered_model = []
        for rowName, rowData in self.data_frame_instance.iteritems():
            self.data_frame_instance[rowName] = (self.data_frame_instance[rowName] / self.data_frame_instance[rowName].shift(1)) - 1
            list_column = self.data_frame_instance[rowName].values.tolist()
            renedered_model.append({'Asset': rowName, 'Value': list_column, 'Time': index_list })
        return renedered_model

    def rates_of_return(self):
        """Method"""
        normalized_list = (self.data_frame_instance / self.data_frame_instance.iloc[0] * 100)
        index_list = list(normalized_list.index.values)
        renedered_model = []
        for column in normalized_list:
            lamana = normalized_list[column].tolist()
            renedered_model.append({'Asset': column, 'Value': lamana, 'Time': index_list })

        return renedered_model

    def rates_of_deviation(self):
        """Method"""
        index_list = list(self.data_frame_instance.index.values)
        renedered_model = []
        for rowName, rowData in self.data_frame_instance.iteritems():
            self.data_frame_instance[rowName] = np.log(self.data_frame_instance[rowName] / self.data_frame_instance[rowName].shift(1))
            list_column = self.data_frame_instance[rowName].values.tolist()
            renedered_model.append({'Asset': rowName, 'Value': list_column, 'Time': index_list })
        return renedered_model


    # def Rates_of_Corelation(self):
    #     pass


        # for rowName, rowData in self.data_frame_instance.iteritems():
    #     self.data_frame_instance['Simple Return'] = (self.data_frame_instance[rowName] / self.data_frame_instance[rowName].shift(1)) - 1
    #     self.data_frame_instance['Logarithmic Return'] = np.log(self.data_frame_instance[rowName] / self.data_frame_instance[rowName].shift(1))
    #     self.Jochen = self.data_frame_instance.values.tolist()
    #     self.dictToReturn.append(self.Jochen)
    #     print('Jochen', self.Jochen)
        # print(rowName+' Simple Return raw: ',self.data_frame_instance['Simple Return'])
        # print(rowName+' Logarithmic Return raw: ',self.data_frame_instance['Logarithmic Return'])

