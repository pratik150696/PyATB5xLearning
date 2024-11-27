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

student_list = [student_info1,student_info2]
print(student_list)
print(student_list[0])
print(student_list[0]["name"])
print(student_list[0]["age"])
print(student_list[0]["address"])
print(student_list[0]["address"]["office_address"])
print(student_list[1])
