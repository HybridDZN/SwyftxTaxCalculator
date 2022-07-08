class Transaction:

    def __init__(self, name, value, event):
        self.name = name
        self.value = value
        self.event = event

    def __str__(self):
        print('Asset: ', self.name)
        print('Value: ', self.value)
        print('Event: ', end=" ")
        return self.event

    
