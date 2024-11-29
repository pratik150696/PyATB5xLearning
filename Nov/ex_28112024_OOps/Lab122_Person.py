# Take input and create class in Python

class Person:

    def __init__(self):
        print("I will be Called")
        self.name = input("Enter the Name: \n ")
        self.age = input("Enter your Age: \n ")
        self.phone = input("Enter your Phone Number: \n ")
        self.address = input("Enter your Address: \n ")

    def name_of_the_function_t_display(self):
        print(f"Name is {self.name}" ,f"Age is {self.age}",f"Phone is {self.phone}", f"Address is {self.address}")

person1 = Person()
person1.name_of_the_function_t_display()