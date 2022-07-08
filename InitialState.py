import pandas

class InitialState:
  @staticmethod
  def create_dataframe(file_path):
    return pandas.read_csv(
            file_path, skiprows=[0, 2], usecols=[0, 2, 3, 9],
            keep_default_na=False,
        )

    open_position = calculate_dataframe('data/initial.csv')
  
  position_list = []
  
  for i in range(len(open_position)):
    if open_position['Asset'][i] not in position_list:
      position_list.append(Transaction(
        name = open_position['Asset'][i],
        value = open_position['AUD Value'][i],
        event = 'Open Position'
      )
  
  
