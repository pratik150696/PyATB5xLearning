# Write a program to take user age and let him know
# that he can go to club     // 21

# Step1: Logic Building formula
#      I/P --> datatype --> int
#      O/P --> datatype --> string  --> you can go or not

age = int(input("Enter your Age: "))

# Step2:  >21 --> you can go,   <21 --> yon can not go

# Step3: Write the logic
if age >= 21:
    print("Yes you can go to Club")
else:
    print("You can not go to Club")

# Step4:  Check for the Edge Cases

# We should consider edge cases such as:
# 1) Negative ages or extremely high value  (-15 , 3566282713423488)
# 2) Non-Numeric Input --> ABC
# 3) Age which is valid > 130


# Step5: Optimize the Code
# Handle all the edges
