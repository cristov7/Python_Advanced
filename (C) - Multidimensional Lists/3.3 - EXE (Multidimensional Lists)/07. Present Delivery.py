count_presents = int(input())
size_of_the_neighborhood = int(input())
matrix_list = []
for nested_list_index in range(size_of_the_neighborhood):
    nested_list = input().split()
    matrix_list.append(nested_list)
santa_nested_list_index = None
santa_nested_element_index = None
count_all_nice_kids = 0
for nested_list_index in range(len(matrix_list)):
    for nested_element_index in range(len(matrix_list[nested_list_index])):
        nested_element = matrix_list[nested_list_index][nested_element_index]
        if nested_element == "S":
            santa_nested_list_index = nested_list_index
            santa_nested_element_index = nested_element_index
            matrix_list[santa_nested_list_index][santa_nested_element_index] = "-"
        elif nested_element == "V":
            count_all_nice_kids += 1
        else:
            continue
count_waiting_for_presents_nice_kids = count_all_nice_kids
COMMAND_UP = "up"
COMMAND_DOWN = "down"
COMMAND_LEFT = "left"
COMMAND_RIGHT = "right"
COMMAND_END = "Christmas morning"
while True:
    command = input()
    if command == "":
        break
    elif command == COMMAND_END:
        break
    elif command == COMMAND_UP:
        if santa_nested_list_index - 1 >= 0:
            santa_nested_list_index -= 1
            nested_element = matrix_list[santa_nested_list_index][santa_nested_element_index]
            if nested_element == "V":
                count_presents -= 1
                count_waiting_for_presents_nice_kids -= 1
                matrix_list[santa_nested_list_index][santa_nested_element_index] = "-"
                if count_presents > 0:
                    continue
                else:
                    break
            elif nested_element == "X":
                matrix_list[santa_nested_list_index][santa_nested_element_index] = "-"
            elif nested_element == "C":
                if santa_nested_list_index - 1 >= 0:
                    up_nested_element = matrix_list[santa_nested_list_index - 1][santa_nested_element_index]
                    if up_nested_element == "V":
                        count_presents -= 1
                        count_waiting_for_presents_nice_kids -= 1
                        matrix_list[santa_nested_list_index - 1][santa_nested_element_index] = "-"
                    if up_nested_element == "X":
                        count_presents -= 1
                        matrix_list[santa_nested_list_index - 1][santa_nested_element_index] = "-"
                if santa_nested_list_index + 1 < len(matrix_list):
                    down_nested_element = matrix_list[santa_nested_list_index + 1][santa_nested_element_index]
                    if down_nested_element == "V":
                        count_presents -= 1
                        count_waiting_for_presents_nice_kids -= 1
                        matrix_list[santa_nested_list_index + 1][santa_nested_element_index] = "-"
                    if down_nested_element == "X":
                        count_presents -= 1
                        matrix_list[santa_nested_list_index + 1][santa_nested_element_index] = "-"
                if santa_nested_element_index - 1 >= 0:
                    left_nested_element = matrix_list[santa_nested_list_index][santa_nested_element_index - 1]
                    if left_nested_element == "V":
                        count_presents -= 1
                        count_waiting_for_presents_nice_kids -= 1
                        matrix_list[santa_nested_list_index][santa_nested_element_index - 1] = "-"
                    if left_nested_element == "X":
                        count_presents -= 1
                        matrix_list[santa_nested_list_index][santa_nested_element_index - 1] = "-"
                if santa_nested_element_index + 1 < len(matrix_list[santa_nested_list_index]):
                    right_nested_element = matrix_list[santa_nested_list_index][santa_nested_element_index + 1]
                    if right_nested_element == "V":
                        count_presents -= 1
                        count_waiting_for_presents_nice_kids -= 1
                        matrix_list[santa_nested_list_index][santa_nested_element_index + 1] = "-"
                    if right_nested_element == "X":
                        count_presents -= 1
                        matrix_list[santa_nested_list_index][santa_nested_element_index + 1] = "-"
                if count_presents > 0:
                    continue
                else:
                    break
            else:
                continue
        else:
            continue
    elif command == COMMAND_DOWN:
        if santa_nested_list_index + 1 < len(matrix_list):
            santa_nested_list_index += 1
            nested_element = matrix_list[santa_nested_list_index][santa_nested_element_index]
            if nested_element == "V":
                count_presents -= 1
                count_waiting_for_presents_nice_kids -= 1
                matrix_list[santa_nested_list_index][santa_nested_element_index] = "-"
                if count_presents > 0:
                    continue
                else:
                    break
            elif nested_element == "X":
                matrix_list[santa_nested_list_index][santa_nested_element_index] = "-"
            elif nested_element == "C":
                if santa_nested_list_index - 1 >= 0:
                    up_nested_element = matrix_list[santa_nested_list_index - 1][santa_nested_element_index]
                    if up_nested_element == "V":
                        count_presents -= 1
                        count_waiting_for_presents_nice_kids -= 1
                        matrix_list[santa_nested_list_index - 1][santa_nested_element_index] = "-"
                    if up_nested_element == "X":
                        count_presents -= 1
                        matrix_list[santa_nested_list_index - 1][santa_nested_element_index] = "-"
                if santa_nested_list_index + 1 < len(matrix_list):
                    down_nested_element = matrix_list[santa_nested_list_index + 1][santa_nested_element_index]
                    if down_nested_element == "V":
                        count_presents -= 1
                        count_waiting_for_presents_nice_kids -= 1
                        matrix_list[santa_nested_list_index + 1][santa_nested_element_index] = "-"
                    if down_nested_element == "X":
                        count_presents -= 1
                        matrix_list[santa_nested_list_index + 1][santa_nested_element_index] = "-"
                if santa_nested_element_index - 1 >= 0:
                    left_nested_element = matrix_list[santa_nested_list_index][santa_nested_element_index - 1]
                    if left_nested_element == "V":
                        count_presents -= 1
                        count_waiting_for_presents_nice_kids -= 1
                        matrix_list[santa_nested_list_index][santa_nested_element_index - 1] = "-"
                    if left_nested_element == "X":
                        count_presents -= 1
                        matrix_list[santa_nested_list_index][santa_nested_element_index - 1] = "-"
                if santa_nested_element_index + 1 < len(matrix_list[santa_nested_list_index]):
                    right_nested_element = matrix_list[santa_nested_list_index][santa_nested_element_index + 1]
                    if right_nested_element == "V":
                        count_presents -= 1
                        count_waiting_for_presents_nice_kids -= 1
                        matrix_list[santa_nested_list_index][santa_nested_element_index + 1] = "-"
                    if right_nested_element == "X":
                        count_presents -= 1
                        matrix_list[santa_nested_list_index][santa_nested_element_index + 1] = "-"
                if count_presents > 0:
                    continue
                else:
                    break
            else:
                continue
        else:
            continue
    elif command == COMMAND_LEFT:
        if santa_nested_element_index - 1 >= 0:
            santa_nested_element_index -= 1
            nested_element = matrix_list[santa_nested_list_index][santa_nested_element_index]
            if nested_element == "V":
                count_presents -= 1
                count_waiting_for_presents_nice_kids -= 1
                matrix_list[santa_nested_list_index][santa_nested_element_index] = "-"
                if count_presents > 0:
                    continue
                else:
                    break
            elif nested_element == "X":
                matrix_list[santa_nested_list_index][santa_nested_element_index] = "-"
            elif nested_element == "C":
                if santa_nested_list_index - 1 >= 0:
                    up_nested_element = matrix_list[santa_nested_list_index - 1][santa_nested_element_index]
                    if up_nested_element == "V":
                        count_presents -= 1
                        count_waiting_for_presents_nice_kids -= 1
                        matrix_list[santa_nested_list_index - 1][santa_nested_element_index] = "-"
                    if up_nested_element == "X":
                        count_presents -= 1
                        matrix_list[santa_nested_list_index - 1][santa_nested_element_index] = "-"
                if santa_nested_list_index + 1 < len(matrix_list):
                    down_nested_element = matrix_list[santa_nested_list_index + 1][santa_nested_element_index]
                    if down_nested_element == "V":
                        count_presents -= 1
                        count_waiting_for_presents_nice_kids -= 1
                        matrix_list[santa_nested_list_index + 1][santa_nested_element_index] = "-"
                    if down_nested_element == "X":
                        count_presents -= 1
                        matrix_list[santa_nested_list_index + 1][santa_nested_element_index] = "-"
                if santa_nested_element_index - 1 >= 0:
                    left_nested_element = matrix_list[santa_nested_list_index][santa_nested_element_index - 1]
                    if left_nested_element == "V":
                        count_presents -= 1
                        count_waiting_for_presents_nice_kids -= 1
                        matrix_list[santa_nested_list_index][santa_nested_element_index - 1] = "-"
                    if left_nested_element == "X":
                        count_presents -= 1
                        matrix_list[santa_nested_list_index][santa_nested_element_index - 1] = "-"
                if santa_nested_element_index + 1 < len(matrix_list[santa_nested_list_index]):
                    right_nested_element = matrix_list[santa_nested_list_index][santa_nested_element_index + 1]
                    if right_nested_element == "V":
                        count_presents -= 1
                        count_waiting_for_presents_nice_kids -= 1
                        matrix_list[santa_nested_list_index][santa_nested_element_index + 1] = "-"
                    if right_nested_element == "X":
                        count_presents -= 1
                        matrix_list[santa_nested_list_index][santa_nested_element_index + 1] = "-"
                if count_presents > 0:
                    continue
                else:
                    break
            else:
                continue
        else:
            continue
    elif command == COMMAND_RIGHT:
        if santa_nested_element_index + 1 < len(matrix_list[santa_nested_list_index]):
            santa_nested_element_index += 1
            nested_element = matrix_list[santa_nested_list_index][santa_nested_element_index]
            if nested_element == "V":
                count_presents -= 1
                count_waiting_for_presents_nice_kids -= 1
                matrix_list[santa_nested_list_index][santa_nested_element_index] = "-"
                if count_presents > 0:
                    continue
                else:
                    break
            elif nested_element == "X":
                matrix_list[santa_nested_list_index][santa_nested_element_index] = "-"
            elif nested_element == "C":
                if santa_nested_list_index - 1 >= 0:
                    up_nested_element = matrix_list[santa_nested_list_index - 1][santa_nested_element_index]
                    if up_nested_element == "V":
                        count_presents -= 1
                        count_waiting_for_presents_nice_kids -= 1
                        matrix_list[santa_nested_list_index - 1][santa_nested_element_index] = "-"
                    if up_nested_element == "X":
                        count_presents -= 1
                        matrix_list[santa_nested_list_index - 1][santa_nested_element_index] = "-"
                if santa_nested_list_index + 1 < len(matrix_list):
                    down_nested_element = matrix_list[santa_nested_list_index + 1][santa_nested_element_index]
                    if down_nested_element == "V":
                        count_presents -= 1
                        count_waiting_for_presents_nice_kids -= 1
                        matrix_list[santa_nested_list_index + 1][santa_nested_element_index] = "-"
                    if down_nested_element == "X":
                        count_presents -= 1
                        matrix_list[santa_nested_list_index + 1][santa_nested_element_index] = "-"
                if santa_nested_element_index - 1 >= 0:
                    left_nested_element = matrix_list[santa_nested_list_index][santa_nested_element_index - 1]
                    if left_nested_element == "V":
                        count_presents -= 1
                        count_waiting_for_presents_nice_kids -= 1
                        matrix_list[santa_nested_list_index][santa_nested_element_index - 1] = "-"
                    if left_nested_element == "X":
                        count_presents -= 1
                        matrix_list[santa_nested_list_index][santa_nested_element_index - 1] = "-"
                if santa_nested_element_index + 1 < len(matrix_list[santa_nested_list_index]):
                    right_nested_element = matrix_list[santa_nested_list_index][santa_nested_element_index + 1]
                    if right_nested_element == "V":
                        count_presents -= 1
                        count_waiting_for_presents_nice_kids -= 1
                        matrix_list[santa_nested_list_index][santa_nested_element_index + 1] = "-"
                    if right_nested_element == "X":
                        count_presents -= 1
                        matrix_list[santa_nested_list_index][santa_nested_element_index + 1] = "-"
                if count_presents > 0:
                    continue
                else:
                    break
            else:
                continue
        else:
            continue
    else:
        continue
matrix_list[santa_nested_list_index][santa_nested_element_index] = "S"
if count_presents <= 0 and count_waiting_for_presents_nice_kids > 0:
    print("Santa ran out of presents!")
    for nested_list in matrix_list:
        print(*nested_list)
else:
    for nested_list in matrix_list:
        print(*nested_list)
if count_waiting_for_presents_nice_kids > 0:
    print(f"No presents for {count_waiting_for_presents_nice_kids} nice kid/s.")
else:
    print(f"Good job, Santa! {count_all_nice_kids} happy nice kid/s.")
