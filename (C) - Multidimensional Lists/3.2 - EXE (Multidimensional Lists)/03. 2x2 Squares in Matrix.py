def create_matrix_list_function():
    current_matrix_list = []
    current_info_list = list(map(int, input().split()))
    current_count_nested_lists = current_info_list[0]
    # current_count_nested_elements = current_info_list[1]
    for current_nested_list_index in range(current_count_nested_lists):
        current_nested_list = list(map(int, input().split()))
        current_matrix_list.append(current_nested_list)
    return current_matrix_list


def return_count_square_matrices_function(current_matrix_list: list):
    current_count_square_matrices = 0
    for nested_list_index in range(len(current_matrix_list) - 1):
        nested_list = current_matrix_list[nested_list_index]
        for nested_element_index in range(len(nested_list) - 1):
            nested_element = current_matrix_list[nested_list_index][nested_element_index]
            second_nested_element = current_matrix_list[nested_list_index][nested_element_index + 1]
            third_nested_element = current_matrix_list[nested_list_index + 1][nested_element_index]
            fourth_nested_element = current_matrix_list[nested_list_index + 1][nested_element_index + 1]
            if nested_element == second_nested_element == third_nested_element == fourth_nested_element:
                current_count_square_matrices += 1
            else:
                continue
    return current_count_square_matrices


matrix_list = create_matrix_list_function()
count_square_matrices = return_count_square_matrices_function(matrix_list)
print(count_square_matrices)


# info_list = list(map(int, input().split()))
# count_nested_lists = info_list[0]
# count_nested_elements = info_list[1]
# matrix_list = []
# for nested_list_index in range(count_nested_lists):
#     nested_list = input().split()
#     matrix_list.append(nested_list)
# count_square_matrices = 0
# for nested_list_index in range(len(matrix_list) - 1):
#     nested_list = matrix_list[nested_list_index]
#     for nested_element_index in range(len(nested_list) - 1):
#         nested_element = matrix_list[nested_list_index][nested_element_index]
#         second_nested_element = matrix_list[nested_list_index][nested_element_index + 1]
#         third_nested_element = matrix_list[nested_list_index + 1][nested_element_index]
#         fourth_nested_element = matrix_list[nested_list_index + 1][nested_element_index + 1]
#         if nested_element == second_nested_element == third_nested_element == fourth_nested_element:
#             count_square_matrices += 1
#         else:
#             continue
# print(count_square_matrices)


# count_nested_lists, count_nested_elements = list(map(int, input().split()))
# matrix_list = [input().split() for nested_list_index in range(count_nested_lists)]
# count_square_matrices_list = [matrix_list[nested_list_index][nested_element_index] for nested_list_index in range(len(matrix_list) - 1) for nested_element_index in range(len(matrix_list[nested_list_index]) - 1) if matrix_list[nested_list_index][nested_element_index] == matrix_list[nested_list_index][nested_element_index + 1] == matrix_list[nested_list_index + 1][nested_element_index] == matrix_list[nested_list_index + 1][nested_element_index + 1]]
# print(len(count_square_matrices_list))
