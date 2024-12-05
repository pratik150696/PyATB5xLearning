class Calc:

    def sum(self, a, b):
        return a + b

    def sum(self, a, b, c=1):
        return a + b + c


calc_ref = Calc()
calc_ref.sum(3, 4)
