# Single Inheritance   ----> 85% of time you will use SI in API , Web Automation

class Father:
    key = "2BHK"

    def car(self):
        print("Father has a car --> Alto ")
        print(self.key)

class Son(Father):                 # Single Inheritance
    key2 = "3BHK"

    def suv(self):
            print("MG Hector, Black")
            print(self.key2)

father_obj = Father()
father_obj.car()

son_obj = Son()
son_obj.suv()

son_obj.car()      # Able to access Father Class