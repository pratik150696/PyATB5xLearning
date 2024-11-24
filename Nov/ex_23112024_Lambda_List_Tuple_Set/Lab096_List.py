my_list = [1,2,3]

# Indexing
print("Element at the Index 0 -->", my_list[0])
print("Element at the Index 1 -->", my_list[1])
print("Element at the Index 2 -->", my_list[2])

# Append()   ---> Add object at the end
my_list.append(4)
my_list.append(5)
print(my_list)

# Extend()   ---> Add a New List
my_list.extend([7,10,9,12,8,6])
print(my_list)

# Insert()  ---> Insert value of index
my_list.insert(1, "Pratik")
print(my_list)
print(len(my_list))

my_list.insert(0,0)
print(my_list)

my_list[1] = "Amit"
print(my_list)

# Remove()
my_list.remove("Amit")
print(my_list)


print("-------------------------------------------\n""-------------------------------------------")

my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list)

my_list.remove("Pratik")
my_copy_list.remove("Pratik")
print(my_list)
print(my_copy_list)

my_list.sort()
my_copy_list.sort()
print(my_list)
print(my_copy_list)
