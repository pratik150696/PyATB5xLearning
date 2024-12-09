import os

file_name = "Pratik.txt"
content = "This is a Pratik's File XYZ"

# Create File and Write
# with open(file_name, "w") as file:
#     file.write(content)

# Read File
with open(file_name, "r") as file:
    content2 = file.read()
    print(content2)

# Move the File
# os.chdir("Desktop")

