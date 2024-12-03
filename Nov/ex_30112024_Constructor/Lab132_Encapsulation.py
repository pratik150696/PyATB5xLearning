class Car:

    def __init__(self):
        self.password = "Pratik"    # public instance variable
        self.__password_secure = "pass123"     # private instance variable

    def change_password(self):
        print(self.password)

object_ref = Car()
print(object_ref.password)
object_ref.password = "Alaspure"
object_ref.change_password()

# print(object_ref.__password_secure)   ------> Will not show password
