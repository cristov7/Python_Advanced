def return_matrix_list_function():
    current_count_nested_lists = 6
    current_matrix_list = []
    for current_index_nested_list in range(current_count_nested_lists):
        current_nested_list = input().split()
        current_matrix_list.append(current_nested_list)
    return current_matrix_list


def return_rover_coordinates_list_function(current_matrix_list):
    for current_index_nested_list, current_nested_list in enumerate(current_matrix_list):
        for current_index_nested_element, current_nested_element in enumerate(current_nested_list):
            if current_nested_element == "E":
                current_rover_coordinates_list = [current_index_nested_list, current_index_nested_element]
                return current_rover_coordinates_list
            else:
                continue


def martian_explorer_function(current_matrix_list, current_rover_coordinates_list):
    def print_conclusion_from_area_function():
        if water_deposit > 0 and metal_deposit > 0 and concrete_deposit > 0:
            print("Area suitable to start the colony.")
        else:
            print("Area not suitable to start the colony.")

    def empty_positions_function():
        current_matrix_list[current_rover_coordinates_list[0]][current_rover_coordinates_list[1]] = "E"

    def return_water_deposit_function(current_water_deposit):
        current_water_deposit += 1
        print(f"Water deposit found at ({current_rover_coordinates_list[0]}, {current_rover_coordinates_list[1]})")
        current_matrix_list[current_rover_coordinates_list[0]][current_rover_coordinates_list[1]] = "E"
        return current_water_deposit

    def return_metal_deposit_function(current_metal_deposit):
        current_metal_deposit += 1
        print(f"Metal deposit found at ({current_rover_coordinates_list[0]}, {current_rover_coordinates_list[1]})")
        current_matrix_list[current_rover_coordinates_list[0]][current_rover_coordinates_list[1]] = "E"
        return current_metal_deposit

    def return_concrete_deposit_function(current_concrete_deposit):
        current_concrete_deposit += 1
        print(f"Concrete deposit found at ({current_rover_coordinates_list[0]}, {current_rover_coordinates_list[1]})")
        current_matrix_list[current_rover_coordinates_list[0]][current_rover_coordinates_list[1]] = "E"
        return current_concrete_deposit

    def rover_got_broken_function():
        print(f"Rover got broken at ({current_rover_coordinates_list[0]}, {current_rover_coordinates_list[1]})")
        current_matrix_list[current_rover_coordinates_list[0]][current_rover_coordinates_list[1]] = "E"

    water_deposit = 0
    metal_deposit = 0
    concrete_deposit = 0
    commands_list = input().split(", ")
    for command in commands_list:
        if command == "up":
            current_matrix_list[current_rover_coordinates_list[0]][current_rover_coordinates_list[1]] = "-"
            if 0 <= current_rover_coordinates_list[0] - 1:
                current_rover_coordinates_list[0] -= 1
            else:
                current_rover_coordinates_list[0] = len(current_matrix_list) - 1
            nested_element = current_matrix_list[current_rover_coordinates_list[0]][current_rover_coordinates_list[1]]
            if nested_element == "-":
                empty_positions_function()
            elif nested_element == "W":
                water_deposit = return_water_deposit_function(water_deposit)
            elif nested_element == "M":
                metal_deposit = return_metal_deposit_function(metal_deposit)
            elif nested_element == "C":
                concrete_deposit = return_concrete_deposit_function(concrete_deposit)
            elif nested_element == "R":
                rover_got_broken_function()
                break
            else:
                continue
        elif command == "down":
            current_matrix_list[current_rover_coordinates_list[0]][current_rover_coordinates_list[1]] = "-"
            if current_rover_coordinates_list[0] + 1 < len(current_matrix_list):
                current_rover_coordinates_list[0] += 1
            else:
                current_rover_coordinates_list[0] = 0
            nested_element = current_matrix_list[current_rover_coordinates_list[0]][current_rover_coordinates_list[1]]
            if nested_element == "-":
                empty_positions_function()
            elif nested_element == "W":
                water_deposit = return_water_deposit_function(water_deposit)
            elif nested_element == "M":
                metal_deposit = return_metal_deposit_function(metal_deposit)
            elif nested_element == "C":
                concrete_deposit = return_concrete_deposit_function(concrete_deposit)
            elif nested_element == "R":
                rover_got_broken_function()
                break
            else:
                continue
        elif command == "left":
            current_matrix_list[current_rover_coordinates_list[0]][current_rover_coordinates_list[1]] = "-"
            if 0 <= current_rover_coordinates_list[1] - 1:
                current_rover_coordinates_list[1] -= 1
            else:
                current_rover_coordinates_list[1] = len(current_matrix_list) - 1
            nested_element = current_matrix_list[current_rover_coordinates_list[0]][current_rover_coordinates_list[1]]
            if nested_element == "-":
                empty_positions_function()
            elif nested_element == "W":
                water_deposit = return_water_deposit_function(water_deposit)
            elif nested_element == "M":
                metal_deposit = return_metal_deposit_function(metal_deposit)
            elif nested_element == "C":
                concrete_deposit = return_concrete_deposit_function(concrete_deposit)
            elif nested_element == "R":
                rover_got_broken_function()
                break
            else:
                continue
        elif command == "right":
            current_matrix_list[current_rover_coordinates_list[0]][current_rover_coordinates_list[1]] = "-"
            if current_rover_coordinates_list[1] + 1 < len(current_matrix_list):
                current_rover_coordinates_list[1] += 1
            else:
                current_rover_coordinates_list[1] = 0
            nested_element = current_matrix_list[current_rover_coordinates_list[0]][current_rover_coordinates_list[1]]
            if nested_element == "-":
                empty_positions_function()
            elif nested_element == "W":
                water_deposit = return_water_deposit_function(water_deposit)
            elif nested_element == "M":
                metal_deposit = return_metal_deposit_function(metal_deposit)
            elif nested_element == "C":
                concrete_deposit = return_concrete_deposit_function(concrete_deposit)
            elif nested_element == "R":
                rover_got_broken_function()
                break
            else:
                continue
        else:
            continue
    print_conclusion_from_area_function()


