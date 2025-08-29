# Step 1: Read/Write Text Files
# Writing to a file
with open("example.txt", "w") as fileAccess:
    fileAccess.write("Hello, this is a test file.\nThis is line 2.")

# Reading from a file
with open("example.txt", "r") as f:
    content = f.read()
    print("File Content:\n", content)
