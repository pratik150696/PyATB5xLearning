student_info = {"name": "Pratik",
                "age": 28,
                "address": "MA"
                }
print(student_info["name"])
print(student_info["age"])
print(student_info["address"])
student_info["age"] = "35"
print(student_info)

# Alternate way to create dictionary
student_info2 = dict(name="Pratik", age=28, address="MA")

# Dictionary within Dictionary
student_info = {"name": "Pratik",
                "age": 28,
                "address":
                    {"home_address":"VID",
                     "office_address": "MA"}
                }

print(student_info["address"])
print()