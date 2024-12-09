print("----- Start of a Program")

try:
    a = int(input("Enter Num1: "))   # ValueError: invalid literal for int() with base 10: 'p'
    b = int(input("Enter Num2: "))
    c = a/b   # ZeroDivisionError: division by zero
    print("Result is: ", c)
except Exception as e:
    print(e)
print("----- End of a Program")

# try and Except