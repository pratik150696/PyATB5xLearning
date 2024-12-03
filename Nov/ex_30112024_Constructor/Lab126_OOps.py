a = 10      # Global Variable

class Person:
    b = 11     # Instance Variable

    def print_info(self):
        c = 20     # Local Variable
        print(c)
        print(self.b)
        global a
        print(a)
        a = "Hello"
        print(a)

object_ref = Person()
object_ref.print_info()
