'''This module is a class that can be used to represent a car'''
import pyinputplus as pyip

class Odometer:
    ''' a simple attempt to model an odometer'''
    def __init__(self):
        self.odometer_reading = 0

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year, fuel_econ):
        self.make = make
        self.model = model
        self.year = year
        self.gas_tank = 10
        self.fuel_economy = fuel_econ
        self.odometer = Odometer()

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def fill_gas_tank(self,gas):
        self.gas_tank += gas
        print(f'You now have {self.gas_tank} litres of gas in the tank.')

    def use_gas(self,mileage):
        self.gas_tank -= (mileage/int(self.fuel_economy))
        print(f'You have just driven {mileage} miles.')
        print(f'You now have {self.gas_tank} litres of gas in the tank.')

    def drive(self,mileage):
        self.odometer.update_odometer(mileage + self.odometer.odometer_reading)
        self.use_gas(mileage)

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def get_range(self):
        """Print a statement about the range this battery provides."""
        range = self.battery_size * 4
        print(f"This car can go about {range} miles on a full charge.")

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def upgrade_battery(self):
        # Check what size the battery currently is.
        if self.battery_size < 150:
            self.battery_size = 150
            print('Battery upgraded.')
            self.describe_battery()
        else:
            print(f'You currently have a {self.battery_size} kWh battery.'
                  f'That\'s the maximum size available.')
            
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year, fuel_economy):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year, fuel_economy)
        # a new attribute that is particular to electric cars, not all cars
        self.battery = Battery(pyip.inputInt('Please enter the battery size of your car?: '))

'''
my_tesla = ElectricCar('tesla', 'model s', 2019, 23)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
if pyip.inputYesNo('Do you want to upgrade your battery?') == 'Yes':
    my_tesla.battery.upgrade_battery()
    my_tesla.battery.get_range()

my_merc = Car('mercedes', 'c_class', '2019', '7')
print(my_merc.get_descriptive_name())
my_merc.fill_gas_tank(50)
my_merc.drive(25)

'''
