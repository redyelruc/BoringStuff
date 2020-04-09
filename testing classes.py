class Dog:
    '''a simple attempt to model a dog'''

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def __str__(self):
        '''Default string if the object is printed'''
        return(f'My name is {self.name} and I am {self.age} old.')

    def sit(self):
        '''A method that gets the dog to sit on command'''
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        '''A method the gets the dog to roll over on command'''
        print(f'{self.name} has just rolled over')

my_pet = Dog('Cuisle', '11 weeks')
petes_pet = Dog('Marler', '6 months')
my_pet.sit()
my_pet.roll_over()
print(my_pet.__dict__)
print(my_pet)
print(my_pet is petes_pet)