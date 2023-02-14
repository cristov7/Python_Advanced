def return_matrix_list_function():
    size_of_the_matrix = int(input())
    current_matrix_list = []
    for index_nested_list in range(size_of_the_matrix):
        current_nested_list = list(input())
        current_matrix_list.append(current_nested_list)
    return current_matrix_list


def return_submarine_coordinates_function(current_matrix_list):
    for index_nested_list, current_nested_list in enumerate(current_matrix_list):
        for index_nested_element, current_nested_element in enumerate(current_nested_list):
            if current_nested_element == "S":
                return [index_nested_list, index_nested_element]
            else:
                continue


def navy_battle_function(current_matrix_list, current_submarine_coordinates_list):
    max_hits_from_naval_mines = 2
    count_hits_from_naval_mines = 0
    count_battle_cruiser = 3

    def command_up_function(current_count_hits_from_naval_mines, current_count_battle_cruiser):
        current_matrix_list[current_submarine_coordinates_list[0]][current_submarine_coordinates_list[1]] = "-"
        nested_element = current_matrix_list[current_submarine_coordinates_list[0] - 1][
            current_submarine_coordinates_list[1]]
        current_submarine_coordinates_list[0] -= 1
        if nested_element == "*":
            current_count_hits_from_naval_mines += 1
            if current_count_hits_from_naval_mines > max_hits_from_naval_mines:
                current_matrix_list[current_submarine_coordinates_list[0]][current_submarine_coordinates_list[1]] = "S"
                print(f"Mission failed, U-9 disappeared! Last known coordinates {current_submarine_coordinates_list}!")
                for current_nested_list in current_matrix_list:
                    print(*current_nested_list, sep="")
                return "End", "Mission"
            else:
                current_matrix_list[current_submarine_coordinates_list[0]][current_submarine_coordinates_list[1]] = "S"
        elif nested_element == "C":
            current_count_battle_cruiser -= 1
            if current_count_battle_cruiser == 0:
                current_matrix_list[current_submarine_coordinates_list[0]][current_submarine_coordinates_list[1]] = "S"
                print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
                for current_nested_list in current_matrix_list:
                    print(*current_nested_list, sep="")
                return "End", "Mission"
            else:
                current_matrix_list[current_submarine_coordinates_list[0]][current_submarine_coordinates_list[1]] = "S"
        else:  # elif nested_element == "-":
            current_matrix_list[current_submarine_coordinates_list[0]][current_submarine_coordinates_list[1]] = "S"
        return current_count_hits_from_naval_mines, current_count_battle_cruiser

    def command_down_function(current_count_hits_from_naval_mines, current_count_battle_cruiser):
        current_matrix_list[current_submarine_coordinates_list[0]][current_submarine_coordinates_list[1]] = "-"
        nested_element = current_matrix_list[current_submarine_coordinates_list[0] + 1][
            current_submarine_coordinates_list[1]]
        current_submarine_coordinates_list[0] += 1
        if nested_element == "*":
            current_count_hits_from_naval_mines += 1
            if current_count_hits_from_naval_mines > max_hits_from_naval_mines:
                current_matrix_list[current_submarine_coordinates_list[0]][current_submarine_coordinates_list[1]] = "S"
                print(f"Mission failed, U-9 disappeared! Last known coordinates {current_submarine_coordinates_list}!")
                for current_nested_list in current_matrix_list:
                    print(*current_nested_list, sep="")
                return "End", "Mission"
            else:
                current_matrix_list[current_submarine_coordinates_list[0]][current_submarine_coordinates_list[1]] = "S"
        elif nested_element == "C":
            current_count_battle_cruiser -= 1
            if current_count_battle_cruiser == 0:
                current_matrix_list[current_submarine_coordinates_list[0]][current_submarine_coordinates_list[1]] = "S"
                print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
                for current_nested_list in current_matrix_list:
                    print(*current_nested_list, sep="")
                return "End", "Mission"
            else:
                current_matrix_list[current_submarine_coordinates_list[0]][current_submarine_coordinates_list[1]] = "S"
        else:  # elif nested_element == "-":
            current_matrix_list[current_submarine_coordinates_list[0]][current_submarine_coordinates_list[1]] = "S"
        return current_count_hits_from_naval_mines, current_count_battle_cruiser

    def command_left_function(current_count_hits_from_naval_mines, current_count_battle_cruiser):
        current_matrix_list[current_submarine_coordinates_list[0]][current_submarine_coordinates_list[1]] = "-"
        nested_element = current_matrix_list[current_submarine_coordinates_list[0]][
            current_submarine_coordinates_list[1] - 1]
        current_submarine_coordinates_list[1] -= 1
        if nested_element == "*":
            current_count_hits_from_naval_mines += 1
            if current_count_hits_from_naval_mines > max_hits_from_naval_mines:
                current_matrix_list[current_submarine_coordinates_list[0]][current_submarine_coordinates_list[1]] = "S"
                print(f"Mission failed, U-9 disappeared! Last known coordinates {current_submarine_coordinates_list}!")
                for current_nested_list in current_matrix_list:
                    print(*current_nested_list, sep="")
                return "End", "Mission"
            else:
                current_matrix_list[current_submarine_coordinates_list[0]][current_submarine_coordinates_list[1]] = "S"
        elif nested_element == "C":
            current_count_battle_cruiser -= 1
            if current_count_battle_cruiser == 0:
                current_matrix_list[current_submarine_coordinates_list[0]][current_submarine_coordinates_list[1]] = "S"
                print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
                for current_nested_list in current_matrix_list:
                    print(*current_nested_list, sep="")
                return "End", "Mission"
            else:
                current_matrix_list[current_submarine_coordinates_list[0]][current_submarine_coordinates_list[1]] = "S"
        else:  # elif nested_element == "-":
            current_matrix_list[current_submarine_coordinates_list[0]][current_submarine_coordinates_list[1]] = "S"
        return current_count_hits_from_naval_mines, current_count_battle_cruiser

    def command_right_function(current_count_hits_from_naval_mines, current_count_battle_cruiser):
        current_matrix_list[current_submarine_coordinates_list[0]][current_submarine_coordinates_list[1]] = "-"
        nested_element = current_matrix_list[current_submarine_coordinates_list[0]][
            current_submarine_coordinates_list[1] + 1]
        current_submarine_coordinates_list[1] += 1
        if nested_element == "*":
            current_count_hits_from_naval_mines += 1
            if current_count_hits_from_naval_mines > max_hits_from_naval_mines:
                current_matrix_list[current_submarine_coordinates_list[0]][current_submarine_coordinates_list[1]] = "S"
                print(f"Mission failed, U-9 disappeared! Last known coordinates {current_submarine_coordinates_list}!")
                for current_nested_list in current_matrix_list:
                    print(*current_nested_list, sep="")
                return "End", "Mission"
            else:
                current_matrix_list[current_submarine_coordinates_list[0]][current_submarine_coordinates_list[1]] = "S"
        elif nested_element == "C":
            current_count_battle_cruiser -= 1
            if current_count_battle_cruiser == 0:
                current_matrix_list[current_submarine_coordinates_list[0]][current_submarine_coordinates_list[1]] = "S"
                print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
                for current_nested_list in current_matrix_list:
                    print(*current_nested_list, sep="")
                return "End", "Mission"
            else:
                current_matrix_list[current_submarine_coordinates_list[0]][current_submarine_coordinates_list[1]] = "S"
        else:  # elif nested_element == "-":
            current_matrix_list[current_submarine_coordinates_list[0]][current_submarine_coordinates_list[1]] = "S"
        return current_count_hits_from_naval_mines, current_count_battle_cruiser

    while True:
        command = input()
        if command == "":
            break
        elif command == "up" and 0 <= current_submarine_coordinates_list[0] - 1:
            count_hits_from_naval_mines, count_battle_cruiser = command_up_function(count_hits_from_naval_mines, count_battle_cruiser)
            if count_hits_from_naval_mines == "End" and count_battle_cruiser == "Mission":
                break
            else:
                continue
        elif command == "down" and current_submarine_coordinates_list[0] + 1 < len(current_matrix_list):
            count_hits_from_naval_mines, count_battle_cruiser = command_down_function(count_hits_from_naval_mines, count_battle_cruiser)
            if count_hits_from_naval_mines == "End" and count_battle_cruiser == "Mission":
                break
            else:
                continue
        elif command == "left" and 0 <= current_submarine_coordinates_list[1] - 1:
            count_hits_from_naval_mines, count_battle_cruiser = command_left_function(count_hits_from_naval_mines, count_battle_cruiser)
            if count_hits_from_naval_mines == "End" and count_battle_cruiser == "Mission":
                break
            else:
                continue
        elif command == "right" and current_submarine_coordinates_list[1] + 1 < len(current_matrix_list):
            count_hits_from_naval_mines, count_battle_cruiser = command_right_function(count_hits_from_naval_mines, count_battle_cruiser)
            if count_hits_from_naval_mines == "End" and count_battle_cruiser == "Mission":
                break
            else:
                continue
        else:
            continue


