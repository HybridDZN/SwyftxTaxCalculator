import InitialHoldings


def calculate_initial_average():
    initial_list = InitialHoldings.InitialHoldings().get_values()
    list_total = 0
    for i in range(len(initial_list)):
        list_total += list(initial_list)[i]
    return list_total


class Average:
    def __init__(self, transactions, buy_list, sell_list):
        self.transactions = transactions
        self.buy_list = buy_list
        self.sell_list = sell_list

    def total_buy_calculator(self):
        buy_total = 0
        for i in range(len(self.buy_list)):
            buy_total += float(self.buy_list[i].get_value())
        return buy_total

    def total_sell_calculator(self):
        sell_total = 0
        for i in range(len(self.sell_list)):
            sell_total += float(self.sell_list[i].get_value())
        return sell_total

    def calculate_average(self):
        final = self.total_sell_calculator()- self.total_buy_calculator()
        return final
