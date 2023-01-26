def create_matrix_list_function():
    current_matrix_list = []
    current_count_nested_lists = int(input())
    for current_nested_list_index in range(current_count_nested_lists):
        current_nested_list = list(map(int, input().split(", ")))
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


matrix_list = create_matrix_list_function()
primary_diagonal_list = return_primary_diagonal_list_function(matrix_list)
secondary_diagonal_list = return_secondary_diagonal_list_function(matrix_list)
primary_diagonal_sum = sum(primary_diagonal_list)
secondary_diagonal_sum = sum(secondary_diagonal_list)
print(f"Primary diagonal: {', '.join(str(element) for element in primary_diagonal_list)}. Sum: {primary_diagonal_sum}")
print(f"Secondary diagonal: {', '.join(str(element) for element in secondary_diagonal_list)}. Sum: {secondary_diagonal_sum}")


# count_nested_lists = int(input())
# matrix_list = []
# for nested_list_index in range(count_nested_lists):
#     nested_list = list(map(int, input().split(", ")))
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
# converting_primary_diagonal = [str(element) for element in primary_diagonal_list]
# converting_secondary_diagonal = [str(element) for element in secondary_diagonal_list]
# first_diagonal_sum = sum(primary_diagonal_list)
# second_diagonal_sum = sum(secondary_diagonal_list)
# print(f"Primary diagonal: {', '.join(converting_primary_diagonal)}. Sum: {first_diagonal_sum}")
# print(f"Secondary diagonal: {', '.join(converting_secondary_diagonal)}. Sum: {second_diagonal_sum}")


# matrix_list = [list(map(int, input().split(", "))) for nested_list_index in range(int(input()))]
# primary_diagonal_list = [matrix_list[index][index] for index in range(len(matrix_list))]
# secondary_diagonal_list = [matrix_list[index][::-1][index] for index in range(len(matrix_list))]
# converting_primary_diagonal = [str(element) for element in primary_diagonal_list]
# converting_secondary_diagonal = [str(element) for element in secondary_diagonal_list]
# first_diagonal_sum = sum(primary_diagonal_list)
# second_diagonal_sum = sum(secondary_diagonal_list)
# print(f"Primary diagonal: {', '.join(converting_primary_diagonal)}. Sum: {first_diagonal_sum}")
# print(f"Secondary diagonal: {', '.join(converting_secondary_diagonal)}. Sum: {second_diagonal_sum}")
