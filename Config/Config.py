import PriceData.BinanceFetch as BinanceFetch
# Fetching PriceData (in this Case Bitcoin vs USD)
# Output format is OHLC (Candlestick)
CandleSticks = BinanceFetch.PriceDataFetch()

#Import Formated Price Data
from PriceData.AverageWDate import AveragePrice
# Formating CandleStick to Average Price
PriceData = AveragePrice(CandleSticks)
