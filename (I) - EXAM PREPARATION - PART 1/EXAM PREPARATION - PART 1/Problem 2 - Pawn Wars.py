def return_chessboard_function():
    current_size_of_the_chessboard = 8
    current_matrix_list = []
    for index_nested_list in range(current_size_of_the_chessboard):
        current_nested_list = input().split()
        current_matrix_list.append(current_nested_list)
    return current_matrix_list


def return_pawns_coordinates_function(current_matrix_list):
    current_pawns_coordinates_dict = {"white": [], "black": []}
    for index_nested_list, current_nested_list in enumerate(current_matrix_list):
        for index_nested_element, current_nested_element in enumerate(current_nested_list):
            if current_nested_element == "w":
                current_white_pawn_coordinates_list = [index_nested_list, index_nested_element]
                current_pawns_coordinates_dict["white"] = current_white_pawn_coordinates_list
                if len(current_pawns_coordinates_dict["black"]) == 0:
                    continue
                else:
                    return current_pawns_coordinates_dict
            elif current_nested_element == "b":
                current_black_pawn_coordinates_list = [index_nested_list, index_nested_element]
                current_pawns_coordinates_dict["black"] = current_black_pawn_coordinates_list
                if len(current_pawns_coordinates_dict["white"]) == 0:
                    continue
                else:
                    return current_pawns_coordinates_dict
            else:
                continue


def pawn_wars_function(current_matrix_list, current_pawns_coordinates_dict):
    index_nested_element_to_column_dict = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}
    index_nested_list_to_row_dict = {0: "8", 1: "7", 2: "6", 3: "5", 4: "4", 5: "3", 6: "2", 7: "1"}
    white_pawn_coordinates_list = current_pawns_coordinates_dict["white"]
    black_pawn_coordinates_list = current_pawns_coordinates_dict["black"]

    def white_left_diagonal_function():
        if white_pawn_coordinates_list[0] - 1 >= 0 and 0 <= white_pawn_coordinates_list[1] - 1:
            left_diagonal = current_matrix_list[white_pawn_coordinates_list[0] - 1][white_pawn_coordinates_list[1] - 1]
            if left_diagonal == "b":
                letter = index_nested_element_to_column_dict[white_pawn_coordinates_list[1] - 1]
                digit = index_nested_list_to_row_dict[white_pawn_coordinates_list[0] - 1]
                square = letter + digit
                return f"Game over! White win, capture on {square}."
            else:
                return "Free position!"
        else:
            return "Invalid position!"

    def white_right_diagonal_function():
        if white_pawn_coordinates_list[0] - 1 >= 0 and white_pawn_coordinates_list[1] + 1 < len(current_matrix_list):
            right_diagonal = current_matrix_list[white_pawn_coordinates_list[0] - 1][white_pawn_coordinates_list[1] + 1]
            if right_diagonal == "b":
                letter = index_nested_element_to_column_dict[white_pawn_coordinates_list[1] + 1]
                digit = index_nested_list_to_row_dict[white_pawn_coordinates_list[0] - 1]
                square = letter + digit
                return f"Game over! White win, capture on {square}."
            else:
                return "Free position!"
        else:
            return "Invalid position!"

    def white_forward_move_function():
        current_matrix_list[white_pawn_coordinates_list[0]][white_pawn_coordinates_list[1]] = "-"
        white_pawn_coordinates_list[0] -= 1
        current_matrix_list[white_pawn_coordinates_list[0]][white_pawn_coordinates_list[1]] = "w"
        if white_pawn_coordinates_list[0] == 0:
            letter = index_nested_element_to_column_dict[white_pawn_coordinates_list[1]]
            digit = index_nested_list_to_row_dict[white_pawn_coordinates_list[0]]
            square = letter + digit
            return f"Game over! White pawn is promoted to a queen at {square}."
        else:
            return "Next turn!"

    def black_left_diagonal_function():
        if len(current_matrix_list) > black_pawn_coordinates_list[0] + 1 and 0 <= black_pawn_coordinates_list[1] - 1:
            left_diagonal = current_matrix_list[black_pawn_coordinates_list[0] + 1][black_pawn_coordinates_list[1] - 1]
            if left_diagonal == "w":
                letter = index_nested_element_to_column_dict[black_pawn_coordinates_list[1] - 1]
                digit = index_nested_list_to_row_dict[black_pawn_coordinates_list[0] + 1]
                square = letter + digit
                return f"Game over! Black win, capture on {square}."
            else:
                return "Free position!"
        else:
            return "Invalid position!"

    def black_right_diagonal_function():
        if len(current_matrix_list) > black_pawn_coordinates_list[0] + 1 and black_pawn_coordinates_list[1] + 1 < len(current_matrix_list):
            right_diagonal = current_matrix_list[black_pawn_coordinates_list[0] + 1][black_pawn_coordinates_list[1] + 1]
            if right_diagonal == "w":
                letter = index_nested_element_to_column_dict[black_pawn_coordinates_list[1] + 1]
                digit = index_nested_list_to_row_dict[black_pawn_coordinates_list[0] + 1]
                square = letter + digit
                return f"Game over! Black win, capture on {square}."
            else:
                return "Free position!"
        else:
            return "Invalid position!"

    def black_forward_move_function():
        current_matrix_list[black_pawn_coordinates_list[0]][black_pawn_coordinates_list[1]] = "-"
        black_pawn_coordinates_list[0] += 1
        current_matrix_list[black_pawn_coordinates_list[0]][black_pawn_coordinates_list[1]] = "b"
        if black_pawn_coordinates_list[0] == len(current_matrix_list) - 1:
            letter = index_nested_element_to_column_dict[black_pawn_coordinates_list[1]]
            digit = index_nested_list_to_row_dict[black_pawn_coordinates_list[0]]
            square = letter + digit
            return f"Game over! Black pawn is promoted to a queen at {square}."
        else:
            return "Next turn!"

    while True:
        white_check_left_diagonal = white_left_diagonal_function()
        if white_check_left_diagonal.startswith("Game over!"):
            print(white_check_left_diagonal)
            break
        white_check_right_diagonal = white_right_diagonal_function()
        if white_check_right_diagonal.startswith("Game over!"):
            print(white_check_right_diagonal)
            break
        white_move_forward = white_forward_move_function()
        if white_move_forward.startswith("Game over!"):
            print(white_move_forward)
            break
        black_check_left_diagonal = black_left_diagonal_function()
        if black_check_left_diagonal.startswith("Game over!"):
            print(black_check_left_diagonal)
            break
        black_check_right_diagonal = black_right_diagonal_function()
        if black_check_right_diagonal.startswith("Game over!"):
            print(black_check_right_diagonal)
            break
        black_move_forward = black_forward_move_function()
        if black_move_forward.startswith("Game over!"):
            print(black_move_forward)
            break


