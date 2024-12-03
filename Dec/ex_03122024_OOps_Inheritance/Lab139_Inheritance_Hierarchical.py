class Father:

    def BHK1(self):
        print("1 BHK")


class Pratik(Father):

    def BHK2(self):
        print("2 BHK")


class Yash(Father):

    def BHK3(self):
        print("3 BHK")


class Archana(Father):

    def BHK4(self):
        print("4 BHK")


p = Pratik()
p.BHK1()
p.BHK2()

y = Yash()
y.BHK1()
y.BHK3()

a = Archana()
a.BHK1()
a.BHK4()
