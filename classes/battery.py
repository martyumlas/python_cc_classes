class Battery:

    def __init__(self, battery_size=40):
        '''initialize battery'''
        self.battery_size = battery_size

    def describe_battery_size(self):
        print(f'This car has a {self.battery_size}-kwh battery.')

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")
        
    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65
        else:
            print('Already updgraded')

    # def describe_battery(self):
    #     print(f'this car has a {self.battery}-kwh battery')

