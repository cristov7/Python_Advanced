def creating_matrix_list_function():
    count_nested_lists = int(input())
    current_matrix_list = []
    for current_nested_list_index in range(count_nested_lists):
        current_nested_list = list(map(int, input().split(", ")))
        current_matrix_list.append(current_nested_list)
    return current_matrix_list


def return_even_matrix_list_function(current_matrix_list: list):
    current_even_matrix_list = []
    for current_nested_list in current_matrix_list:
        current_nested_even_list = []
        for current_nested_element in current_nested_list:
            if current_nested_element % 2 == 0:
                current_nested_even_list.append(current_nested_element)
            else:
                continue
        current_even_matrix_list.append(current_nested_even_list)
    return current_even_matrix_list


matrix_list = creating_matrix_list_function()
even_matrix_list = return_even_matrix_list_function(matrix_list)
print(even_matrix_list)


# count_nested_lists = int(input())
# matrix_list = []
# for nested_list_index in range(count_nested_lists):
#     nested_list = list(map(int, input().split(", ")))
#     matrix_list.append(nested_list)
# even_matrix_list = []
# for nested_list in matrix_list:
#     nested_even_list = []
#     for nested_element in nested_list:
#         if nested_element % 2 == 0:
#             nested_even_list.append(nested_element)
#         else:
#             continue
#     even_matrix_list.append(nested_even_list)
# print(even_matrix_list)


# matrix_list = [list(map(int, input().split(", "))) for nested_list_index in range(int(input()))]
# even_matrix_list = [[nested_number for nested_number in nested_list if nested_number % 2 == 0] for nested_list in matrix_list]
# print(even_matrix_list)


# print([[nested_number for nested_number in list(map(int, input().split(", "))) if nested_number % 2 == 0] for nested_list_index in range(int(input()))])
