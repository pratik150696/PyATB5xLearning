class Parent:

    def home(self):
        print("1 BHK")

class Son(Parent):

    def home(self):
        print("3 BHK")

f = Parent()
f.home()

p = Son()
p.home()