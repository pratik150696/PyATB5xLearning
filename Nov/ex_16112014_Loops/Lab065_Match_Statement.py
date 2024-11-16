# Match Statement --> similar like switch in JAVA


#  Write a program to ask the user which browser he want to use to run automation ?

browser_name = input("Enter the Browser Name: ")
match browser_name:
    case "firefox":
        print("Starting Firefox !!!")
    case "chrome":
        print("Starting Chrome !!!")
    case "edge":
        print("Starting Edge !!!")
    case "safari":
        print("Staring Safari !!!")
    case _:
        print("Browser Not Found !!!")
