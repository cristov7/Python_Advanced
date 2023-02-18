def return_matrix_list_function(current_count_playground_dimensions_list):
    current_matrix_list = []
    current_count_nested_lists = current_count_playground_dimensions_list[0]
    current_count_nested_elements = current_count_playground_dimensions_list[1]
    for index_nested_list in range(current_count_nested_lists):
        current_nested_list = input().split()
        if len(current_nested_list) == current_count_nested_elements:
            current_matrix_list.append(current_nested_list)
        else:
            continue
    return current_matrix_list


def return_coordinates_list_function(current_matrix_list):
    for index_nested_list, current_nested_list in enumerate(current_matrix_list):
        if "B" in current_nested_list:
            for index_nested_element, current_nested_element in enumerate(current_nested_list):
                if current_nested_element == "B":
                    current_blind_man_coordinates_list = [index_nested_list, index_nested_element]
                    return current_blind_man_coordinates_list
                else:
                    continue
        else:
            continue


def blind_man_buff_function(current_playground_dimensions_list, current_matrix_list, current_blind_man_coordinates_list, current_count_other_players):
    def print_output_list_function():
        print("Game over!")
        print(f"Touched opponents: {count_touched_opponents} Moves made: {count_moves_made}")

    def command_up_function(current_count_moves_made, current_count_touched_opponents):
        if 0 <= current_blind_man_coordinates_list[0] - 1:
            current_move_to_position = current_matrix_list[current_blind_man_coordinates_list[0] - 1][current_blind_man_coordinates_list[1]]
            if current_move_to_position == "O":
                return [current_count_moves_made, current_count_touched_opponents]
            elif current_move_to_position == "P":
                current_matrix_list[current_blind_man_coordinates_list[0]][current_blind_man_coordinates_list[1]] = "-"
                current_count_moves_made += 1
                current_count_touched_opponents += 1
                current_blind_man_coordinates_list[0] -= 1
                current_matrix_list[current_blind_man_coordinates_list[0]][current_blind_man_coordinates_list[1]] = "B"
                if current_count_other_players == current_count_touched_opponents:
                    return [current_count_moves_made, current_count_touched_opponents, "Game over!"]
                else:
                    return [current_count_moves_made, current_count_touched_opponents]
            else:  # elif move_to_position == "-":
                current_matrix_list[current_blind_man_coordinates_list[0]][current_blind_man_coordinates_list[1]] = "-"
                current_count_moves_made += 1
                current_blind_man_coordinates_list[0] -= 1
                current_matrix_list[current_blind_man_coordinates_list[0]][current_blind_man_coordinates_list[1]] = "B"
                return [current_count_moves_made, current_count_touched_opponents]
        return [current_count_moves_made, current_count_touched_opponents]

    def command_down_function(current_count_moves_made, current_count_touched_opponents):
        if current_blind_man_coordinates_list[0] + 1 < current_playground_dimensions_list[0]:
            current_move_to_position = current_matrix_list[current_blind_man_coordinates_list[0] + 1][current_blind_man_coordinates_list[1]]
            if current_move_to_position == "O":
                return [current_count_moves_made, current_count_touched_opponents]
            elif current_move_to_position == "P":
                current_matrix_list[current_blind_man_coordinates_list[0]][current_blind_man_coordinates_list[1]] = "-"
                current_count_moves_made += 1
                current_count_touched_opponents += 1
                current_blind_man_coordinates_list[0] += 1
                current_matrix_list[current_blind_man_coordinates_list[0]][current_blind_man_coordinates_list[1]] = "B"
                if current_count_other_players == current_count_touched_opponents:
                    return [current_count_moves_made, current_count_touched_opponents, "Game over!"]
                else:
                    return [current_count_moves_made, current_count_touched_opponents]
            else:  # elif move_to_position == "-":
                current_matrix_list[current_blind_man_coordinates_list[0]][current_blind_man_coordinates_list[1]] = "-"
                current_count_moves_made += 1
                current_blind_man_coordinates_list[0] += 1
                current_matrix_list[current_blind_man_coordinates_list[0]][current_blind_man_coordinates_list[1]] = "B"
                return [current_count_moves_made, current_count_touched_opponents]
        return [current_count_moves_made, current_count_touched_opponents]

    def command_left_function(current_count_moves_made, current_count_touched_opponents):
        if 0 <= current_blind_man_coordinates_list[1] - 1:
            current_move_to_position = current_matrix_list[current_blind_man_coordinates_list[0]][current_blind_man_coordinates_list[1] - 1]
            if current_move_to_position == "O":
                return [current_count_moves_made, current_count_touched_opponents]
            elif current_move_to_position == "P":
                current_matrix_list[current_blind_man_coordinates_list[0]][current_blind_man_coordinates_list[1]] = "-"
                current_count_moves_made += 1
                current_count_touched_opponents += 1
                current_blind_man_coordinates_list[1] -= 1
                current_matrix_list[current_blind_man_coordinates_list[0]][current_blind_man_coordinates_list[1]] = "B"
                if current_count_other_players == current_count_touched_opponents:
                    return [current_count_moves_made, current_count_touched_opponents, "Game over!"]
                else:
                    return [current_count_moves_made, current_count_touched_opponents]
            else:  # elif move_to_position == "-":
                current_matrix_list[current_blind_man_coordinates_list[0]][current_blind_man_coordinates_list[1]] = "-"
                current_count_moves_made += 1
                current_blind_man_coordinates_list[1] -= 1
                current_matrix_list[current_blind_man_coordinates_list[0]][current_blind_man_coordinates_list[1]] = "B"
                return [current_count_moves_made, current_count_touched_opponents]
        return [current_count_moves_made, current_count_touched_opponents]

    def command_right_function(current_count_moves_made, current_count_touched_opponents):
        if current_blind_man_coordinates_list[1] + 1 < current_playground_dimensions_list[1]:
            current_move_to_position = current_matrix_list[current_blind_man_coordinates_list[0]][current_blind_man_coordinates_list[1] + 1]
            if current_move_to_position == "O":
                return [current_count_moves_made, current_count_touched_opponents]
            elif current_move_to_position == "P":
                current_matrix_list[current_blind_man_coordinates_list[0]][current_blind_man_coordinates_list[1]] = "-"
                current_count_moves_made += 1
                current_count_touched_opponents += 1
                current_blind_man_coordinates_list[1] += 1
                current_matrix_list[current_blind_man_coordinates_list[0]][current_blind_man_coordinates_list[1]] = "B"
                if current_count_other_players == current_count_touched_opponents:
                    return [current_count_moves_made, current_count_touched_opponents, "Game over!"]
                else:
                    return [current_count_moves_made, current_count_touched_opponents]
            else:  # elif move_to_position == "-":
                current_matrix_list[current_blind_man_coordinates_list[0]][current_blind_man_coordinates_list[1]] = "-"
                current_count_moves_made += 1
                current_blind_man_coordinates_list[1] += 1
                current_matrix_list[current_blind_man_coordinates_list[0]][current_blind_man_coordinates_list[1]] = "B"
                return [current_count_moves_made, current_count_touched_opponents]
        return [current_count_moves_made, current_count_touched_opponents]

    count_moves_made = 0
    count_touched_opponents = 0
    while True:
        command = input()
        if command == "Finish":
            break
        elif command == "up":
            command_list = command_up_function(count_moves_made, count_touched_opponents)
            if "Game over!" in command_list:
                count_moves_made = command_list[0]
                count_touched_opponents = command_list[1]
                break
            else:
                count_moves_made, count_touched_opponents = command_list
        elif command == "down":
            command_list = command_down_function(count_moves_made, count_touched_opponents)
            if "Game over!" in command_list:
                count_moves_made = command_list[0]
                count_touched_opponents = command_list[1]
                break
            else:
                count_moves_made, count_touched_opponents = command_list
        elif command == "left":
            command_list = command_left_function(count_moves_made, count_touched_opponents)
            if "Game over!" in command_list:
                count_moves_made = command_list[0]
                count_touched_opponents = command_list[1]
                break
            else:
                count_moves_made, count_touched_opponents = command_list
        elif command == "right":
            command_list = command_right_function(count_moves_made, count_touched_opponents)
            if "Game over!" in command_list:
                count_moves_made = command_list[0]
                count_touched_opponents = command_list[1]
                break
            else:
                count_moves_made, count_touched_opponents = command_list
        else:
            continue
    print_output_list_function()


