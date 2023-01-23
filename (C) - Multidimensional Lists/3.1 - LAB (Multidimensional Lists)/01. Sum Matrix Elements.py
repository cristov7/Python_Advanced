def creating_matrix_function(current_nested_lists: int, current_nested_elements: int):
    current_matrix_list = []
    for nested_list_index in range(current_nested_lists):
        nested_elements_list = list(map(int, input().split(", ")))
        if len(nested_elements_list) == current_nested_elements:
            current_matrix_list.append(nested_elements_list)
        else:
            raise SystemExit
    return current_matrix_list


def sum_matrix_list_function(current_matrix_list: list):
    current_matrix_sum = 0
    for nested_list in current_matrix_list:
        nested_list_sum = sum(nested_list)
        current_matrix_sum += nested_list_sum
    return current_matrix_sum


info_list = input().split(", ")
count_nested_lists, count_nested_elements = map(int, info_list)
matrix_list = creating_matrix_function(count_nested_lists, count_nested_elements)
matrix_sum = sum_matrix_list_function(matrix_list)
print(matrix_sum)
print(matrix_list)


# info_list = list(map(int, input().split(", ")))
# count_nested_lists = info_list[0]
# count_nested_elements = info_list[1]
# matrix_sum = 0
# matrix_list = []
# for nested_list_index in range(count_nested_lists):
#     matrix_list.append([])
#     nested_elements_list = list(map(int, input().split(", ")))
#     for nested_element_index in range(count_nested_elements):
#         nested_element = nested_elements_list[nested_element_index]
#         matrix_sum += nested_element
#         matrix_list[nested_list_index].append(nested_element)
# print(matrix_sum)
# print(matrix_list)


# info_list = list(map(int, input().split(", ")))
# count_nested_lists = info_list[0]
# count_nested_elements = info_list[1]
# matrix_sum = 0
# matrix_list = []
# for nested_list_index in range(count_nested_lists):
#     nested_elements_list = list(map(int, input().split(", ")))
#     if len(nested_elements_list) == count_nested_elements:
#         matrix_sum += sum(nested_elements_list)
#         matrix_list.append(nested_elements_list)
#     else:
#         raise SystemExit
# print(matrix_sum)
# print(matrix_list)


# info_list = list(map(int, input().split(", ")))
# matrix_list = [list(map(int, input().split(", "))) for nested_list_index in range(info_list[0])]
# matrix_sum = sum([sum(nested_list) for nested_list in matrix_list])
# print(matrix_sum)
# print(matrix_list)
