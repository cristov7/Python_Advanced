def calculating_function(current_matrix_list: list, current_count_nested_lists: int, current_count_nested_elements: int):
    current_max_calculating_matrix_list = []
    current_max_calculating = 0
    for nested_list_index in range(current_count_nested_lists - 1):
        for nested_element_index in range(current_count_nested_elements - 1):
            first_nested_element = current_matrix_list[nested_list_index][nested_element_index]
            second_nested_element = current_matrix_list[nested_list_index][nested_element_index + 1]
            third_nested_element = current_matrix_list[nested_list_index + 1][nested_element_index]
            fourth_nested_element = current_matrix_list[nested_list_index + 1][nested_element_index + 1]
            calculating = first_nested_element + second_nested_element + third_nested_element + fourth_nested_element
            if calculating > current_max_calculating:
                current_max_calculating = calculating
                current_first_nested_list = [first_nested_element, second_nested_element]
                current_second_nested_list = [third_nested_element, fourth_nested_element]
                current_max_calculating_matrix_list = [current_first_nested_list, current_second_nested_list]
            else:
                continue
    return current_max_calculating_matrix_list, current_max_calculating


count_nested_lists, count_nested_elements = map(int, input().split(", "))
matrix_list = [list(map(int, input().split(", "))) for nested_list_index in range(count_nested_lists)]
calculating_matrix_list, max_calculating = calculating_function(matrix_list, count_nested_lists, count_nested_elements)
[print(f"{nested_list[0]} {nested_list[1]}") for nested_list in calculating_matrix_list]
print(max_calculating)


# count_nested_lists, count_nested_elements = list(map(int, input().split(", ")))
# matrix_list = []
# for nested_list_index in range(count_nested_lists):
#     nested_list = list(map(int, input().split(", ")))
#     matrix_list.append(nested_list)
# biggest_matrix_list_sum = 0
# biggest_2_x_2_matrix_list = []
# for nested_list_index in range(0, count_nested_lists - 1):
#     for nested_element_index in range(0, count_nested_elements - 1):
#         first_nested_element = matrix_list[nested_list_index][nested_element_index]
#         second_nested_element = matrix_list[nested_list_index][nested_element_index + 1]
#         third_nested_element = matrix_list[nested_list_index + 1][nested_element_index]
#         fourth_nested_element = matrix_list[nested_list_index + 1][nested_element_index + 1]
#         matrix_list_sum = first_nested_element + second_nested_element + third_nested_element + fourth_nested_element
#         if matrix_list_sum > biggest_matrix_list_sum:
#             biggest_matrix_list_sum = matrix_list_sum
#             first_nested_list = [first_nested_element, second_nested_element]
#             second_nested_list = [third_nested_element, fourth_nested_element]
#             biggest_2_x_2_matrix_list = [first_nested_list, second_nested_list]
#         else:
#             continue
# for nested_list in biggest_2_x_2_matrix_list:
#     print(*nested_list)
# print(biggest_matrix_list_sum)


# size_of_matrix_list = list(map(int, input().split(", ")))
# count_nested_lists = size_of_matrix_list[0]
# count_nested_elements = size_of_matrix_list[1]
# matrix_list = []
# for nested_list_index in range(count_nested_lists):
#     nested_list = list(map(int, input().split(", ")))
#     matrix_list.append(nested_list)
# max_calculating = 0
# max_calculating_matrix_list = []
# for nested_list_index in range(count_nested_lists - 1):
#     for nested_element_index in range(count_nested_elements - 1):
#         first_nested_element = matrix_list[nested_list_index][nested_element_index]
#         second_nested_element = matrix_list[nested_list_index][nested_element_index + 1]
#         third_nested_element = matrix_list[nested_list_index + 1][nested_element_index]
#         fourth_nested_element = matrix_list[nested_list_index + 1][nested_element_index + 1]
#         calculating = first_nested_element + second_nested_element + third_nested_element + fourth_nested_element
#         if calculating > max_calculating:
#             max_calculating = calculating
#             first_nested_list = [first_nested_element, second_nested_element]
#             second_nested_list = [third_nested_element, fourth_nested_element]
#             max_calculating_matrix_list = [first_nested_list, second_nested_list]
#         else:
#             continue
# for nested_list in max_calculating_matrix_list:
#     first_nested_element = nested_list[0]
#     second_nested_element = nested_list[1]
#     print(f"{first_nested_element} {second_nested_element}")
# print(max_calculating)

# max_calculating_matrix_list = []
# for nested_list_index in range(count_nested_lists - 1):
#     for nested_element_index in range(count_nested_elements - 1):
#         first_nested_element = matrix_list[nested_list_index][nested_element_index]
#         second_nested_element = matrix_list[nested_list_index][nested_element_index + 1]
#         third_nested_element = matrix_list[nested_list_index + 1][nested_element_index]
#         fourth_nested_element = matrix_list[nested_list_index + 1][nested_element_index + 1]
#         calculating = first_nested_element + second_nested_element + third_nested_element + fourth_nested_element
#         if calculating > max_calculating:
#             max_calculating = calculating
#             first_nested_list = [first_nested_element, second_nested_element]
#             second_nested_list = [third_nested_element, fourth_nested_element]
#             max_calculating_matrix_list = [first_nested_list, second_nested_list]
#         else:
#             continue
# for nested_list in max_calculating_matrix_list:
#     first_nested_element = nested_list[0]
#     second_nested_element = nested_list[1]
#     print(f"{first_nested_element} {second_nested_element}")
# print(max_calculating)
