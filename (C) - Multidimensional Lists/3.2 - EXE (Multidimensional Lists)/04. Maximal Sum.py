def create_matrix_list_function():
    current_matrix_list = []
    current_info_list = list(map(int, input().split()))
    current_count_nested_lists = current_info_list[0]
    # current_count_nested_elements = current_info_list[1]
    for current_nested_list_index in range(current_count_nested_lists):
        current_nested_list = list(map(int, input().split()))
        current_matrix_list.append(current_nested_list)
    return current_matrix_list


def return_max_sum_and_max_matrix_list_function(current_matrix_list: list):
    maximum_sum = 0
    maximum_nested_elements_list = []
    for nested_list_index in range(len(current_matrix_list) - 2):
        nested_list = current_matrix_list[nested_list_index]
        for nested_element_index in range(len(nested_list) - 2):
            nested_element = current_matrix_list[nested_list_index][nested_element_index]
            second_nested_element = current_matrix_list[nested_list_index][nested_element_index + 1]
            third_nested_element = current_matrix_list[nested_list_index][nested_element_index + 2]
            # first_nested_list = current_matrix_list[nested_list_index][nested_element_index: nested_element_index + 3]
            fourth_nested_element = current_matrix_list[nested_list_index + 1][nested_element_index]
            fifth_nested_element = current_matrix_list[nested_list_index + 1][nested_element_index + 1]
            sixth_nested_element = current_matrix_list[nested_list_index + 1][nested_element_index + 2]
            # second_nested_list = current_matrix_list[nested_list_index + 1][nested_element_index: nested_element_index + 3]
            seventh_nested_element = current_matrix_list[nested_list_index + 2][nested_element_index]
            eighth_nested_element = current_matrix_list[nested_list_index + 2][nested_element_index + 1]
            ninth_nested_element = current_matrix_list[nested_list_index + 2][nested_element_index + 2]
            # third_nested_list = current_matrix_list[nested_list_index + 2][nested_element_index: nested_element_index + 3]
            first_3_nested_elements_sum = nested_element + second_nested_element + third_nested_element
            second_3_nested_elements_sum = fourth_nested_element + fifth_nested_element + sixth_nested_element
            third_3_nested_elements_sum = seventh_nested_element + eighth_nested_element + ninth_nested_element
            nested_elements_sum = first_3_nested_elements_sum + second_3_nested_elements_sum + third_3_nested_elements_sum
            # nested_elements_sum = sum(first_nested_list) + sum(second_nested_list) + sum(third_nested_list)
            if nested_elements_sum >= maximum_sum:
                maximum_sum = nested_elements_sum
                first_nested_list = [nested_element, second_nested_element, third_nested_element]
                second_nested_list = [fourth_nested_element, fifth_nested_element, sixth_nested_element]
                third_nested_list = [seventh_nested_element, eighth_nested_element, ninth_nested_element]
                maximum_nested_elements_list = [first_nested_list, second_nested_list, third_nested_list]
            else:
                continue
    return maximum_sum, maximum_nested_elements_list


matrix_list = create_matrix_list_function()
current_maximum_sum, current_maximum_nested_elements_list = return_max_sum_and_max_matrix_list_function(matrix_list)
print(f"Sum = {current_maximum_sum}")
for current_nested_list in current_maximum_nested_elements_list:
    current_first_nested_element = current_nested_list[0]
    current_second_nested_element = current_nested_list[1]
    current_third_nested_element = current_nested_list[2]
    print(f"{current_first_nested_element} {current_second_nested_element} {current_third_nested_element}")


# info_list = list(map(int, input().split()))
# count_nested_lists = info_list[0]
# count_nested_elements = info_list[1]
# matrix_list = []
# for nested_list_index in range(count_nested_lists):
#     nested_list = list(map(int, input().split()))
#     matrix_list.append(nested_list)
# maximum_sum = 0
# maximum_nested_elements_list = []
# for nested_list_index in range(len(matrix_list) - 2):
#     nested_list = matrix_list[nested_list_index]
#     for nested_element_index in range(len(nested_list) - 2):
#         nested_element = matrix_list[nested_list_index][nested_element_index]
#         second_nested_element = matrix_list[nested_list_index][nested_element_index + 1]
#         third_nested_element = matrix_list[nested_list_index][nested_element_index + 2]
#         fourth_nested_element = matrix_list[nested_list_index + 1][nested_element_index]
#         fifth_nested_element = matrix_list[nested_list_index + 1][nested_element_index + 1]
#         sixth_nested_element = matrix_list[nested_list_index + 1][nested_element_index + 2]
#         seventh_nested_element = matrix_list[nested_list_index + 2][nested_element_index]
#         eighth_nested_element = matrix_list[nested_list_index + 2][nested_element_index + 1]
#         ninth_nested_element = matrix_list[nested_list_index + 2][nested_element_index + 2]
#         first_3_nested_elements_sum = nested_element + second_nested_element + third_nested_element
#         second_3_nested_elements_sum = fourth_nested_element + fifth_nested_element + sixth_nested_element
#         third_3_nested_elements_sum = seventh_nested_element + eighth_nested_element + ninth_nested_element
#         nested_elements_sum = first_3_nested_elements_sum + second_3_nested_elements_sum + third_3_nested_elements_sum
#         if nested_elements_sum >= maximum_sum:
#             maximum_sum = nested_elements_sum
#             first_nested_list = [nested_element, second_nested_element, third_nested_element]
#             second_nested_list = [fourth_nested_element, fifth_nested_element, sixth_nested_element]
#             third_nested_list = [seventh_nested_element, eighth_nested_element, ninth_nested_element]
#             maximum_nested_elements_list = [first_nested_list, second_nested_list, third_nested_list]
#         else:
#             continue
# print(f"Sum = {maximum_sum}")
# for nested_list in maximum_nested_elements_list:
#     first_nested_element = nested_list[0]
#     second_nested_element = nested_list[1]
#     third_nested_element = nested_list[2]
#     print(f"{first_nested_element} {second_nested_element} {third_nested_element}")


# matrix_list = [list(map(int, input().split())) for nested_list_index in range(list(map(int, input().split()))[0])]
# maximum_sum = 0
# maximum_nested_elements_list = []
# for nested_list_index in range(len(matrix_list) - 2):
#     for nested_element_index in range(len(matrix_list[nested_list_index]) - 2):
#         first_nested_list = matrix_list[nested_list_index][nested_element_index: nested_element_index + 3]
#         second_nested_list = matrix_list[nested_list_index + 1][nested_element_index: nested_element_index + 3]
#         third_nested_list = matrix_list[nested_list_index + 2][nested_element_index: nested_element_index + 3]
#         nested_elements_sum = sum(first_nested_list) + sum(second_nested_list) + sum(third_nested_list)
#         if nested_elements_sum >= maximum_sum:
#             maximum_sum = nested_elements_sum
#             maximum_nested_elements_list = [first_nested_list, second_nested_list, third_nested_list]
#         else:
#             continue
# print(f"Sum = {maximum_sum}")
# [print(f"{nested_list[0]} {nested_list[1]} {nested_list[2]}") for nested_list in maximum_nested_elements_list]
