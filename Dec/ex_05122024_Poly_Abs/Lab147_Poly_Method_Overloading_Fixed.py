class Calc:

    def sum(self, *args):
        for a in args:
            print(a)


calc_ref = Calc()
calc_ref.sum(5)
calc_ref.sum(3, 4)
calc_ref.sum(4,4,5)