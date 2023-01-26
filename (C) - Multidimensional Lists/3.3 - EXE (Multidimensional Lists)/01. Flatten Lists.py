def return_flatten_list_function():
    current_info = input()
    current_info_list = current_info.split("|")
    current_flatten_list = []
    for current_element in current_info_list:
        current_element_list = list(map(int, current_element.split()))
        current_flatten_list.append(current_element_list)
    current_flatten_list.reverse()
    return current_flatten_list


flatten_list = return_flatten_list_function()
for nested_list in flatten_list:
    for nested_element in nested_list:
        print(nested_element, end=" ")


# info = input()
# info_list = info.split("|")
# flatten_list = []
# for element in info_list:
#     element_list = list(map(int, element.split()))
#     flatten_list.append(element_list)
# flatten_list.reverse()
# for nested_list in flatten_list:
#     for nested_element in nested_list:
#         print(nested_element, end=" ")


# flatten_list = [list(map(int, nested_element.split())) for nested_element in input().split("|")][::-1]
# [print(nested_element, end=" ") for nested_list in flatten_list for nested_element in nested_list]
