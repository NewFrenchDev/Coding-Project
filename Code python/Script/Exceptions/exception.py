import os

#Ask to the user to enter a path to open a file
file_to_open = input("Enter the path to the file to open: ")

#Open the file and treat exceptions
try:
    with open(file_to_open, 'r', encoding='utf-8') as f:
        content = f.read()
except UnicodeDecodeError:
    print("Impossible to open the file!")
except FileNotFoundError as not_found:
    print(not_found)
else:
    print(content)
finally:
    print("Done!")