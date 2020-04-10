#importing the Car class from the car.py programme I wrote
from car import Car


my_new_car = Car('audi', 'a4', 2019, 23)
print(my_new_car.get_descriptive_name())
my_new_car.odometer.odometer_reading = 23
my_new_car.odometer.read_odometer()
my_new_car.drive(50)
my_new_car.odometer.read_odometer()