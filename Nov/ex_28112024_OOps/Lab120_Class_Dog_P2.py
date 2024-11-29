class Dog:
    # Attribute
    name = None
    breed = None
    height = None

    # Behaviour

    def __init__(self):    # Constructor  (Default)
        print("I Will be Called")

    def bark(self):
        print("Barking")

    def sleep(self):
        print("Sleeping")

    def talk(self):
        pass


# Object Ref
chow_ref = Dog()  # chow -->Obj Ref    Dog() ---> Obj
mow_ref = Dog()
bow_ref = Dog()
rancho_ref = Dog()

print(chow_ref.name)
print(mow_ref.name)
