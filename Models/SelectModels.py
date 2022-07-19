def ModelData(config, DataFrame):
    
    if config['Selected_Model'] == 'Rates of Simple Volatility':
        return DataFrame.rates_of_simple_volatility()
    elif config['Selected_Model'] == 'Rates of Logarithmic Volatility':
        return DataFrame.rates_of_logarithmic_volatility()
    elif config['Selected_Model'] == 'Rates of Return':
        return DataFrame.rates_of_return()
    elif config['Selected_Model'] == 'Rates of Deviation':
        return DataFrame.rates_of_deviation()
    elif config['Selected_Model'] == 'Rates of Deviation':
        return
   