import find_parent
import talib as talib
import numpy

def AveragePrice(CandleData):
    # creating empty lists
    op = []
    hi = []
    lo = []
    cl = []

    # pushing data into lists
    for element in CandleData:
        op.append(element[1])
        hi.append(element[2])
        lo.append(element[3])
        cl.append(element[4])

    # converting list to array (for talib)
    open = numpy.array(op)
    high = numpy.array(hi)
    low = numpy.array(lo)
    close = numpy.array(cl)

    Average = [[], []]

    # Pushing Data into the Average List
    for element in CandleData:
        Average[0].append(str(element[0]))

    # Calculating Average Price
    for element in talib.AVGPRICE(open, high, low, close).tolist():
        Average[1].append(element)

    return Average
