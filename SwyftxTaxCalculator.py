import pandas
import InitialHoldings
from collections import deque

import Transaction

transactions = pandas.read_csv(
    'data/transactions.csv', skiprows=[0], usecols=[0, 2, 3, 9],
    keep_default_na=False)  # Columns being used: Date, Event, Asset, AUD Value

initial_holdings = InitialHoldings.InitialHoldings()

buy_list = []
sell_list = []
asset_iterator = 0
asset_list = list(initial_holdings.position_map.keys())
current_asset_value = initial_holdings.position_map[transactions['Asset'][asset_iterator]]

for i in range(len(transactions)):
    if transactions['Event'][i] == 'buy':
        # buy_list.append(transactions['Asset'][i] + "-" + transactions['AUD Value'][i])
        buy_list.append(Transaction.Transaction(
            name=transactions['Asset'][i],
            value=transactions['AUD Value'][i],
            event=transactions['Event'][i]
        ))

for i in range(len(transactions)):
    if transactions['Event'][i] == 'sell':
        # buy_list.append(transactions['Asset'][i] + "-" + transactions['AUD Value'][i])
        buy_list.append(Transaction.Transaction(
            name=transactions['Asset'][i],
            value=transactions['AUD Value'][i],
            event=transactions['Event'][i]
        ))

print('Buy List:')
for item in buy_list:
    print(item)

print('Sell List:')
for item in buy_list:
    print(item)
