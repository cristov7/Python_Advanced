def creating_matrix_list_function():
    count_nested_lists = int(input())
    current_matrix_list = []
    for current_nested_list_index in range(count_nested_lists):
        current_nested_list = list(map(int, input().split(", ")))
        current_matrix_list.append(current_nested_list)
    return current_matrix_list


def return_flattering_list_function(current_matrix_list: list):
    current_flattering_list = []
    for current_nested_list in current_matrix_list:
        for current_nested_element in current_nested_list:
            current_flattering_list.append(current_nested_element)
    return current_flattering_list


matrix_list = creating_matrix_list_function()
flattering_list = return_flattering_list_function(matrix_list)
print(flattering_list)


# count_lists = int(input())
# flattering_list = []
# for numbers_list_index in range(count_lists):
#     numbers_list = list(map(int, input().split(", ")))
#     flattering_list.extend(numbers_list)
# print(flattering_list)


# matrix_list = [list(map(int, input().split(", "))) for numbers_list_index in range(int(input()))]
# flattering_list = [nested_element for nested_list in matrix_list for nested_element in nested_list]
# print(flattering_list)
