class Restaurant():
    '''restaurant class'''

    def __init__(self, name, restaurant_type):
        self.name = name
        self.restaurant_type = restaurant_type

    def description(self):
        print(f'{self.name} is {self.restaurant_type}')

    def open(self):
        print(f'{self.name} is now open')


jolibee = Restaurant('jolibee', 'fast-food')

print(jolibee.name)
print(jolibee.restaurant_type)
jolibee.description()
jolibee.open()




