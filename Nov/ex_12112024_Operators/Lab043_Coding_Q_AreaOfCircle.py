# Write a Python program to calculate the area of circle using the formula area =   pi r square (pi = 3.14)

# Step 1: I/P  --> r = radius = datatype(float), pi = 3.14
# & O/P --> float

# Step 2:
#   area = pi*(r**2)

# Step 3:

radius = float(input("Enter the Radius of a circle: "))
pi = 3.14
area = pi * (radius ** 2)

print("Area of a Circle is: ", area)

# print(f"Area of a Circle is:  {area:.2f}" )    --> .2f means upto 2 decimal point

print("---------------------------------")

import math

print(math.pi)
print(math.pow(radius, 2))
area = math.pi * math.pow(radius, 2)
print("Area of a Circle is: ", area)


print("-------------------------------")

import math
print(math.pi)
print(math.sin(90))
print(math.tan(90))
print(math.cos( 90))
print(math.pow(2,3))