matrix_list = return_matrix_list_function()
submarine_coordinates_list = return_submarine_coordinates_function(matrix_list)
navy_battle_function(matrix_list, submarine_coordinates_list)


# size_of_the_matrix = int(input())
# matrix_list = []
# submarine_coordinates_list = []
# for index_nested_list in range(size_of_the_matrix):
#     nested_list = list(input())
#     for index_nested_element, nested_element in enumerate(nested_list):
#         if nested_element == "S":
#             submarine_coordinates_list = [index_nested_list, index_nested_element]
#     matrix_list.append(nested_list)
# max_hits_from_naval_mines = 2   # "*"
# count_hits_from_naval_mines = 0
# count_battle_cruiser = 3   # "C"
# COMMAND_UP = "up"
# COMMAND_DOWN = "down"
# COMMAND_LEFT = "left"
# COMMAND_RIGHT = "right"
# while True:
#     command = input()
#     if command == "":
#         break
#     elif command == COMMAND_UP and 0 <= submarine_coordinates_list[0] - 1:
#         matrix_list[submarine_coordinates_list[0]][submarine_coordinates_list[1]] = "-"
#         nested_element = matrix_list[submarine_coordinates_list[0] - 1][submarine_coordinates_list[1]]
#         submarine_coordinates_list[0] -= 1
#         if nested_element == "*":
#             count_hits_from_naval_mines += 1
#             if count_hits_from_naval_mines > max_hits_from_naval_mines:
#                 matrix_list[submarine_coordinates_list[0]][submarine_coordinates_list[1]] = "S"
#                 print(f"Mission failed, U-9 disappeared! Last known coordinates {submarine_coordinates_list}!")
#                 break
#             else:
#                 matrix_list[submarine_coordinates_list[0]][submarine_coordinates_list[1]] = "S"
#         elif nested_element == "C":
#             count_battle_cruiser -= 1
#             if count_battle_cruiser == 0:
#                 matrix_list[submarine_coordinates_list[0]][submarine_coordinates_list[1]] = "S"
#                 print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
#                 break
#             else:
#                 matrix_list[submarine_coordinates_list[0]][submarine_coordinates_list[1]] = "S"
#         else:   # elif nested_element == "-":
#             matrix_list[submarine_coordinates_list[0]][submarine_coordinates_list[1]] = "S"
#     elif command == COMMAND_DOWN and submarine_coordinates_list[0] + 1 < len(matrix_list):
#         matrix_list[submarine_coordinates_list[0]][submarine_coordinates_list[1]] = "-"
#         nested_element = matrix_list[submarine_coordinates_list[0] + 1][submarine_coordinates_list[1]]
#         submarine_coordinates_list[0] += 1
#         if nested_element == "*":
#             count_hits_from_naval_mines += 1
#             if count_hits_from_naval_mines > max_hits_from_naval_mines:
#                 matrix_list[submarine_coordinates_list[0]][submarine_coordinates_list[1]] = "S"
#                 print(f"Mission failed, U-9 disappeared! Last known coordinates {submarine_coordinates_list}!")
#                 break
#             else:
#                 matrix_list[submarine_coordinates_list[0]][submarine_coordinates_list[1]] = "S"
#         elif nested_element == "C":
#             count_battle_cruiser -= 1
#             if count_battle_cruiser == 0:
#                 matrix_list[submarine_coordinates_list[0]][submarine_coordinates_list[1]] = "S"
#                 print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
#                 break
#             else:
#                 matrix_list[submarine_coordinates_list[0]][submarine_coordinates_list[1]] = "S"
#         else:  # elif nested_element == "-":
#             matrix_list[submarine_coordinates_list[0]][submarine_coordinates_list[1]] = "S"
#     elif command == COMMAND_LEFT and 0 <= submarine_coordinates_list[1] - 1:
#         matrix_list[submarine_coordinates_list[0]][submarine_coordinates_list[1]] = "-"
#         nested_element = matrix_list[submarine_coordinates_list[0]][submarine_coordinates_list[1] - 1]
#         submarine_coordinates_list[1] -= 1
#         if nested_element == "*":
#             count_hits_from_naval_mines += 1
#             if count_hits_from_naval_mines > max_hits_from_naval_mines:
#                 matrix_list[submarine_coordinates_list[0]][submarine_coordinates_list[1]] = "S"
#                 print(f"Mission failed, U-9 disappeared! Last known coordinates {submarine_coordinates_list}!")
#                 break
#             else:
#                 matrix_list[submarine_coordinates_list[0]][submarine_coordinates_list[1]] = "S"
#         elif nested_element == "C":
#             count_battle_cruiser -= 1
#             if count_battle_cruiser == 0:
#                 matrix_list[submarine_coordinates_list[0]][submarine_coordinates_list[1]] = "S"
#                 print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
#                 break
#             else:
#                 matrix_list[submarine_coordinates_list[0]][submarine_coordinates_list[1]] = "S"
#         else:  # elif nested_element == "-":
#             matrix_list[submarine_coordinates_list[0]][submarine_coordinates_list[1]] = "S"
#     elif command == COMMAND_RIGHT and submarine_coordinates_list[1] + 1 < len(matrix_list):
#         matrix_list[submarine_coordinates_list[0]][submarine_coordinates_list[1]] = "-"
#         nested_element = matrix_list[submarine_coordinates_list[0]][submarine_coordinates_list[1] + 1]
#         submarine_coordinates_list[1] += 1
#         if nested_element == "*":
#             count_hits_from_naval_mines += 1
#             if count_hits_from_naval_mines > max_hits_from_naval_mines:
#                 matrix_list[submarine_coordinates_list[0]][submarine_coordinates_list[1]] = "S"
#                 print(f"Mission failed, U-9 disappeared! Last known coordinates {submarine_coordinates_list}!")
#                 break
#             else:
#                 matrix_list[submarine_coordinates_list[0]][submarine_coordinates_list[1]] = "S"
#         elif nested_element == "C":
#             count_battle_cruiser -= 1
#             if count_battle_cruiser == 0:
#                 matrix_list[submarine_coordinates_list[0]][submarine_coordinates_list[1]] = "S"
#                 print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
#                 break
#             else:
#                 matrix_list[submarine_coordinates_list[0]][submarine_coordinates_list[1]] = "S"
#         else:  # elif nested_element == "-":
#             matrix_list[submarine_coordinates_list[0]][submarine_coordinates_list[1]] = "S"
#     else:
#         continue
# for nested_list in matrix_list:
#     print(*nested_list, sep="")
