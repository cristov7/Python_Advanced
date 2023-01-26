def create_matrix_list_function():
    current_info_list = list(map(int, input().split()))
    current_count_nested_lists = current_info_list[0]
    current_count_nested_elements = current_info_list[1]
    current_matrix_list = []
    for current_nested_list_index in range(current_count_nested_lists):
        current_nested_list = []
        for nested_element_index in range(current_nested_list_index, current_count_nested_elements + current_nested_list_index):
            current_first_letter = chr(current_nested_list_index + 97)
            current_second_letter = chr(nested_element_index + 97)
            current_third_letter = current_first_letter
            current_nested_element = current_first_letter + current_second_letter + current_third_letter
            current_nested_list.append(current_nested_element)
        current_matrix_list.append(current_nested_list)
    return current_matrix_list


matrix_list = create_matrix_list_function()
for nested_list in matrix_list:
    for nested_element in nested_list:
        print(nested_element, end=" ")
    print()


# info_list = list(map(int, input().split()))
# count_nested_lists = info_list[0]
# count_nested_elements = info_list[1]
# matrix_list = []
# for nested_list_index in range(count_nested_lists):
#     nested_list = []
#     for nested_element_index in range(nested_list_index, count_nested_elements + nested_list_index):
#         first_letter = chr(nested_list_index + 97)
#         second_letter = chr(nested_element_index + 97)
#         third_letter = first_letter
#         nested_element = first_letter + second_letter + third_letter
#         nested_list.append(nested_element)
#     matrix_list.append(nested_list)
# for nested_list in matrix_list:
#     for nested_element in nested_list:
#         print(nested_element, end=" ")
#     print()


# count_nested_lists, count_nested_elements = list(map(int, input().split()))
# start_end = ord("a")
# for nested_list_index in range(start_end, start_end + count_nested_lists):
#     for nested_element_index in range(start_end, start_end + count_nested_elements):
#         first_char = chr(nested_list_index)
#         second_char = chr(nested_list_index + nested_element_index - start_end)
#         third_char = first_char
#         print(f"{first_char}{second_char}{third_char}", end=" ")
#     print()
