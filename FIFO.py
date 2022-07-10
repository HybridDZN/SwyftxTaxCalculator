class FIFO:
    total_value = 0

    def __init__(self, transactions, buy_list, sell_list):
        self.transactions = transactions
        self.buy_list = buy_list
        self.sell_list = sell_list

    def calculate(self):
        for transaction in range(len(self.transactions)):
            if self.transactions['Event'][transaction] == 'sell':
                current_buy = self.buy_list.pop()
                for item in range(len(self.sell_list)):
                    if transaction['Asset'][item] == self.sell_list.name[item]:
                        print('success')
