import os
file_name = "text.txt"
if os.path.exists(file_name):
    print("File found")
else:
    print("File not found")


# file_name = "text.txt"
# try:
#     file = open(file_name)   # open(file_name, "r")
#     print("File found")
# except FileNotFoundError:
#     print("File not found")


# try:
#     open("text.txt", "r")   # open(file_name, "r")
# except FileNotFoundError:
#     print("File not found")
# else:
#     print("File found")
