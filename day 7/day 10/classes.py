# OOP
#Defining a clasa and its attributes.
#Creating instances(onjects) of a class
# Class methods(functions belonging to a class)
#Inheritance & Polymorphism
#Method overriding



class Dog:
    def __init__(self, no_of_eyes, color):
        self.no_of_eyes =no_of_eyes
        self.color = color
    def bark(self):
        print("woof woof")
    def move(self):
        print("limp")
german_shepherd = Dog(no_of_eyes=2, color='Grey')
dodgder =Dog(no_of_eyes=1, color='white')
Japanese_spitz=Dog(2, 'brown')

print(german_shepherd.color)
print(Japanese_spitz.no_of_eyes)

Japanese_spitz.color = 'white'
print(Japanese_spitz.color)
dodgder.bark()

german_shepherd.move()