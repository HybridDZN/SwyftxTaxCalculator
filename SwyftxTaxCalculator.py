import pandas

from CreateLists import CreateLists
from FIFO import FIFO
import InitialHoldings

transactions = pandas.read_csv(
    'data/transactions.csv', skiprows=[0], usecols=[0, 2, 3, 9],
    keep_default_na=False)  # Columns being used: Date, Event, Asset, AUD Value

initial_holdings = InitialHoldings.InitialHoldings()

list_creator = CreateLists(transactions)
buy_list = list_creator.create_buy_list()
sell_list = list_creator.create_sell_list()
