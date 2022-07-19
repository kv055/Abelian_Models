def LiquidationLevel():
    price = 0
    tradecollateral = 400
    accountballance = 450
    faktor = 3
    einstiegspreis = 11100
    short = False
    
    schwankungAbsolut = price - einstiegspreis
    schwankung = ((price / einstiegspreis) - 1) * 100

    leverage = tradecollateral * faktor

    profitloss = 0

    liquidationlevel = 0

    if short == False:
        profitloss = (leverage / 100) * schwankung
        liquidationlevel = ((0.8 * tradecollateral) - accountballance) / (leverage / 100)
    else:
        profitloss = (leverage / 100) * (-schwankung)
        liquidationlevel = (-((0.8 * tradecollateral) - accountballance) / (leverage / 100))
 

    equity = accountballance + profitloss
    marginlevel = (equity / tradecollateral) * 100
    liquidationpreis = einstiegspreis-((-liquidationlevel * 0.01)*einstiegspreis)