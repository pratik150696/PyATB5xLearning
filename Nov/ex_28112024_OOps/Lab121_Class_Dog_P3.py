class Dog:
    # Attribute
    name = None
    breed = None
    height = None

    # Behaviour

    def __init__(self, name, breed):  # Constructor  (Parameterised)
        print("PC")
        self.name = name
        self.breed = breed

    def bark(self):
        print("Barking")

    def sleep(self):
        print("Who is Sleeping---> "+ self.name)

    def talk(self):
        pass


# Object Ref
chow_ref = Dog("chow","mustiff")  # chow -->Obj Ref    Dog() ---> Obj
print(chow_ref.name)
chow_ref.sleep()
print(id(chow_ref))


mow_ref = Dog("mow","husky")
print(mow_ref.name)
mow_ref.sleep()
print(id(mow_ref))
