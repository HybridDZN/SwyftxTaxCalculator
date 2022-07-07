import pandas
import InitialHoldingsSetup
from collections import deque


transactions = pandas.read_csv(
    'data/transactions.csv', skiprows=[0], usecols=[0, 2, 3, 9],
    keep_default_na=False)  # Columns being used: Date, Event, Asset, AUD Value


initial_holdings = InitialHoldingsSetup.InitialHoldings()

assetList = []
buyQueueList = []
# transactions = transactions[1:(transactions['Date'] == 'Fiat Transactions')]

# Populate list of assets
for i in range(len(transactions)):
    asset = transactions['Asset'][i]
    if asset not in assetList and asset != 'Asset':
        assetList.append(str(asset))

assetList.sort()
assetList.remove(assetList[0])
# Debug print to see what is in the list
# print("Asset List: ")
# print(assetList)


currentAssetIndex = 0
buyQueue = deque()
totalSells = 0

for i in range(len(transactions)):
    if transactions['Event'][i] == 'buy':
        buyQueue.append(transactions.iloc[i])

#print(list(buyQueue))
#print('Total buy events: ' + str(len(buyQueue)))

sellQueue = deque()
for i in range(len(transactions)):
    if transactions['Event'][i] == 'sell':
        sellQueue.append((transactions.iloc[i]))

#print(list(sellQueue))
#print('Total buy events: ' + str(len(buyQueue)))
#print('Total sell events: ' + str(len(sellQueue)))

for i in range(len(transactions)):
    if transactions['Asset'][i] == assetList[currentAssetIndex]:
        if transactions['AUD Value'][i] == 'sell':
            #print(buyQueue.pop())
            currentAssetIndex += 1


# print(list(buyQueue))
# print(totalSells)





