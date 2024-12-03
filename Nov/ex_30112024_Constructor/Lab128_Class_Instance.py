class Person:

    def __init__(self, name):
        self.name =  name


    def walk(self):
        return self.name

amit = Person("Amit")
pratik = Person("Pratik")

print(amit.name)
print(pratik.name)

print("Who is Walking", amit.walk())
print("Who is Walking", pratik.walk())