# # In "text.txt" file:
# -I was quick to judge him, but it wasn't his fault.
# -Is this some kind of joke?! Is it?
# -Quick, hide here. It is safer.


from string import punctuation
with open("text.txt", "r") as text_file:
    lines_list = text_file.readlines()
number_line = 0
output_list = []
for line in lines_list:
    number_line += 1
    count_letters = sum([1 for char in line if char.isalpha()])
    count_punctuation_marks = sum([1 for char in line if char in punctuation])
    output = f"Line {number_line}: {line[:-1]} ({count_letters})({count_punctuation_marks})\n"
    output_list.append(output)
output_file = open("output.txt", "w")
output_file.writelines(output_list)
output_file.close()


# # In "output.txt" file:
# Line 1: -I was quick to judge him, but it wasn't his fault. (37)(4)
# Line 2: -Is this some kind of joke?! Is it? (24)(4)
# Line 3: -Quick, hide here. It is safer. (22)(4)


# from string import punctuation
# with open("text.txt", "r") as text_file:
#     lines_list = text_file.readlines()
# output_file = open("output.txt", "w")
# for index in range(0, len(lines_list)):
#     line = lines_list[index]
#     count_letters = 0
#     count_punctuation_marks = 0
#     for char in line:
#         if char.isalpha():
#             count_letters += 1
#         elif char in punctuation:
#             count_punctuation_marks += 1
#         else:
#             continue
#     output_file.write(f"Line {index + 1}: {line[:-1]} ({count_letters})({count_punctuation_marks})\n")
# output_file.close()
