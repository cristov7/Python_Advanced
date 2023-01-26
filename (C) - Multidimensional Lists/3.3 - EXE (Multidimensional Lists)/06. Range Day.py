matrix_list = []
for nested_list_index in range(5):
    nested_list = input().split()
    matrix_list.append(nested_list)
coordinate_nested_list_index = None
coordinate_nested_element_index = None
count_targets = 0
for nested_list_index in range(len(matrix_list)):
    for nested_element_index in range(len(matrix_list[nested_list_index])):
        nested_element = matrix_list[nested_list_index][nested_element_index]
        if nested_element == "A":
            coordinate_nested_list_index = nested_list_index
            coordinate_nested_element_index = nested_element_index
            matrix_list[coordinate_nested_list_index][coordinate_nested_element_index] = "."
        elif nested_element == "x":
            count_targets += 1
        else:
            continue
count_targets_left = count_targets
targets_list = []
targets_left_bool = True
count_commands = int(input())
for command_index in range(count_commands):
    command_list = input().split()
    command = command_list[0]
    if command == "move":
        move = command_list[1]
        if move == "right":
            steps = int(command_list[2])
            if coordinate_nested_element_index + steps < len(matrix_list[coordinate_nested_list_index]):
                nested_element = matrix_list[coordinate_nested_list_index][coordinate_nested_element_index + steps]
                if nested_element == ".":
                    coordinate_nested_element_index += steps
                else:
                    continue
            else:
                continue
        elif move == "left":
            steps = int(command_list[2])
            if coordinate_nested_element_index - steps >= 0:
                nested_element = matrix_list[coordinate_nested_list_index][coordinate_nested_element_index - steps]
                if nested_element == ".":
                    coordinate_nested_element_index -= steps
                else:
                    continue
            else:
                continue
        elif move == "up":
            steps = int(command_list[2])
            if coordinate_nested_list_index - steps >= 0:
                nested_element = matrix_list[coordinate_nested_list_index - steps][coordinate_nested_element_index]
                if nested_element == ".":
                    coordinate_nested_list_index -= steps
                else:
                    continue
            else:
                continue
        elif move == "down":
            steps = int(command_list[2])
            if coordinate_nested_list_index + steps < len(matrix_list):
                nested_element = matrix_list[coordinate_nested_list_index + steps][coordinate_nested_element_index]
                if nested_element == ".":
                    coordinate_nested_list_index += steps
                else:
                    continue
            else:
                continue
        else:
            continue
    elif command == "shoot":
        direction = command_list[1]
        if direction == "right":
            if coordinate_nested_element_index < len(matrix_list[coordinate_nested_list_index]) - 1:
                for nested_element_index in range(coordinate_nested_element_index + 1, len(matrix_list[coordinate_nested_list_index])):
                    nested_element = matrix_list[coordinate_nested_list_index][nested_element_index]
                    if nested_element == "x":
                        count_targets_left -= 1
                        targets_list.append([coordinate_nested_list_index, nested_element_index])
                        matrix_list[coordinate_nested_list_index][nested_element_index] = "."
                        if count_targets_left == 0:
                            targets_left_bool = False
                            break
                        else:
                            break
                    else:
                        continue
            else:
                continue
        elif direction == "left":
            if coordinate_nested_element_index > 0:
                for nested_element_index in range(coordinate_nested_element_index - 1, -1, -1):
                    nested_element = matrix_list[coordinate_nested_list_index][nested_element_index]
                    if nested_element == "x":
                        count_targets_left -= 1
                        targets_list.append([coordinate_nested_list_index, nested_element_index])
                        matrix_list[coordinate_nested_list_index][nested_element_index] = "."
                        if count_targets_left == 0:
                            targets_left_bool = False
                            break
                        else:
                            break
                    else:
                        continue
            else:
                continue
        elif direction == "up":
            if coordinate_nested_list_index > 0:
                for nested_list_index in range(coordinate_nested_list_index - 1, -1, -1):
                    nested_element = matrix_list[nested_list_index][coordinate_nested_element_index]
                    if nested_element == "x":
                        count_targets_left -= 1
                        targets_list.append([nested_list_index, coordinate_nested_element_index])
                        matrix_list[nested_list_index][coordinate_nested_element_index] = "."
                        if count_targets_left == 0:
                            targets_left_bool = False
                            break
                        else:
                            break
                    else:
                        continue
            else:
                continue
        elif direction == "down":
            if coordinate_nested_list_index < len(matrix_list) - 1:
                for nested_list_index in range(coordinate_nested_list_index + 1, len(matrix_list)):
                    nested_element = matrix_list[nested_list_index][coordinate_nested_element_index]
                    if nested_element == "x":
                        count_targets_left -= 1
                        targets_list.append([nested_list_index, coordinate_nested_element_index])
                        matrix_list[nested_list_index][coordinate_nested_element_index] = "."
                        if count_targets_left == 0:
                            targets_left_bool = False
                            break
                        else:
                            break
                    else:
                        continue
            else:
                continue
        else:
            continue
    if targets_left_bool:
        continue
    else:
        break
if targets_left_bool:
    print(f"Training not completed! {count_targets_left} targets left.")
else:
    print(f"Training completed! All {count_targets} targets hit.")
for nested_target_list_index in range(len(targets_list)):
    nested_target_list = targets_list[nested_target_list_index]
    print(nested_target_list)
