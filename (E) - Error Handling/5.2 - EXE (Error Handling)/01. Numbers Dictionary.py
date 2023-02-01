numbers_dictionary = {}
COMMAND_SEARCH = "Search"
while True:
    try:
        command = input()
        if command == COMMAND_SEARCH:
            break
        else:
            number_as_string = command
            number = int(input())
            numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")
COMMAND_REMOVE = "Remove"
while True:
    try:
        command = input()
        if command == COMMAND_REMOVE:
            break
        else:
            searched_number = command
            if searched_number in numbers_dictionary.keys():
                print(numbers_dictionary[searched_number])
            else:
                raise KeyError
    except KeyError:
        print("Number does not exist in dictionary")
COMMAND_END = "End"
while True:
    try:
        command = input()
        if command == COMMAND_END:
            break
        else:
            searched_number = command
            if searched_number in numbers_dictionary.keys():
                del numbers_dictionary[searched_number]
            else:
                raise KeyError
    except KeyError:
        print("Number does not exist in dictionary")
print(numbers_dictionary)


# numbers_dictionary = {}
# while True:
#     try:
#         number_as_string = input()
#         if number_as_string == "Search":
#             break
#         else:
#             number = int(input())
#             numbers_dictionary[number_as_string] = number
#     except ValueError:
#         print("The variable number must be an integer")
# while True:
#     try:
#         searched_number = input()
#         if searched_number == "Remove":
#             break
#         else:
#             print(numbers_dictionary[searched_number])
#     except KeyError:
#         print("Number does not exist in dictionary")
# while True:
#     try:
#         searched_number = input()
#         if searched_number == "End":
#             break
#         else:
#             del numbers_dictionary[searched_number]
#     except KeyError:
#         print("Number does not exist in dictionary")
# print(numbers_dictionary)


# numbers_dictionary = {}
# try:
#     COMMAND_SEARCH = "Search"
#     while True:
#         command = input()
#         if command == COMMAND_SEARCH:
#             break
#         else:
#             number_as_string = command
#             number = int(input())
#             numbers_dictionary[number_as_string] = number
#     COMMAND_REMOVE = "Remove"
#     while True:
#         command = input()
#         if command == COMMAND_REMOVE:
#             break
#         else:
#             searched_number = command
#             if searched_number in numbers_dictionary.keys():
#                 print(numbers_dictionary[searched_number])
#             else:
#                 print("Number does not exist in dictionary")
#     COMMAND_END = "End"
#     while True:
#         command = input()
#         if command == COMMAND_END:
#             break
#         else:
#             searched_number = command
#             if searched_number in numbers_dictionary.keys():
#                 del numbers_dictionary[searched_number]
#             else:
#                 print("Number does not exist in dictionary")
# except ValueError:
#     print("The variable number must be an integer")
# finally:
#     print(numbers_dictionary)
