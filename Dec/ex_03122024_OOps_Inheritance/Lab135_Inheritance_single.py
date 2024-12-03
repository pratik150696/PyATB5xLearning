class Parent:
    gold = "2Kg"

    def BHK2(self):
        print("2 BHK")

class child(Parent):
    diamond  = "Diamond"

    def BHK3(self):
        print("3 BHK")

child_obj = child()
print(child_obj.gold)
child_obj.BHK2()
