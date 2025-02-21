# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal),
# or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

# Step1: Logic Building Formula
#   I/P --> data type  --> float
#   O/P --> data type --> String

A = float(input("Enter length of side A: "))
B = float(input("Enter length of side B: "))
C = float(input("Enter length of side C: "))


# Step2: Rough Logic   -->
#  A = B = C --> Equilateral
#  A = B = != C --> Isosceles
#  A != B != C --> Scalene


# Step3:  Write Logic
def classify_triangle():
    if A > 0 and B > 0 and C > 0:
        if A + B > C and B + C > A and A + C > B:

            if A == B == C:
                print("Triangle is Equilateral")
            elif A == B or A == C or B == C:
                print("Triangle is Isosceles")
            else:
                print("Triangle is Scalene")
        else:
            print("Not a Valid Triangle")
    else:
        print("Not a Valid Length")


classify_triangle()
