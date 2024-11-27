student_info1 = {"name": "Pratik",
                "age": 28,
                "address":
                    {"home_address":"VID",
                     "office_address": "MA"}
                }

student_info2 = {"name": "Amit",
                "age": 31,
                "address":
                    {"home_address":"MUM",
                     "office_address": "TN"}
                }


student_info3 = {"name": "Virat",
                "age": 37,
                "address":
                    {"home_address":"Delhi",
                     "office_address": "BENGALURU"}
                }

student_list = [student_info1,student_info2, student_info3]
# Print office address of Virat
print(student_list[2])
print(student_list[2]["address"])
print(student_list[2]["address"]["office_address"])

# Alternate Way
print(student_info3)
print(student_info3["address"])
print(student_info3["address"]["office_address"])