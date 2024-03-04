class Restaurant():
    '''restaurant class'''

    def __init__(self, name, restaurant_type):
        self.name = name
        self.restaurant_type = restaurant_type
        self.number_serve = 0

    def description(self):
        print(f'{self.name} is {self.restaurant_type}')

    def open(self):
        print(f'{self.name} is now open')
    
    def set_number_served(self, num):
        self.number_serve = num

    def increment_number_served(self, num):
        self.number_serve += num

# jolibee = Restaurant('jolibee', 'fast-food')
#
# print(jolibee.number_serve)
#
# jolibee.set_number_served(6)
#
# print(jolibee.number_serve)
#
# jolibee.increment_number_served(10)
#
# print(jolibee.number_serve)
