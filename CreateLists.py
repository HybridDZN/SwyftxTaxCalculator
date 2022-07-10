import Transaction


class CreateLists:
    buy_list = []
    sell_list = []

    def __init__(self, transactions):
        self.transactions = transactions

    def create_buy_list(self):
        for i in range(len(self.transactions)):
            if self.transactions['Event'][i] == 'buy':
                # buy_list.append(transactions['Asset'][i] + "-" + transactions['AUD Value'][i])
                self.buy_list.append(Transaction.Transaction(
                    name=self.transactions['Asset'][i],
                    value=self.transactions['AUD Value'][i],
                    event=self.transactions['Event'][i]
                ))
        return self.buy_list

    def create_sell_list(self):
        for i in range(len(self.transactions)):
            if self.transactions['Event'][i] == 'sell':
                # buy_list.append(transactions['Asset'][i] + "-" + transactions['AUD Value'][i])
                self.sell_list.append(Transaction.Transaction(
                    name=self.transactions['Asset'][i],
                    value=self.transactions['AUD Value'][i],
                    event=self.transactions['Event'][i]
                ))
        return self.sell_list

    def list_debugger(self):
        print('Buy List:')
        for item in self.buy_list:
            print(item)
        print('Sell List:')
        for item in self.sell_list:
            print(item)
