import pandas


class InitialHoldings:
    @staticmethod
    def generate_dataframe(file_path):
        return pandas.read_csv(
            file_path, skiprows=[0, 2], usecols=[0, 2, 3, 9],
            keep_default_na=False,
        )

    open_position = generate_dataframe('data/initial.csv')
    # print('Initial State')
    # print(open_position)
    position_map = {}
    for i in range(len(open_position)):
        if open_position['Asset'][i] not in position_map:
            position_map[open_position['Asset'][i]] = open_position['AUD Value'][i]
    position_map = {key: value for key, value in position_map.items() if value >= 1.0}

    def print_initial_holdings(self):
        print('\nInitial Holdings Dictionary')
        print('Asset : Initial Value')
        for key, value in self.position_map.items():
            print(key, ' : ', value)

    def get_values(self):
        return self.position_map.values()