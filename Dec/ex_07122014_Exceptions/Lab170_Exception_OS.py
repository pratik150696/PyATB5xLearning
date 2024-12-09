import os

print(os.getcwd())  # Return the current working directory

# List Files in the current directory
files = os.listdir('/Users/ASUS/PycharmProjects/PyATB5xLearning')
print(f"Files in Current Directory: {files}")

# Create new directory
# os.mkdir("Test2")

# Check if File Exists

file_exists = os.path.exists("TestData.txt")
print(file_exists)
