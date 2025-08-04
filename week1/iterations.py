# for loop
for value in range(1, 6):
    print("Number:")
    print(value)

# while loop
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue  # skip 3
    print("While loop:", i)
    i += 1
