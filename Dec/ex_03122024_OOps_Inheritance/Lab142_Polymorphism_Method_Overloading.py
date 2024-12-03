# Method Overloading

class Dog:

    def bark(self):
        print("Dog is Barking")

    def bark(self, breed):
        print(f"Dog with a {breed} is Barking")

d = Dog()
d.bark("Chow")