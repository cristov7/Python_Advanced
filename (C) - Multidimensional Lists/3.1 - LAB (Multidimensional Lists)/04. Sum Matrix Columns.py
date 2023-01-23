def creating_matrix_list_function(current_count_nested_lists: int):
    current_matrix_list = []
    for current_nested_list_index in range(current_count_nested_lists):
        current_nested_list = list(map(int, input().split()))
        current_matrix_list.append(current_nested_list)
    return current_matrix_list


def return_sorting_list_function(current_matrix_list: list, current_count_nested_elements: int):
    current_sorting_list = []
    for current_nested_list_index in range(current_count_nested_elements):
        current_sorted_list = [current_nested_list[current_nested_list_index] for current_nested_list in current_matrix_list]
        current_sorting_list.append(current_sorted_list)
    return current_sorting_list


def return_calculating_list_function(current_sorting_list: list):
    current_calculating_list = []
    for current_sorting_nested_list in current_sorting_list:
        current_calculation = sum(current_sorting_nested_list)
        current_calculating_list.append(current_calculation)
    return current_calculating_list


info_list = list(map(int, input().split(", ")))
count_nested_lists = info_list[0]
count_nested_elements = info_list[1]
matrix_list = creating_matrix_list_function(count_nested_lists)
sorting_list = return_sorting_list_function(matrix_list, count_nested_elements)
calculating_list = return_calculating_list_function(sorting_list)
print(*calculating_list, sep="\n")


# info_list = list(map(int, input().split(", ")))
# count_nested_lists = info_list[0]
# count_nested_elements = info_list[1]
# matrix_list = []
# for nested_list_index in range(count_nested_lists):
#     nested_list = list(map(int, input().split()))
#     matrix_list.append(nested_list)
# sorting_list = []
# for nested_list_index in range(count_nested_elements):
#     sorted_list = [nested_list[nested_list_index] for nested_list in matrix_list]
#     sorting_list.append(sorted_list)
# calculating_list = []
# for sorting_nested_list in sorting_list:
#     calculation = sum(sorting_nested_list)
#     calculating_list.append(calculation)
# print(*calculating_list, sep="\n")


# info_list = list(map(int, input().split(", ")))
# count_nested_lists = info_list[0]
# count_nested_elements = info_list[1]
# matrix_list = [list(map(int, input().split())) for nested_list_index in range(count_nested_lists)]
# sorting_list = [[nested_list[nested_element_index] for nested_list in matrix_list] for nested_element_index in range(count_nested_elements)]
# calculating_list = [(sum(nested_list)) for nested_list in sorting_list]
# print(*calculating_list, sep="\n")
