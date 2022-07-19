"""Module"""

# from scipy import stats
# import statsmodels.api as sm
import numpy as np
from Models.PriceData2DataFrame import Creator

class Modelz():
    """Class"""
    def __init__(self,StatisticsPriceData) -> None:
        self.data_frame_instance = Creator(StatisticsPriceData)
        self.Dataframe = self.data_frame_instance.PriceData

    def rates_of_logarithmic_volatility(self):
        """Method"""
        index_list = list(self.Dataframe.index.values)
        renedered_model = []
        for rowName, rowData in self.Dataframe.iteritems():
            self.Dataframe[rowName] = np.log(self.Dataframe[rowName] / self.Dataframe[rowName].shift(1))
            list_column = self.Dataframe[rowName].values.tolist()
            renedered_model.append({'Asset': rowName, 'Value': list_column, 'Time': index_list })
        return renedered_model

    def rates_of_simple_volatility(self):
        """Method"""
        index_list = list(self.Dataframe.index.values)
        renedered_model = []
        for rowName, rowData in self.Dataframe.iteritems():
            self.Dataframe[rowName] = (self.Dataframe[rowName] / self.Dataframe[rowName].shift(1)) - 1
            list_column = self.Dataframe[rowName].values.tolist()
            renedered_model.append({'Asset': rowName, 'Value': list_column, 'Time': index_list })
        return renedered_model

    def rates_of_return(self):
        """Method"""
        normalized_list = (self.Dataframe / self.Dataframe.iloc[0] * 100)
        index_list = list(normalized_list.index.values)
        renedered_model = []
        for column in normalized_list:
            lamana = normalized_list[column].tolist()
            renedered_model.append({'Asset': column, 'Value': lamana, 'Time': index_list })

        return renedered_model


    def rates_of_deviation(self):
        """Method"""
        index_list = list(self.Dataframe.index.values)
        renedered_model = []
        for rowName, rowData in self.Dataframe.iteritems():
            self.Dataframe[rowName] = np.log(self.Dataframe[rowName] / self.Dataframe[rowName].shift(1))
            list_column = self.Dataframe[rowName].values.tolist()
            renedered_model.append({'Asset': rowName, 'Value': list_column, 'Time': index_list })
        return renedered_model


    # def Rates_of_Corelation(self):
    #     pass


        # for rowName, rowData in self.Dataframe.iteritems():
    #     self.Dataframe['Simple Return'] = (self.Dataframe[rowName] / self.Dataframe[rowName].shift(1)) - 1
    #     self.Dataframe['Logarithmic Return'] = np.log(self.Dataframe[rowName] / self.Dataframe[rowName].shift(1))
    #     self.Jochen = self.Dataframe.values.tolist()
    #     self.dictToReturn.append(self.Jochen)
    #     print('Jochen', self.Jochen)
        # print(rowName+' Simple Return raw: ',self.Dataframe['Simple Return'])
        # print(rowName+' Logarithmic Return raw: ',self.Dataframe['Logarithmic Return'])

