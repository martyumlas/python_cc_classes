from restaurant import Restaurant


class IceCreamStand(Restaurant):

    def __init__(self, name, flavors, restaurant_type='ice cream stand'):
        super().__init__(name, restaurant_type)
        self.flavors = flavors
    def display_flavors(self):
        print('available flavors: \n')
        for flavor in self.flavors:
            print(flavor)

selecta = IceCreamStand('selecta', ['mango', 'ube', 'cheese'])

selecta.description()

selecta.display_flavors()

jollibee = Restaurant('jolibee', 'fast-food')

jollibee.description()

