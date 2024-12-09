a = int(input("Enter Num1: "))   # ValueError: invalid literal for int() with base 10: 'p'
b = int(input("Enter Num2: "))
c = a/b   # ZeroDivisionError: division by zero
print("Result is: ", c)