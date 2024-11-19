# Create a program to sum of three numbers from the user input.
# If user does not enter any number use default 100,200,300 ?

# Step 1: Logic building Formula --> I/P & O/P

num1 = int(input("Enter First Number:\n "))
num2 = int(input("Enter Second Number:\n "))
num3 = int(input("Enter Third Number:\n "))

def sum_of_three_numbers(n1 =100, n2 = 200 , n3 =300):
    return n1 + n2 + n3


result = sum_of_three_numbers(num1,num2,num3)
print(result)

result2 =sum_of_three_numbers()
print(result2)