class Transaction:

    def __init__(self, name, value, event):
        self.name = name
        self.value = value
        self.event = event

    def get_value(self):
        return self.value

    def __str__(self):
        print('Asset: ', self.name, '| Value: ', end="")
        # print('Event: ', end=" ")
        return self.value
