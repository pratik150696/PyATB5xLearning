class Person:

# Attributes  ----> What you have ?
    id = None
    name = None
    age = None
    email = None
    gender = None
    height = None
    phone_no = None
    address = None

# Behaviour ----> What you can do ?

    def talk(self):    # NRNA
        print("I can Talk")

    def walk(self):
        print("I can Walk")

    def sleep(self, name):   # Arg with No Return
        print("I am a Method!!!")
        print("Sleep", name)

    def sleep2(self, name):
        print("I am a Method!!!")
        return None


# Create an Object of a Class

pratik = Person()
pratik.name = "Pratik Alaspure"
pratik.gender = "Male"