matrix_list = return_chessboard_function()
pawns_coordinates_dict = return_pawns_coordinates_function(matrix_list)
pawn_wars_function(matrix_list, pawns_coordinates_dict)


# size_of_the_chessboard = 8
# index_nested_element_to_column_dict = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}
# index_nested_list_to_row_dict = {0: "8", 1: "7", 2: "6", 3: "5", 4: "4", 5: "3", 6: "2", 7: "1"}
# matrix_list = []
# white_pawn_coordinates_list = []
# black_pawn_coordinates_list = []
# for index_nested_list in range(size_of_the_chessboard):
#     nested_list = input().split()
#     for index_nested_element, nested_element in enumerate(nested_list):
#         if nested_element == "w":
#             white_pawn_coordinates_list = [index_nested_list, index_nested_element]
#         elif nested_element == "b":
#             black_pawn_coordinates_list = [index_nested_list, index_nested_element]
#         else:   # elif nested_element == "-":
#             continue
#     matrix_list.append(nested_list)
# while True:
#     if white_pawn_coordinates_list[0] - 1 >= 0 and 0 <= white_pawn_coordinates_list[1] - 1:
#         left_diagonal = matrix_list[white_pawn_coordinates_list[0] - 1][white_pawn_coordinates_list[1] - 1]
#         if left_diagonal == "b":
#             letter = index_nested_element_to_column_dict[white_pawn_coordinates_list[1] - 1]
#             digit = index_nested_list_to_row_dict[white_pawn_coordinates_list[0] - 1]
#             square = letter + digit
#             print(f"Game over! White win, capture on {square}.")
#             break
#     if white_pawn_coordinates_list[0] - 1 >= 0 and white_pawn_coordinates_list[1] + 1 < len(matrix_list):
#         right_diagonal = matrix_list[white_pawn_coordinates_list[0] - 1][white_pawn_coordinates_list[1] + 1]
#         if right_diagonal == "b":
#             letter = index_nested_element_to_column_dict[white_pawn_coordinates_list[1] + 1]
#             digit = index_nested_list_to_row_dict[white_pawn_coordinates_list[0] - 1]
#             square = letter + digit
#             print(f"Game over! White win, capture on {square}.")
#             break
#     matrix_list[white_pawn_coordinates_list[0]][white_pawn_coordinates_list[1]] = "-"
#     white_pawn_coordinates_list[0] -= 1
#     matrix_list[white_pawn_coordinates_list[0]][white_pawn_coordinates_list[1]] = "w"
#     if white_pawn_coordinates_list[0] == 0:
#         letter = index_nested_element_to_column_dict[white_pawn_coordinates_list[1]]
#         digit = index_nested_list_to_row_dict[white_pawn_coordinates_list[0]]
#         square = letter + digit
#         print(f"Game over! White pawn is promoted to a queen at {square}.")
#         break
#     if len(matrix_list) > black_pawn_coordinates_list[0] + 1 and 0 <= black_pawn_coordinates_list[1] - 1:
#         left_diagonal = matrix_list[black_pawn_coordinates_list[0] + 1][black_pawn_coordinates_list[1] - 1]
#         if left_diagonal == "w":
#             letter = index_nested_element_to_column_dict[black_pawn_coordinates_list[1] - 1]
#             digit = index_nested_list_to_row_dict[black_pawn_coordinates_list[0] + 1]
#             square = letter + digit
#             print(f"Game over! Black win, capture on {square}.")
#             break
#     if len(matrix_list) > black_pawn_coordinates_list[0] + 1 and black_pawn_coordinates_list[1] + 1 < len(matrix_list):
#         right_diagonal = matrix_list[black_pawn_coordinates_list[0] + 1][black_pawn_coordinates_list[1] + 1]
#         if right_diagonal == "w":
#             letter = index_nested_element_to_column_dict[black_pawn_coordinates_list[1] + 1]
#             digit = index_nested_list_to_row_dict[black_pawn_coordinates_list[0] + 1]
#             square = letter + digit
#             print(f"Game over! Black win, capture on {square}.")
#             break
#     matrix_list[black_pawn_coordinates_list[0]][black_pawn_coordinates_list[1]] = "-"
#     black_pawn_coordinates_list[0] += 1
#     matrix_list[black_pawn_coordinates_list[0]][black_pawn_coordinates_list[1]] = "b"
#     if black_pawn_coordinates_list[0] == len(matrix_list) - 1:
#         letter = index_nested_element_to_column_dict[black_pawn_coordinates_list[1]]
#         digit = index_nested_list_to_row_dict[black_pawn_coordinates_list[0]]
#         square = letter + digit
#         print(f"Game over! Black pawn is promoted to a queen at {square}.")
#         break