matrix_list = return_matrix_list_function()
rover_coordinates_list = return_rover_coordinates_list_function(matrix_list)
martian_explorer_function(matrix_list, rover_coordinates_list)


# count_nested_lists = 6
# matrix_list = []
# rover_coordinates_list = []
# for index_nested_list in range(count_nested_lists):
#     nested_list = input().split()
#     for index_nested_element, nested_element in enumerate(nested_list):
#         if nested_element == "E":
#             rover_coordinates_list = [index_nested_list, index_nested_element]
#         else:
#             continue
#     matrix_list.append(nested_list)
# water_deposit = 0
# metal_deposit = 0
# concrete_deposit = 0
# COMMAND_UP = "up"
# COMMAND_DOWN = "down"
# COMMAND_LEFT = "left"
# COMMAND_RIGHT = "right"
# commands_list = input().split(", ")
# for command in commands_list:
#     if command == COMMAND_UP:
#         matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "-"
#         if 0 <= rover_coordinates_list[0] - 1:
#             rover_coordinates_list[0] -= 1
#             nested_element = matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]]
#             if nested_element == "W":
#                 water_deposit += 1
#                 print(f"Water deposit found at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#             elif nested_element == "M":
#                 metal_deposit += 1
#                 print(f"Metal deposit found at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#             elif nested_element == "C":
#                 concrete_deposit += 1
#                 print(f"Concrete deposit found at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#             elif nested_element == "R":
#                 print(f"Rover got broken at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#                 break
#             else:   # elif nested_element == "-":
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#         else:
#             rover_coordinates_list[0] = count_nested_lists - 1
#             nested_element = matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]]
#             if nested_element == "W":
#                 water_deposit += 1
#                 print(f"Water deposit found at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#             elif nested_element == "M":
#                 metal_deposit += 1
#                 print(f"Metal deposit found at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#             elif nested_element == "C":
#                 concrete_deposit += 1
#                 print(f"Concrete deposit found at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#             elif nested_element == "R":
#                 print(f"Rover got broken at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#                 break
#             else:   # elif nested_element == "-":
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#     elif command == COMMAND_DOWN:
#         matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "-"
#         if rover_coordinates_list[0] + 1 < count_nested_lists:
#             rover_coordinates_list[0] += 1
#             nested_element = matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]]
#             if nested_element == "W":
#                 water_deposit += 1
#                 print(f"Water deposit found at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#             elif nested_element == "M":
#                 metal_deposit += 1
#                 print(f"Metal deposit found at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#             elif nested_element == "C":
#                 concrete_deposit += 1
#                 print(f"Concrete deposit found at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#             elif nested_element == "R":
#                 print(f"Rover got broken at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#                 break
#             else:  # elif nested_element == "-":
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#         else:
#             rover_coordinates_list[0] = 0
#             nested_element = matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]]
#             if nested_element == "W":
#                 water_deposit += 1
#                 print(f"Water deposit found at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#             elif nested_element == "M":
#                 metal_deposit += 1
#                 print(f"Metal deposit found at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#             elif nested_element == "C":
#                 concrete_deposit += 1
#                 print(f"Concrete deposit found at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#             elif nested_element == "R":
#                 print(f"Rover got broken at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#                 break
#             else:  # elif nested_element == "-":
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#     elif command == COMMAND_LEFT:
#         matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "-"
#         if 0 <= rover_coordinates_list[1] - 1:
#             rover_coordinates_list[1] -= 1
#             nested_element = matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]]
#             if nested_element == "W":
#                 water_deposit += 1
#                 print(f"Water deposit found at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#             elif nested_element == "M":
#                 metal_deposit += 1
#                 print(f"Metal deposit found at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#             elif nested_element == "C":
#                 concrete_deposit += 1
#                 print(f"Concrete deposit found at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#             elif nested_element == "R":
#                 print(f"Rover got broken at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#                 break
#             else:  # elif nested_element == "-":
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#         else:
#             rover_coordinates_list[1] = count_nested_lists - 1
#             nested_element = matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]]
#             if nested_element == "W":
#                 water_deposit += 1
#                 print(f"Water deposit found at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#             elif nested_element == "M":
#                 metal_deposit += 1
#                 print(f"Metal deposit found at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#             elif nested_element == "C":
#                 concrete_deposit += 1
#                 print(f"Concrete deposit found at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#             elif nested_element == "R":
#                 print(f"Rover got broken at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#                 break
#             else:  # elif nested_element == "-":
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#     elif command == COMMAND_RIGHT:
#         matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "-"
#         if rover_coordinates_list[1] + 1 < count_nested_lists:
#             rover_coordinates_list[1] += 1
#             nested_element = matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]]
#             if nested_element == "W":
#                 water_deposit += 1
#                 print(f"Water deposit found at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#             elif nested_element == "M":
#                 metal_deposit += 1
#                 print(f"Metal deposit found at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#             elif nested_element == "C":
#                 concrete_deposit += 1
#                 print(f"Concrete deposit found at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#             elif nested_element == "R":
#                 print(f"Rover got broken at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#                 break
#             else:  # elif nested_element == "-":
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#         else:
#             rover_coordinates_list[1] = 0
#             nested_element = matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]]
#             if nested_element == "W":
#                 water_deposit += 1
#                 print(f"Water deposit found at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#             elif nested_element == "M":
#                 metal_deposit += 1
#                 print(f"Metal deposit found at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#             elif nested_element == "C":
#                 concrete_deposit += 1
#                 print(f"Concrete deposit found at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#             elif nested_element == "R":
#                 print(f"Rover got broken at ({rover_coordinates_list[0]}, {rover_coordinates_list[1]})")
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#                 break
#             else:  # elif nested_element == "-":
#                 matrix_list[rover_coordinates_list[0]][rover_coordinates_list[1]] = "E"
#     else:
#         continue
# if water_deposit > 0 and metal_deposit > 0 and concrete_deposit > 0:
#     print("Area suitable to start the colony.")
# else:
#     print("Area not suitable to start the colony.")
