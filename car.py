class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas = 0

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()
    
    def read_odometer(self):
        print(f'this car has {self.odometer_reading} miles on it')

    def update_odometer(self, mileage):
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self, gas):
        self.gas += gas
        

'''
my_new_car = Car('honda', 'brv', '2017')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
'''

'''

modifying attributes

#directly

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#by method

my_new_car.update_odometer(60)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()

'''

