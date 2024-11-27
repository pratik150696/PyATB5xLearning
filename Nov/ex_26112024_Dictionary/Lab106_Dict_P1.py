# Dict  ---> Key and Value Pairs ---> {}

my_dict = {"name" : "Pratik" ,
           "age": 28,
           "role": "SSE",
           "experience": 3
           }
print(my_dict)
print(my_dict["age"])


# Change Value
my_dict["role"] = "Automation Tester"
print(my_dict)

# Delete Key & Value
del my_dict["age"]
print(my_dict)

# Iteration
for key, value in my_dict.items():
    print(key, "----->", value)

# Checking Existence
print("age" in  my_dict)
print("role" in my_dict)
