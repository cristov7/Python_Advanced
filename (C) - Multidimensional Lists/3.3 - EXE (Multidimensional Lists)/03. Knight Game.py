size_of_the_board = int(input())
matrix_list = []
for nested_list_index in range(size_of_the_board):
    nested_list = list(input())
    matrix_list.append(nested_list)
count_removed_knights = 0
while True:
    knights_dict = {}
    for nested_list_index in range(len(matrix_list)):
        for nested_element_index in range(len(matrix_list[nested_list_index])):
            nested_element = matrix_list[nested_list_index][nested_element_index]
            if nested_element == "K":
                count_atk_knights = 0
                if 0 <= nested_list_index - 2 < len(matrix_list) and \
                        0 <= nested_element_index - 1 < len(matrix_list[nested_list_index - 2]):
                    move = matrix_list[nested_list_index - 2][nested_element_index - 1]
                    if move == "K":
                        count_atk_knights += 1
                if 0 <= nested_list_index - 2 < len(matrix_list) and \
                        0 <= nested_element_index + 1 < len(matrix_list[nested_list_index - 2]):
                    move = matrix_list[nested_list_index - 2][nested_element_index + 1]
                    if move == "K":
                        count_atk_knights += 1
                if 0 <= nested_list_index - 1 < len(matrix_list) and \
                        0 <= nested_element_index - 2 < len(matrix_list[nested_list_index - 1]):
                    move = matrix_list[nested_list_index - 1][nested_element_index - 2]
                    if move == "K":
                        count_atk_knights += 1
                if 0 <= nested_list_index - 1 < len(matrix_list) and \
                        0 <= nested_element_index + 2 < len(matrix_list[nested_list_index - 1]):
                    move = matrix_list[nested_list_index - 1][nested_element_index + 2]
                    if move == "K":
                        count_atk_knights += 1
                if 0 <= nested_list_index + 1 < len(matrix_list) and \
                        0 <= nested_element_index - 2 < len(matrix_list[nested_list_index + 1]):
                    move = matrix_list[nested_list_index + 1][nested_element_index - 2]
                    if move == "K":
                        count_atk_knights += 1
                if 0 <= nested_list_index + 1 < len(matrix_list) and \
                        0 <= nested_element_index + 2 < len(matrix_list[nested_list_index + 1]):
                    move = matrix_list[nested_list_index + 1][nested_element_index + 2]
                    if move == "K":
                        count_atk_knights += 1
                if 0 <= nested_list_index + 2 < len(matrix_list) and \
                        0 <= nested_element_index - 1 < len(matrix_list[nested_list_index + 2]):
                    move = matrix_list[nested_list_index + 2][nested_element_index - 1]
                    if move == "K":
                        count_atk_knights += 1
                if 0 <= nested_list_index + 2 < len(matrix_list) and \
                        0 <= nested_element_index + 1 < len(matrix_list[nested_list_index + 2]):
                    move = matrix_list[nested_list_index + 2][nested_element_index + 1]
                    if move == "K":
                        count_atk_knights += 1
                coordinates_tuple = (nested_list_index, nested_element_index)
                knights_dict[coordinates_tuple] = count_atk_knights
            else:
                continue
    sorted_knights_list = sorted(knights_dict.items(), key=lambda value: value[1], reverse=True)
    knight_tuple = sorted_knights_list[0]
    coordinates_tuple = knight_tuple[0]
    count_atk_knights = knight_tuple[1]
    if count_atk_knights == 0:
        break
    else:
        nested_list_index = coordinates_tuple[0]
        nested_element_index = coordinates_tuple[1]
        matrix_list[nested_list_index][nested_element_index] = "0"
        count_removed_knights += 1
print(count_removed_knights)
