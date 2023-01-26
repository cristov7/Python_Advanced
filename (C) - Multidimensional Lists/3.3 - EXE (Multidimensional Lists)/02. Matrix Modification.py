def create_matrix_list_function():
    current_count_nested_lists = int(input())
    current_matrix_list = []
    for current_nested_list_index in range(current_count_nested_lists):
        current_nested_list = list(map(int, input().split()))
        current_matrix_list.append(current_nested_list)
    return current_matrix_list


def return_modification_matrix_list_function(current_matrix_list: list):
    while True:
        command = input()
        if command == "END":
            break
        else:
            command_list = command.split()
            info = command_list[0]
            nested_list_index = int(command_list[1])
            nested_element_index = int(command_list[2])
            value = int(command_list[3])
            if info == "Add":
                if 0 <= nested_list_index < len(current_matrix_list) and \
                        0 <= nested_element_index <= len(current_matrix_list[nested_list_index]):
                    nested_element = current_matrix_list[nested_list_index][nested_element_index]
                    update_nested_element = nested_element + value
                    current_matrix_list[nested_list_index][nested_element_index] = update_nested_element
                else:
                    print("Invalid coordinates")
            elif info == "Subtract":
                if 0 <= nested_list_index < len(current_matrix_list) and \
                        0 <= nested_element_index <= len(
                        current_matrix_list[nested_list_index]):
                    nested_element = current_matrix_list[nested_list_index][nested_element_index]
                    update_nested_element = nested_element - value
                    current_matrix_list[nested_list_index][nested_element_index] = update_nested_element
                else:
                    print("Invalid coordinates")
            else:
                print("Invalid coordinates")
    return current_matrix_list


matrix_list = create_matrix_list_function()
print_commands = return_modification_matrix_list_function(matrix_list)
for nested_list in matrix_list:
    print(*nested_list)


# count_nested_lists = int(input())
# matrix_list = []
# for nested_list_index in range(count_nested_lists):
#     nested_list = list(map(int, input().split()))
#     matrix_list.append(nested_list)
# COMMAND_END = "END"
# while True:
#     command = input()
#     if command == COMMAND_END:
#         break
#     else:
#         command_list = command.split()
#         info = command_list[0]
#         nested_list_index = int(command_list[1])
#         nested_element_index = int(command_list[2])
#         value = int(command_list[3])
#         if info == "Add":
#             if 0 <= nested_list_index < len(matrix_list) and \
#                     0 <= nested_element_index <= len(matrix_list[nested_list_index]):
#                 nested_element = matrix_list[nested_list_index][nested_element_index]
#                 update_nested_element = nested_element + value
#                 matrix_list[nested_list_index][nested_element_index] = update_nested_element
#             else:
#                 print("Invalid coordinates")
#         elif info == "Subtract":
#             if 0 <= nested_list_index < len(matrix_list) and \
#                     0 <= nested_element_index <= len(matrix_list[nested_list_index]):
#                 nested_element = matrix_list[nested_list_index][nested_element_index]
#                 update_nested_element = nested_element - value
#                 matrix_list[nested_list_index][nested_element_index] = update_nested_element
#             else:
#                 print("Invalid coordinates")
#         else:
#             print("Invalid coordinates")
# for nested_list in matrix_list:
#     print(*nested_list)
