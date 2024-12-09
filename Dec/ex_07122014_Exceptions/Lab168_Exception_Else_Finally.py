try:
    num1 = int(input("Enter Num1: "))  # ValueError: invalid literal for int() with base 10: 'p'
    num2 = int(input("Enter Num2: "))
    result = num1 / num2  # ZeroDivisionError: division by zero

except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print("Result is: ", result)
