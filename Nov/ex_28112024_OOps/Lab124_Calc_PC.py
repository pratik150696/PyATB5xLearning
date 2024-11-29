class Calc:

    # a = None
    # b =None

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


object_ref1 = Calc(3, 4)
object_ref2 = Calc(3, 4)
object_ref3 = Calc(3, 4)
object_ref4 = Calc(3, 4)

output1 = object_ref1.sum()
output2 = object_ref1.sub()
output3 = object_ref1.mul()
output4 = object_ref1.div()

print(output1)
print(output2)
print(output3)
print(output4)
