def create_matrix_list_function():
    current_matrix_list = []
    current_info_list = list(map(int, input().split()))
    current_count_nested_lists = current_info_list[0]
    current_count_nested_elements = current_info_list[1]
    for current_nested_list_index in range(current_count_nested_lists):
        current_nested_list = input().split()
        if len(current_nested_list) == current_count_nested_elements:
            current_matrix_list.append(current_nested_list)
        else:
            continue
    return current_matrix_list


def print_commands_function(current_matrix_list: list):
    while True:
        command = input()
        if command == "END":
            raise SystemExit
        else:
            if command.startswith("swap "):
                command_list = [int(element) for element in command.split() if element.isdigit()]
                if len(command_list) == 4:
                    first_nested_list_index = command_list[0]
                    first_nested_element_index = command_list[1]
                    second_nested_list_index = command_list[2]
                    second_nested_element_index = command_list[3]
                    if first_nested_list_index < len(current_matrix_list) \
                            and second_nested_list_index < len(current_matrix_list):
                        if first_nested_element_index < len(current_matrix_list[first_nested_list_index]) \
                                and second_nested_element_index < len(current_matrix_list[second_nested_list_index]):
                            # first_nested_element = current_matrix_list[first_nested_list_index][first_nested_element_index]
                            # second_nested_element = current_matrix_list[second_nested_list_index][second_nested_element_index]
                            current_matrix_list[first_nested_list_index][first_nested_element_index], \
                            current_matrix_list[second_nested_list_index][second_nested_element_index] = \
                                current_matrix_list[second_nested_list_index][second_nested_element_index], \
                                current_matrix_list[first_nested_list_index][first_nested_element_index]
                            for nested_list in current_matrix_list:
                                for nested_element in nested_list:
                                    print(nested_element, end=" ")
                                print()
                        else:
                            print("Invalid input!")
                    else:
                        print("Invalid input!")
                else:
                    print("Invalid input!")
            else:
                print("Invalid input!")


matrix_list = create_matrix_list_function()
print_commands = print_commands_function(matrix_list)


# info_list = list(map(int, input().split()))
# count_nested_lists = info_list[0]
# count_nested_elements = info_list[1]
# matrix_list = []
# for nested_list_index in range(count_nested_lists):
#     nested_list = input().split()
#     if len(nested_list) == count_nested_elements:
#         matrix_list.append(nested_list)
#     else:
#         continue
# COMMAND_END = "END"
# while True:
#     command = input()
#     if command == COMMAND_END:
#         break
#     else:
#         if command.startswith("swap "):
#             command_list = [int(element) for element in command.split() if element.isdigit()]
#             if len(command_list) == 4:
#                 first_nested_list_index = command_list[0]
#                 first_nested_element_index = command_list[1]
#                 second_nested_list_index = command_list[2]
#                 second_nested_element_index = command_list[3]
#                 if first_nested_list_index < len(matrix_list) and second_nested_list_index < len(matrix_list):
#                     if first_nested_element_index < len(matrix_list[first_nested_list_index]) and second_nested_element_index < len(matrix_list[second_nested_list_index]):
#                         # first_nested_element = matrix_list[first_nested_list_index][first_nested_element_index]
#                         # second_nested_element = matrix_list[second_nested_list_index][second_nested_element_index]
#                         matrix_list[first_nested_list_index][first_nested_element_index], matrix_list[second_nested_list_index][second_nested_element_index] = matrix_list[second_nested_list_index][second_nested_element_index], matrix_list[first_nested_list_index][first_nested_element_index]
#                         for nested_list in matrix_list:
#                             for nested_element in nested_list:
#                                 print(nested_element, end=" ")
#                             print()
#                     else:
#                         print("Invalid input!")
#                 else:
#                     print("Invalid input!")
#             else:
#                 print("Invalid input!")
#         else:
#             print("Invalid input!")
