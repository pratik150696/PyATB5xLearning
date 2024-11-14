# Problem to find max number between two

# Step1: Logic building formula
#      I/P --> datatype  --> float
#      O/P --> datatype  --> float

# Step2: Rough Logic
# Step3: Write Logic

num1 = float(input("Enter Number One: "))
num2 = float(input("Enter Number Two: "))

if num1 > num2:
    print("Max is : ", num1)
else:
    print("Max is : ", num2)

# Step4: Edge Cases
# 1) If both of them are equal num1 == num2
# 2) String --> ABC , ten ,fifty
# 3) Negative Value --> -35 ,-50
