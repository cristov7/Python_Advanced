with open("my_first_file.txt", "x") as file:          # create a file
    file.write("I just created my first file!")       # add element to the file
#
# In "my_first_file.txt" file:
# I just created my first file!


# file_path = "my_first_file.txt"
# content = "I just created my first file!"
# file = open(file_path, "w")                         # create or overwritten a file
# file.write(content)                                 # add element to the file
# file.close()                                        # close the file
#
# # In "my_first_file.txt" file:
# # I just created my first file!


# file_path = "my_first_file.txt"
# file = open(file_path, "a")                         # add or create and add
# file.write("I just created my first file!")         # add element to the file
# file.close()                                        # close the file
