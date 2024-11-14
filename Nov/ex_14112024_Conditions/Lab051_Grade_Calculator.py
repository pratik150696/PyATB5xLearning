# Write a program that calculates and displays the letter grade for a given numerical score
# (e.g A,B,C,D or E) based on the following grading scale ?
"""
A: 90 -100
B: 80-89
C: 70-79
D: 60-69
E: 50-59
"""
from turtledemo.sorting_animate import Block

# Step1: Building a logic
#      I/P --> datatype  --> int
#      O/P --> datatype --> string

Score = int(input("Enter your score: "))

# Step2: Rough Logic   >=90 & <=100  --> A , ......
if Score >= 90 and Score <= 100:
    print("Your Grade is: ", "A")
elif Score >= 80 and Score <= 89:
    print("Your Grade is: ", "B")
elif Score >= 70 and Score <= 79:
    print("Your Grade is: ", "C")
elif Score >= 60 and Score <= 69:
    print("Your Grade is: ", "D")
else:
    print("Your Grade is: ", "F")
