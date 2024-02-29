class Restaurant:

    def __init__(self, restaurant_name, restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type

    def describe_restaurant(self):
        return f'{self.restaurant_type} is {self.restaurant_type}'

    def open_restaurant(self):
        return f'{self.restaurant_name} is now open'


jollibee = Restaurant('jollibee', 'fast-food')
balay_dako = Restaurant('balay dako', 'fine dining')


print(balay_dako.restaurant_name)
