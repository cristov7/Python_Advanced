first_numbers_set = set(map(int, input().split()))
second_numbers_set = set(map(int, input().split()))
count_commands = int(input())
COMMAND_ADD_FIRST = "Add First "
COMMAND_ADD_SECOND = "Add Second "
COMMAND_REMOVE_FIRST = "Remove First "
COMMAND_REMOVE_SECOND = "Remove Second "
COMMAND_CHECK_SUBSET = "Check Subset"
for command in range(1, count_commands + 1):
    current_command = input()
    if current_command.startswith(COMMAND_ADD_FIRST):
        current_command_list = current_command.split()
        numbers_set = {int(element) for element in current_command_list if element.isdigit()}
        first_numbers_set.update(numbers_set)
        # for number in numbers_set:
        #     first_numbers_set.add(number)
    elif current_command.startswith(COMMAND_ADD_SECOND):
        current_command_list = current_command.split()
        numbers_set = {int(element) for element in current_command_list if element.isdigit()}
        second_numbers_set.update(numbers_set)
        # for number in numbers_set:
        #     second_numbers_set.add(number)
    elif current_command.startswith(COMMAND_REMOVE_FIRST):
        current_command_list = current_command.split()
        numbers_set = {int(element) for element in current_command_list if element.isdigit()}
        first_numbers_set = first_numbers_set.difference(numbers_set)
        # for number in numbers_set:
        #     first_numbers_set.discard(number)
    elif current_command.startswith(COMMAND_REMOVE_SECOND):
        current_command_list = current_command.split()
        numbers_set = {int(element) for element in current_command_list if element.isdigit()}
        second_numbers_set = second_numbers_set.difference(numbers_set)
        # for number in numbers_set:
        #     second_numbers_set.discard(number)
    elif current_command == COMMAND_CHECK_SUBSET:
        first_check = first_numbers_set.issubset(second_numbers_set)
        second_check = second_numbers_set.issubset(first_numbers_set)
        if first_check or second_check:
            print("True")
        else:
            print("False")
    else:
        continue
sorted_first_numbers_set = sorted(first_numbers_set)
sorted_second_numbers_set = sorted(second_numbers_set)
print(*sorted_first_numbers_set, sep=", ")
print(*sorted_second_numbers_set, sep=", ")


# first_numbers_set = {int(number) for number in input().split()}
# second_numbers_set = {int(number) for number in input().split()}
# count_commands = int(input())
# for command in range(1, count_commands + 1):
#     first_command, second_command, *others_list = input().split()
#     others_set = {int(number) for number in others_list}
#     if first_command == "Add":
#         if second_command == "First":
#             first_numbers_set.update(others_set)
#         elif second_command == "Second":
#             second_numbers_set.update(others_set)
#         else:
#             continue
#     elif first_command == "Remove":
#         if second_command == "First":
#             first_numbers_set = first_numbers_set.difference(others_set)
#         elif second_command == "Second":
#             second_numbers_set = second_numbers_set.difference(others_set)
#         else:
#             continue
#     elif first_command == "Check" and second_command == "Subset":
#         first_check = first_numbers_set.issubset(second_numbers_set)
#         second_check = second_numbers_set.issubset(first_numbers_set)
#         if first_check or second_check:
#             print("True")
#         else:
#             print("False")
#     else:
#         continue
# sorted_first_numbers_set = sorted(first_numbers_set)
# sorted_second_numbers_set = sorted(second_numbers_set)
# print(*sorted_first_numbers_set, sep=", ")
# print(*sorted_second_numbers_set, sep=", ")
