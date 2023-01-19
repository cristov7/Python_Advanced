from collections import deque
substrings_deque = deque(input().split())
main_colors_tuple = ("red", "yellow", "blue")
secondary_colors_tuple = ("orange", "purple", "green")
find_colors_list = []
while True:
    if len(substrings_deque) > 1:
        first_substring = substrings_deque.popleft()
        last_substring = substrings_deque.pop()
        current_first_string = first_substring + last_substring
        current_second_string = last_substring + first_substring
        if current_first_string in main_colors_tuple or current_first_string in secondary_colors_tuple:
            find_colors_list.append(current_first_string)
        elif current_second_string in main_colors_tuple or current_second_string in secondary_colors_tuple:
            find_colors_list.append(current_second_string)
        else:
            middle_index = len(substrings_deque) // 2
            if len(first_substring) > 1 and len(last_substring) > 1:
                first_middle_substring = first_substring[:-1]
                second_middle_substring = last_substring[:-1]
                substrings_deque.insert(middle_index, first_middle_substring)
                substrings_deque.insert(middle_index + 1, second_middle_substring)
            else:
                if len(first_substring) == 1 and len(last_substring) == 1:
                    continue
                elif len(first_substring) == 1:
                    middle_substring = last_substring[:-1]
                    substrings_deque.insert(middle_index, middle_substring)
                else:   # elif len(last_substring) == 1:
                    middle_substring = first_substring[:-1]
                    substrings_deque.insert(middle_index, middle_substring)
    elif len(substrings_deque) == 1:
        current_string = substrings_deque.popleft()
        if current_string in main_colors_tuple or current_string in secondary_colors_tuple:
            find_colors_list.append(current_string)
            break
        else:
            if len(current_string) > 1:
                current_substring = current_string[:-1]
                substrings_deque.append(current_substring)
            else:
                break
    else:   # elif len(substrings_deque) == 0:
        break
paint_colors_list = []
for color in find_colors_list:
    if color in main_colors_tuple:
        paint_colors_list.append(color)
    else:   # elif color in secondary_colors_tuple:
        if color == "orange" and "red" in find_colors_list and "yellow" in find_colors_list:
            paint_colors_list.append(color)
        elif color == "purple" and "red" in find_colors_list and "blue" in find_colors_list:
            paint_colors_list.append(color)
        elif color == "green" and "yellow" in find_colors_list and "blue" in find_colors_list:
            paint_colors_list.append(color)
        else:
            continue
print(paint_colors_list)
