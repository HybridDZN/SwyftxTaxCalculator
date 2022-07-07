import pandas


class InitialHoldings:
    @staticmethod
    def calculate_initial_holdings(file_path):
        return pandas.read_csv(
            file_path, skiprows=[0, 2], usecols=[0, 2, 3, 9],
            keep_default_na=False,
        )
    open_position = calculate_initial_holdings('data/initial.csv')
    # print('Initial State')
    # print(open_position)
    position_map = {}
    for i in range(len(open_position)):
        if open_position['Asset'][i] not in position_map:
            position_map[open_position['Asset'][i]] = open_position['AUD Value'][i]
    position_map = {key: value for key, value in position_map.items() if value >= 1.0}
    print('\nInitial Holdings Dictionary')
    print('Asset : Initial Value')
    for key, value in position_map.items():
        print(key, ' : ', value)
