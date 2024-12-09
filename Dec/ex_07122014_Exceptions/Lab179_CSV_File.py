# CSV  ,comma separated File
import csv

with open("TestData.csv") as csvFile:
    reader = csv.reader(csvFile)
    for col in reader:
        print(col[0], col[1], sep=" | ")
