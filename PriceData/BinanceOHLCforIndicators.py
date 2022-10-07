import numpy

def OHLCformated(CandleData):
    # creating empty lists
    date = []
    op = []
    hi = []
    lo = []
    cl = []

    # pushing data into lists
    for element in CandleData:
        date.append(element[0])
        op.append(element[1])
        hi.append(element[2])
        lo.append(element[3])
        cl.append(element[4])

    # converting list to array (for talib)
    open = numpy.array(op)
    high = numpy.array(hi)
    low = numpy.array(lo)
    close = numpy.array(cl)

    return {
        'date': date,
        'open': open,
        'high': high,
        'low': low,
        'close': close
    }