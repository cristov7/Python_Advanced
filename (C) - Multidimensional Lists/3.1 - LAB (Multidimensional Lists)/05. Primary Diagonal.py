def creating_matrix_list_function():
    size_of_a_square_matrix = int(input())
    current_matrix_list = []
    for current_nested_list_index in range(size_of_a_square_matrix):
        current_nested_list = list(map(int, input().split()))
        current_matrix_list.append(current_nested_list)
    return current_matrix_list


def return_calculating_matrix_diagonal_function(current_matrix_list: list):
    current_sum_primary_diagonal = 0
    for current_nested_list_index in range(len(current_matrix_list)):
        current_nested_list = current_matrix_list[current_nested_list_index]
        current_nested_element = current_nested_list[current_nested_list_index]
        current_sum_primary_diagonal += current_nested_element
    return current_sum_primary_diagonal


matrix_list = creating_matrix_list_function()
sum_primary_diagonal = return_calculating_matrix_diagonal_function(matrix_list)
print(sum_primary_diagonal)


# size_of_a_square_matrix = int(input())
# matrix_list = []
# for nested_list_index in range(size_of_a_square_matrix):
#     nested_list = list(map(int, input().split()))
#     matrix_list.append(nested_list)
# sum_primary_diagonal = 0
# for nested_list_index in range(len(matrix_list)):
#     nested_list = matrix_list[nested_list_index]
#     nested_element = nested_list[nested_list_index]
#     sum_primary_diagonal += nested_element
# print(sum_primary_diagonal)


# matrix_list = [list(map(int, input().split())) for index_nested_lists in range(int(input()))]
# sum_primary_diagonal = sum([matrix_list[nested_list_index][nested_list_index] for nested_list_index in range(len(matrix_list))])
# print(sum_primary_diagonal)
