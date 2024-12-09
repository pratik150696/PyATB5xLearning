class XYZ:

    def f1(self):
        try:
            a = int(input("Enter the Number: "))
        except Exception as e:
            print("Enter the value of a as int only")
        else:
            print(a)
        finally:
            print("FINALLY: Anyhow I will be Printed")
obj_ref = XYZ()
obj_ref.f1()