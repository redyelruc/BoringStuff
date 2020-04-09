'''Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating
that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.'''

class Restaurant:
    # a simple nodel of a restaurant
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print (f'The restaurant {self.name} serves {self.cuisine} food.')
        print (f'They\'ve served {self.number_served} customers to date.')

    def open_restaurant(self):
        print(f'{self.name} is now open for business.')

    def serve_people(self, num_customers):
        self.number_served +=num_customers

restaurant = Restaurant('Bella Chao', 'Italian')
new_restaurant = Restaurant('Rampage\'s', 'Vegetarian' )

new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()
new_restaurant.serve_people(3)
restaurant.describe_restaurant()
restaurant.serve_people(12)
restaurant.describe_restaurant()

