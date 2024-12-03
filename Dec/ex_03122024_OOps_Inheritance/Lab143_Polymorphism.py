# Method Overloading

class MathUtils:
    # Direct Method Overloading Not Supported, Need to use Default Parameters i.e add(a=0, b=0)
    def add(self, a=0, b=0):
        return a + b

    def add(self, a=0, b=0, c=0):
        return a + b + c

    def add(self, a=0, b=0, c=0, d=0):
        return a + b + c + d


math = MathUtils()
op1 = math.add(5, 5)
op2 = math.add(10, 10, 10)
op3 = math.add(10, 20, 10, 20)

print(op1)
print(op2)
print(op3)
