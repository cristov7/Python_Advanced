# # In "words.txt" file:
# quick is fault

# # In "text.txt" file:
# -I was quick to judge him, but it wasn't his fault.
# -Is this some kind of joke?! Is it?
# -Quick, hide here…It is safer.

words_file = open("words.txt", "r")
words_file_list = words_file.readlines()
words_file.close()
words_dict = {}
for line in words_file_list:
    line_list = line.split()
    for word in line_list:
        word.lower()
        if word not in words_dict:
            words_dict[word] = 0
        else:
            continue
text_file = open("text.txt", "r")
text_file_list = text_file.readlines()
text_file.close()
for word in words_dict.keys():
    for line in text_file_list:
        current_line = ""
        for char in line:
            if char.isalpha():
                char = char.lower()
                current_line += char
            elif char == "'":
                current_line += char
            else:
                current_line += " "
        current_line_list = current_line.split()
        if word in current_line_list:
            count = current_line_list.count(word)
            words_dict[word] += count
        else:
            continue
sorted_dict = dict(sorted(words_dict.items(), key=lambda x: -x[1]))
for word, count in sorted_dict.items():
    print(f"{word} - {count}")
