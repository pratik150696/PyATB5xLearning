# Program to find Maximum number between three value

value1 = float(input("Enter value one: "))
value2 = float(input("Enter value two: "))
value3 = float(input("Enter value three: "))

if value1 > value2 and value1 > value3:
    print("Max value is ", value1)
elif value2 > value3 and value2 > value1:
    print("Max value is ", value2)
else:
    print("Max value is ", value3)
