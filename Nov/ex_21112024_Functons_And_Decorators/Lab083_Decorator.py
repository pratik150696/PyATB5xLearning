def add_extra_safety(func):

    def wrapper():
        print("1. Before the function is called.")
        print("2. Add Helmet, Dashcam, Gloves, Knee Guard, Licence.")
        func()  #driving_scooty  & drive_ola_scooter
        print("3. After the function is called.")
        print("4. Secure driving, Leave all the items ")
    return wrapper()

@add_extra_safety
def drive_ola_scooter():
    print("Ola")


@add_extra_safety
def driving_scooty():
    print("Normal Function!!!")
    print("I am driving a Scooty")
