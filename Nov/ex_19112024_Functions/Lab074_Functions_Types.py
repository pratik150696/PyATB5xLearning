# 1. They can't return -> non return`
# 2. They can return something
# 3. They have parameters
# 4.`They don't parameters / arguments`


# 1. They can't return -> non return` ---> No Parameter
def greet():
    print("Hello")


greet()


# 2. No return type with Parameter
def greet_with_name(name):
    print("Hello,", name)


greet_with_name("Pratik")


# 3. No return type with Default Parameter ( # Positional Argument )
def say_hello_default_arg(name="Pratik"):
    print("Hello,", name.upper())


say_hello_default_arg("Alaspure")
say_hello_default_arg()


#  Multiple Parameter / Arguments
def multiple_arg(name1="A", name2="B"):
    print("Multiple-->", name1.upper(), name2.upper()   )


multiple_arg()
multiple_arg("Pratik")
multiple_arg(name1 ="Pratik")
multiple_arg("Pratik", "Alaspure")
multiple_arg(name2="Alaspure")


# 4. Argument + Return Type

def sum_of_two_number(a,b):
    return a + b

result = sum_of_two_number(4,56)
print(result)

def sum_of_two_numbers_with_default(num1 = 100 , num2 = 200):
    return num1 + num2

result = sum_of_two_numbers_with_default(num1=34, num2=34)
print(result)

result= sum_of_two_numbers_with_default()
print(result)
