chars_dict = {}
text = input()
chars_list = list(text)
for current_char in chars_list:
    if current_char not in chars_dict.keys():
        count_char = chars_list.count(current_char)
        chars_dict[current_char] = count_char
    else:
        continue
sorted_tuples_list = sorted(chars_dict.items())
for sorted_tuple in sorted_tuples_list:
    char = sorted_tuple[0]
    count = sorted_tuple[1]
    print(f"{char}: {count} time/s")


# chars_dict = {}
# chars_list = list(input())
# for current_char in chars_list:
#     if current_char not in chars_dict.keys():
#         chars_dict[current_char] = 1
#     else:
#         chars_dict[current_char] += 1
# sorted_tuples_list = sorted(chars_dict.items(), key=lambda keys: keys[0])
# for sorted_tuple in sorted_tuples_list:
#     char = sorted_tuple[0]
#     count = sorted_tuple[1]
#     print(f"{char}: {count} time/s")
