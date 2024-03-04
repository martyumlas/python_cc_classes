class Battery:

    def __init__(self, battery_size=40):
        '''initialize battery'''
        self.battery_size = battery_size

    def describe_battery_size(self):
        print(f'This car has a {self.battery_size}-kwh battery.')

    # def describe_battery(self):
    #     print(f'this car has a {self.battery}-kwh battery')

