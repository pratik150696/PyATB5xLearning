def add_before_ui_after_ui(func):
    def wrapper():
        print("Before running the UI TC")
        print("Start Browser!!!")
        func()
        print("Ending the running UI TC")
        print("Quit Browser!!!")

    return wrapper()


@add_before_ui_after_ui
def test_ui():
        print(">>>>>I will test the UI")
