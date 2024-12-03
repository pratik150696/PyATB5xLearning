# Method Overriding

class Father:

    def home(self):
        print("1 BHK")

class Pratik(Father):

    def home(self):
        print("3 BHK")

f = Father()
f.home()

p = Pratik()
p.home()