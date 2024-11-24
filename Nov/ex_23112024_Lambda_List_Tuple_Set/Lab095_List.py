# List ---> Collection of Item  -> [ Duplicates are allowed ]----> Mutable(Can be change)
# Grocery List  --> Butter, Bread, Banana, Paneer.
# Marks --> 37,56,55,78,96


my_list = [1,2,3]     # Same Data Type
my_list2 = [ 1, True , "Pratik" , 19.9]      # Different Data Type


print(my_list)
print(len(my_list2))
print(my_list[0])
print(my_list[1])
print(my_list[2])
# print(my_list[5])    ---> Index Out Of Range

my_list[0] = "Pratik"
my_list[1] = "Janardan"
my_list[2] = "Alaspure"

print(my_list)

print("---------------------------------")

for item in my_list2:
    print(item, end=" ")