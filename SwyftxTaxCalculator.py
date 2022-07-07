import pandas
import InitialHoldingsSetup
from collections import deque



transactions = pandas.read_csv(
    'data/transactions.csv', skiprows=[0], usecols=[0, 2, 3, 9],
    keep_default_na=False)  # Columns being used: Date, Event, Asset, AUD Value

initial_holdings = InitialHoldingsSetup.InitialHoldings()

buy_list = []
sell_list = []
asset_iterator = 0
asset_list = list(initial_holdings.position_map.keys())
current_asset_value = initial_holdings.position_map[transactions['Asset'][asset_iterator]]

for i in range(len(transactions)):
    if transactions['Event'][i] == 'buy':
        buy_list.append('' + transactions['Asset'][i] + " " + transactions['AUD Value'][i])

print('Buy List:')
print(buy_list)

for i in range(len(transactions)):
    if transactions['Event'][i] == 'sell':
        sell_list.append('' + transactions['Asset'][i] + " " + transactions['AUD Value'][i])

print('Sell List:')
print(sell_list)
