# Write a program to calculate even and odd

# def find_even_odd(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
#
#
# find_even_odd(5)

num = int(input("Enter a Number: "))
check_even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"
# print(check_even_odd(6))
print(check_even_odd(num))
