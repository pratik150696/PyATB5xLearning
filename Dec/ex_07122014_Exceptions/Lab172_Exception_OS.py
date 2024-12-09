import os

try:
    full_path = os.getcwd()
    print(full_path)

    full_path_file = full_path + "/example.txt"
    print(full_path_file)

    # Name of OS

    print(os.name)  # nt --> Windows, posix --> Mac, Linux

    # Read the File
    file = open(full_path_file)
except Exception as e:
    print(e)

finally:
    print("This code will Execute Anyhow")

