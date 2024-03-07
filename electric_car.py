from battery import Battery
from car import Car

class ElectricCar(Car):
    '''this is a child class of car'''

    def __init__(self, make, model, year):
        '''initialize attribute of the  parent class'''
        super().__init__(make, model, year)
        self.battery = Battery()

    # def describe_battery(self):
    #     print(f'this car has a {self.battery}-kwh battery')

    def fill_gas_tank(self, gas=None):
        if gas is None:
            print(f'This car doesn\'t have a gas tank!')

my_honda_city = Car('honda', 'city', '2000')
print(my_honda_city.get_descriptive_name())
my_honda_city.fill_gas_tank(50)
print(f'currently have {my_honda_city.gas} liters of gas')

print('------------------')

'''instance of electric car'''
leaf = ElectricCar('nissan', 'leaf', '2014')
print(leaf.get_descriptive_name())
leaf.battery.describe_battery_size()
leaf.fill_gas_tank()
