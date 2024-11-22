# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100
# unless it is also divisible by 400.
# Use an if-else statement to make this determination.


# Step1: Logic Building Formula
#   I/P --> data type  --> int
#   O/P --> data type --> String

year = int(input("Enter a Year: "))

# Step2: Rough Logic   --> %4 , %! 100, %400


# Step3:  Write Logic
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Year is a leap Year")
else:
    print("Year is not a leap year")
