# Tuple     ---> Collection of Item -->  ()    ---> Immutable(Can not change)

my_tuple = (1,2,4,9,16)
# my_tuple[2] = 25             # Tuple does not support item change
print(my_tuple)


# Real Example of List
shopping_list= ["Bread", "Butter" ,"Paneer"]
shopping_list[1] = "Miik"
print(shopping_list)

# Real Example of Tuple        ---> Tuple is used when we dont need to change
my_tuple = ("xyz.com", "sdet.live")
print(my_tuple)
my_api_list = list(my_tuple)
print(my_api_list)

# my_tuple[0] = "abc.com"           #TypeError: 'tuple' object does not support item assignment