playground_dimensions_list = list(map(int, input().split()))
matrix_list = return_matrix_list_function(playground_dimensions_list)
blind_man_coordinates_list = return_coordinates_list_function(matrix_list)
count_other_players = 3
blind_man_buff_function(playground_dimensions_list, matrix_list, blind_man_coordinates_list, count_other_players)


# playground_dimensions_list = list(map(int, input().split()))
# count_nested_lists = playground_dimensions_list[0]
# count_nested_elements = playground_dimensions_list[1]
# matrix_list = []
# coordinates_index_nested_list = 0
# coordinates_index_nested_element = 0
# for index_nested_list in range(count_nested_lists):
#     nested_list = input().split()
#     if len(nested_list) == count_nested_elements:
#         if "B" in nested_list:
#             for index_nested_element, nested_element in enumerate(nested_list):
#                 if nested_element == "B":
#                     coordinates_index_nested_list = index_nested_list
#                     coordinates_index_nested_element = index_nested_element
#                     break
#                 else:
#                     continue
#             matrix_list.append(nested_list)
#         else:
#             matrix_list.append(nested_list)
#     else:
#         continue
# count_moves_made = 0
# count_other_players = 3
# count_touched_opponents = 0
# COMMAND_FINISH = "Finish"
# COMMAND_UP = "up"
# COMMAND_DOWN = "down"
# COMMAND_LEFT = "left"
# COMMAND_RIGHT = "right"
# while True:
#     command = input()
#     if command == COMMAND_FINISH:
#         break
#     elif command == COMMAND_UP:
#         if 0 <= coordinates_index_nested_list - 1:
#             move_to_position = matrix_list[coordinates_index_nested_list - 1][coordinates_index_nested_element]
#             if move_to_position == "O":
#                 continue
#             elif move_to_position == "P":
#                 matrix_list[coordinates_index_nested_list][coordinates_index_nested_element] = "-"
#                 count_moves_made += 1
#                 count_touched_opponents += 1
#                 coordinates_index_nested_list -= 1
#                 matrix_list[coordinates_index_nested_list][coordinates_index_nested_element] = "B"
#                 if count_other_players == count_touched_opponents:
#                     break
#                 else:
#                     continue
#             else:   # elif move_to_position == "-":
#                 matrix_list[coordinates_index_nested_list][coordinates_index_nested_element] = "-"
#                 count_moves_made += 1
#                 coordinates_index_nested_list -= 1
#                 matrix_list[coordinates_index_nested_list][coordinates_index_nested_element] = "B"
#         else:
#             continue
#     elif command == COMMAND_DOWN:
#         if coordinates_index_nested_list + 1 < count_nested_lists:
#             move_to_position = matrix_list[coordinates_index_nested_list + 1][coordinates_index_nested_element]
#             if move_to_position == "O":
#                 continue
#             elif move_to_position == "P":
#                 matrix_list[coordinates_index_nested_list][coordinates_index_nested_element] = "-"
#                 count_moves_made += 1
#                 count_touched_opponents += 1
#                 coordinates_index_nested_list += 1
#                 matrix_list[coordinates_index_nested_list][coordinates_index_nested_element] = "B"
#                 if count_other_players == count_touched_opponents:
#                     break
#                 else:
#                     continue
#             else:  # elif move_to_position == "-":
#                 matrix_list[coordinates_index_nested_list][coordinates_index_nested_element] = "-"
#                 count_moves_made += 1
#                 coordinates_index_nested_list += 1
#                 matrix_list[coordinates_index_nested_list][coordinates_index_nested_element] = "B"
#         else:
#             continue
#     elif command == COMMAND_LEFT:
#         if 0 <= coordinates_index_nested_element - 1:
#             move_to_position = matrix_list[coordinates_index_nested_list][coordinates_index_nested_element - 1]
#             if move_to_position == "O":
#                 continue
#             elif move_to_position == "P":
#                 matrix_list[coordinates_index_nested_list][coordinates_index_nested_element] = "-"
#                 count_moves_made += 1
#                 count_touched_opponents += 1
#                 coordinates_index_nested_element -= 1
#                 matrix_list[coordinates_index_nested_list][coordinates_index_nested_element] = "B"
#                 if count_other_players == count_touched_opponents:
#                     break
#                 else:
#                     continue
#             else:  # elif move_to_position == "-":
#                 matrix_list[coordinates_index_nested_list][coordinates_index_nested_element] = "-"
#                 count_moves_made += 1
#                 coordinates_index_nested_element -= 1
#                 matrix_list[coordinates_index_nested_list][coordinates_index_nested_element] = "B"
#         else:
#             continue
#     elif command == COMMAND_RIGHT:
#         if coordinates_index_nested_element + 1 < count_nested_elements:
#             move_to_position = matrix_list[coordinates_index_nested_list][coordinates_index_nested_element + 1]
#             if move_to_position == "O":
#                 continue
#             elif move_to_position == "P":
#                 matrix_list[coordinates_index_nested_list][coordinates_index_nested_element] = "-"
#                 count_moves_made += 1
#                 count_touched_opponents += 1
#                 coordinates_index_nested_element += 1
#                 matrix_list[coordinates_index_nested_list][coordinates_index_nested_element] = "B"
#                 if count_other_players == count_touched_opponents:
#                     break
#                 else:
#                     continue
#             else:  # elif move_to_position == "-":
#                 matrix_list[coordinates_index_nested_list][coordinates_index_nested_element] = "-"
#                 count_moves_made += 1
#                 coordinates_index_nested_element += 1
#                 matrix_list[coordinates_index_nested_list][coordinates_index_nested_element] = "B"
#         else:
#             continue
#     else:
#         continue
# print("Game over!")
# print(f"Touched opponents: {count_touched_opponents} Moves made: {count_moves_made}")
