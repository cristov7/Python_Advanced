field_size = int(input())
commands_list = input().split()
all_coals = 0
matrix_list = []
for nested_list_index in range(field_size):
    nested_list = input().split()
    count_coals = nested_list.count("c")
    all_coals += count_coals
    matrix_list.append(nested_list)
coordinate_nested_list_index = 0
coordinate_nested_element_index = 0
find_miner = False
for nested_list_index in range(len(matrix_list)):
    if find_miner:
        break
    else:
        for nested_element_index in range(len(matrix_list[nested_list_index])):
            nested_element = matrix_list[nested_list_index][nested_element_index]
            if nested_element == "s":
                find_miner = True
                coordinate_nested_list_index = nested_list_index
                coordinate_nested_element_index = nested_element_index
                break
            else:
                continue
count_coals = 0
for command in commands_list:
    if command == "left":
        new_coordinate_nested_list_index = coordinate_nested_list_index
        new_coordinate_nested_element_index = coordinate_nested_element_index - 1
        if 0 <= new_coordinate_nested_element_index < len(matrix_list):
            coordinate_nested_list_index = new_coordinate_nested_list_index
            coordinate_nested_element_index = new_coordinate_nested_element_index
            current_nested_element = matrix_list[coordinate_nested_list_index][coordinate_nested_element_index]
            if current_nested_element == "c":
                matrix_list[coordinate_nested_list_index][coordinate_nested_element_index] = "*"
                count_coals += 1
                if count_coals == all_coals:
                    print(f"You collected all coal! ({coordinate_nested_list_index}, {coordinate_nested_element_index})")
                    raise SystemExit
                else:
                    continue
            elif current_nested_element == "e":
                print(f"Game over! ({coordinate_nested_list_index}, {coordinate_nested_element_index})")
                raise SystemExit
            else:
                continue
        else:
            continue
    elif command == "right":
        new_coordinate_nested_list_index = coordinate_nested_list_index
        new_coordinate_nested_element_index = coordinate_nested_element_index + 1
        if 0 <= new_coordinate_nested_element_index < len(matrix_list):
            coordinate_nested_list_index = new_coordinate_nested_list_index
            coordinate_nested_element_index = new_coordinate_nested_element_index
            current_nested_element = matrix_list[coordinate_nested_list_index][coordinate_nested_element_index]
            if current_nested_element == "c":
                matrix_list[coordinate_nested_list_index][coordinate_nested_element_index] = "*"
                count_coals += 1
                if count_coals == all_coals:
                    print(f"You collected all coal! ({coordinate_nested_list_index}, {coordinate_nested_element_index})")
                    raise SystemExit
                else:
                    continue
            elif current_nested_element == "e":
                print(f"Game over! ({coordinate_nested_list_index}, {coordinate_nested_element_index})")
                raise SystemExit
            else:
                continue
        else:
            continue
    elif command == "up":
        new_coordinate_nested_list_index = coordinate_nested_list_index - 1
        new_coordinate_nested_element_index = coordinate_nested_element_index
        if 0 <= new_coordinate_nested_list_index < len(matrix_list):
            coordinate_nested_list_index = new_coordinate_nested_list_index
            coordinate_nested_element_index = new_coordinate_nested_element_index
            current_nested_element = matrix_list[coordinate_nested_list_index][coordinate_nested_element_index]
            if current_nested_element == "c":
                matrix_list[coordinate_nested_list_index][coordinate_nested_element_index] = "*"
                count_coals += 1
                if count_coals == all_coals:
                    print(f"You collected all coal! ({coordinate_nested_list_index}, {coordinate_nested_element_index})")
                    raise SystemExit
                else:
                    continue
            elif current_nested_element == "e":
                print(f"Game over! ({coordinate_nested_list_index}, {coordinate_nested_element_index})")
                raise SystemExit
            else:
                continue
        else:
            continue
    elif command == "down":
        new_coordinate_nested_list_index = coordinate_nested_list_index + 1
        new_coordinate_nested_element_index = coordinate_nested_element_index
        if 0 <= new_coordinate_nested_list_index < len(matrix_list):
            coordinate_nested_list_index = new_coordinate_nested_list_index
            coordinate_nested_element_index = new_coordinate_nested_element_index
            current_nested_element = matrix_list[coordinate_nested_list_index][coordinate_nested_element_index]
            if current_nested_element == "c":
                matrix_list[coordinate_nested_list_index][coordinate_nested_element_index] = "*"
                count_coals += 1
                if count_coals == all_coals:
                    print(
                        f"You collected all coal! ({coordinate_nested_list_index}, {coordinate_nested_element_index})")
                    raise SystemExit
                else:
                    continue
            elif current_nested_element == "e":
                print(f"Game over! ({coordinate_nested_list_index}, {coordinate_nested_element_index})")
                raise SystemExit
            else:
                continue
        else:
            continue
    else:
        continue
count_remaining_coals = all_coals - count_coals
print(f"{count_remaining_coals} pieces of coal left. ({coordinate_nested_list_index}, {coordinate_nested_element_index})")
