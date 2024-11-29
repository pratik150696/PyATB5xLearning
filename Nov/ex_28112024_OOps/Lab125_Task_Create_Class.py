# Task 1 - Create a Class PyATB , 5 Attributes, 3 Functions/Methods
#
# Use PC - to set the value of the attributes
#
# create a Print student information method/function


class PyATB:


    def __init__(self,name,age,gender,role,experience):
        self.name = name
        self.age = age
        self.gender = gender
        self.role = role
        self.experience = experience

    def student_info(self):
        print( f"Name is {self.name}" ,f"Age is {self.age}",f"Gender is {self.gender}", f"Role is {self.role}"
               ,f"Experience is {self.experience}")

object1 = PyATB("Pratik",28,"Male", "Automation Tester", 3)
object2 = PyATB("Alia",31,"Female", "Manual Tester", 5)
object3 = PyATB("Rahul",26,"Male", "Automation Tester", 2)

object1.student_info()
object2.student_info()
object3.student_info()