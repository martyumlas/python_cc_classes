from car import Car

class ElectricCar(Car):
    '''this is a child class of car'''

    def __init__(self, make, model, year):
        '''initialize attribute of the  parent class'''
        super().__init__(make, model, year)
        self.battery_size = 40
    def describe_battery(self):
        print(f'this car has a {self.battery_size}-kwh battery')

    def fill_gas_tank(self, gas=None):
        if gas is not None:
            print("This car doesn't have a gas tank")
        else:
            super().fill_gas_tank(0)

        
brv = Car('Honda', 'brv', '2017')

leaf = ElectricCar('Honda', 'city', '1997')

print(brv.get_descriptive_name())

print(leaf.get_descriptive_name())

leaf.describe_battery()

brv.fill_gas_tank(50)

print(brv.gas)

leaf.fill_gas_tank()

print(leaf.gas)
