pb_global_b = 12               # Global Variable


def my_function():
    pb_a = 10                  # Local Variable
    print(pb_global_b)
    print(pb_a)

# print(pb_a)  ----> Local variable cannot use outside
pb_global_b   #-----> Global can use anywhere
my_function()
