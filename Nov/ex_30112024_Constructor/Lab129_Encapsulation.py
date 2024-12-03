class Car:

    def __init__(self,o_name, o_make,o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model


    def start_engine(self):
        print("Starting the car with the name ",self.name)
        print("Starting the car with the make ",self.make)
        print("Starting the car with the model ",self.model)

lambo = Car("Lambo", "V6","2024")
lambo.start_engine()


print("------------------------------------------")


mg_hector = Car("Hector", "1.5 Turbo", 2023)
mg_hector.start_engine()