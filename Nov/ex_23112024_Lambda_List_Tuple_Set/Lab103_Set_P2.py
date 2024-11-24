# Union
set1 = {1, 2, 3}
set2 = {4, 5, 6}

my_set = set1.union(set2)
print(my_set)

# Intersection
set3 = {1, 2, 3, 4, 5}
set4 = {4, 5, 6, 7, 8, }

my_set2 = set3.intersection(set4)
print(my_set2)

# Difference
set5 = {1, 2, 3, 4, 5}
set6 = {4, 5, 6, 7, 8}

my_set3 = set5.difference(set6)
print(my_set3)
my_set3 = set6.difference(set5)
print(my_set3)
