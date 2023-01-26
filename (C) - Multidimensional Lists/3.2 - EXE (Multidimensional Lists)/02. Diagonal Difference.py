def create_matrix_list_function():
    current_matrix_list = []
    current_count_nested_list = int(input())
    for current_nested_list_index in range(current_count_nested_list):
        current_nested_list = list(map(int, input().split()))
        current_matrix_list.append(current_nested_list)
    return current_matrix_list


def return_primary_diagonal_list_function(current_matrix_list: list):
    current_primary_diagonal_list = []
    for current_nested_list_index in range(len(current_matrix_list)):
        current_nested_list = current_matrix_list[current_nested_list_index]
        current_nested_element = current_nested_list[current_nested_list_index]
        current_primary_diagonal_list.append(current_nested_element)
    return current_primary_diagonal_list


def return_secondary_diagonal_list_function(current_matrix_list: list):
    current_secondary_diagonal_list = []
    for current_nested_list_index in range(len(current_matrix_list)):
        current_nested_list = matrix_list[current_nested_list_index][::-1]
        # current_nested_list.reverse()
        current_nested_element = current_nested_list[current_nested_list_index]
        current_secondary_diagonal_list.append(current_nested_element)
    return current_secondary_diagonal_list


def return_diagonal_difference_function(current_primary_diagonal_list: list, current_secondary_diagonal_list: list):
    current_primary_diagonal_sum = sum(current_primary_diagonal_list)
    current_secondary_diagonal_sum = sum(current_secondary_diagonal_list)
    current_diagonal_difference_abs = abs(current_primary_diagonal_sum - current_secondary_diagonal_sum)
    return current_diagonal_difference_abs


matrix_list = create_matrix_list_function()
primary_diagonal_list = return_primary_diagonal_list_function(matrix_list)
secondary_diagonal_list = return_secondary_diagonal_list_function(matrix_list)
diagonal_difference_abs = return_diagonal_difference_function(primary_diagonal_list, secondary_diagonal_list)
print(diagonal_difference_abs)


# count_nested_list = int(input())
# matrix_list = []
# for nested_list_index in range(count_nested_list):
#     nested_list = list(map(int, input().split()))
#     matrix_list.append(nested_list)
# primary_diagonal_list = []
# for nested_list_index in range(len(matrix_list)):
#     nested_list = matrix_list[nested_list_index]
#     nested_element = nested_list[nested_list_index]
#     primary_diagonal_list.append(nested_element)
# secondary_diagonal_list = []
# for nested_list_index in range(len(matrix_list)):
#     nested_list = matrix_list[nested_list_index][::-1]
#     # nested_list.reverse()
#     nested_element = nested_list[nested_list_index]
#     secondary_diagonal_list.append(nested_element)
# first_diagonal_sum = sum(primary_diagonal_list)
# second_diagonal_sum = sum(secondary_diagonal_list)
# diagonal_difference_abs = abs(first_diagonal_sum - second_diagonal_sum)
# print(diagonal_difference_abs)


# matrix_list = [list(map(int, input().split())) for nested_list_index in range(int(input()))]
# first_diagonal_list = [matrix_list[index][index] for index in range(len(matrix_list))]
# second_diagonal_list = [matrix_list[index][::-1][index] for index in range(len(matrix_list))]
# first_diagonal_sum = sum(first_diagonal_list)
# second_diagonal_sum = sum(second_diagonal_list)
# diagonal_difference_abs = abs(first_diagonal_sum - second_diagonal_sum)
# print(diagonal_difference_abs)
