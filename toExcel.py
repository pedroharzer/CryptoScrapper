import pandas as pd
from openpyxl import *
from scraping import *
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
coinNames = ['Bitcoin', 'Ethereum', 'ETH', 'BTC', 'ADA', 'XRP', 'DOGE', 'DOT', 'UNI', 'BCH', 'LTC', 'AXS', 'AAVE', 'LUNA', 'TATA']
coinNews = []
controlString = ''
controlArray = []
def buildDict(data, coinNames,coinNews, controlString, controlArray):
    newDict = {
        'News' : data
    }
    for news in newDict['News']: #loop pelos titulos
        for coin in coinNames: #loop para verificar se as moedas em "CoinName" se encontram em cada titulo
            print("coin " + coin)
            if news.count(coin) > 0:
                controlArray.append(coin)
        for coins in controlArray:
                #vou juntar tudo em uma string e guardar essa string na array, depois vou limpar a array
            controlString += coins + " "
        if controlString.__len__()> 0:
            coinNews.append(controlString)
        else:
            coinNews.append('Not coin related')
        controlString = ''
        controlArray.clear()
    newDict.update({
        'Coin' : coinNews
    })
    return newDict
def buildDataFrame(info):
    df = pd.DataFrame(data = info)
    return df
data = soupMess('span', 'post-card-inline__title')
info = buildDict(data, coinNames, coinNews, controlString, controlArray)
dataframe = buildDataFrame(info)
try:
    dataframe.to_excel('Tabela.xlsx', index=False)
    print('Tabela criada!')
except:
    print('falhei')
 
