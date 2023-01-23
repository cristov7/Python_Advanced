def creating_matrix_list_function():
    current_matrix_list = []
    for nested_list_index in range(int(input())):
        current_nested_list = list(input())
        current_matrix_list.append(current_nested_list)
    return current_matrix_list


def check_char_in_matrix_list_function(current_matrix_list: list, current_char: str):
    for current_nested_list_index in range(len(current_matrix_list)):
        current_nested_list = current_matrix_list[current_nested_list_index]
        for current_nested_element_index in range(len(current_nested_list)):
            current_nested_element = current_nested_list[current_nested_element_index]
            if current_nested_element == current_char:
                return f"({current_nested_list_index}, {current_nested_element_index})"
            else:
                continue
    else:
        return f"{current_char} does not occur in the matrix"


matrix_list = creating_matrix_list_function()
char = input()
check_char_in_matrix = check_char_in_matrix_list_function(matrix_list, char)
print(check_char_in_matrix)


# size_of_a_square_matrix = int(input())
# matrix_list = []
# for nested_list_index in range(size_of_a_square_matrix):
#     nested_list = list(input())
#     matrix_list.append(nested_list)
# char = input()
# for nested_list_index in range(len(matrix_list)):
#     nested_list = matrix_list[nested_list_index]
#     for nested_element_index in range(len(nested_list)):
#         nested_element = nested_list[nested_element_index]
#         if nested_element == char:
#             print(f"({nested_list_index}, {nested_element_index})")
#             raise SystemExit
#         else:
#             continue
# else:
#     print(f"{char} does not occur in the matrix")


# matrix_list = [list(input()) for nested_list_index in range(int(input()))]
# char = input()
# for nested_list in matrix_list:
#     if char in nested_list:
#         list_index = matrix_list.index(nested_list)
#         element_index = nested_list.index(char)
#         print(f"({list_index}, {element_index})")
#         break
#     else:
#         continue
# else:
#     print(f"{char} does not occur in the matrix")
