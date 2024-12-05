# Method overloading is not supported in Python

class Calc:

    def sum(self, a, b):
        return a + b

    def sum(self, a, b, c):
        return a + b + c


calc_ref = Calc()
calc_ref.sum(3, 4)
