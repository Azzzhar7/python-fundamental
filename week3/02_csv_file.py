# Step 2: Working with CSV Files
import csv

# Writing CSV
headers = ["Name", "Age"];
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerow(["Alice", 25])
    writer.writerow(["Bob", 30])

# Reading CSV
count = 0
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        count = count+1
        if count >= 100:
            break
        print(row)
