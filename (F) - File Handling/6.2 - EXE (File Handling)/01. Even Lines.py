# # In "text.txt" file:
# -I was quick to judge him, but it wasn't his fault.
# -Is this some kind of joke?! Is it?
# -Quick, hide here. It is safer.


file = open("text.txt", "r")
lines_list = file.readlines()
file.close()
even_list = []
for index, line in enumerate(lines_list):
    if index % 2 == 0:
        even_list.append(line)
    else:
        continue
replace_chars_list = ["-", ",", ".", "!", "?"]
for char in replace_chars_list:
    for index, line in enumerate(even_list):
        if char in line:
            replace_line = line.replace(char, "@")
            even_list[index] = replace_line
        else:
            continue
split_list = []
for line in even_list:
    line_list = line.split()
    split_list.append(line_list)
for line_list in split_list:
    line_list.reverse()
    print(" ".join(line_list))


# with open("text.txt", "r") as file:
#     lines_list = file.readlines()
# even_list = [line for index, line in enumerate(lines_list) if index % 2 == 0]
# replace_chars_list = ["-", ",", ".", "!", "?"]
# for char in replace_chars_list:
#     for index, line in enumerate(even_list):
#         if char in line:
#             replace_line = line.replace(char, "@")
#             even_list[index] = replace_line
#         else:
#             continue
# split_list = [line.split() for line in even_list]
# [print(" ".join(line_list[::-1])) for line_list in split_list]


# replace_chars_list = ["-", ",", ".", "!", "?"]
# with open("text.txt", "r") as file:
#     lines_list = file.readlines()
# for index_line in range(0, len(lines_list), 2):
#     for char in replace_chars_list:
#         lines_list[index_line] = lines_list[index_line].replace(char, "@")
#     print(*lines_list[index_line].split()[::-1])
