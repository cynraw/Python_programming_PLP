try:
    with open('non-existantfile.txt', 'r') as file:
        data = file.read()
except FileNotFoundError:
    print('File not found please check file name')


# The finnaly block will always run regardless of whether an exception is raised or not.
# This is useful for cleaning up resources such as closing a file or a database connection.
try:
    file = open("sample.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()