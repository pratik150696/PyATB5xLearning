# Multiple Inheritance ----> Not Supported in Java

class Father:

    def home(self):
        print("This is Father's Home")

    def father_money(self):
        return 5


class Mother:

    def home(self):
        print("This is Mother's Home")

    def mother_money(self):
        return 2

class Son(Father, Mother):

    def son_money(self):
        print("Son")

s = Son()
print(s.mother_money())
print(s.father_money())
print(s.home())             # First will Print written in Line 20