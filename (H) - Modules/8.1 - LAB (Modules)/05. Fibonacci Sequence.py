from module import create_sequence_function, locate_function


# def create_sequence_function(count_numbers: int):
#     numbers_list = []
#     for count_number in range(1, count_numbers + 1):
#         if count_number == 1:
#             current_number = 0
#             numbers_list.append(current_number)
#         elif count_number == 2:
#             current_number = 1
#             numbers_list.append(current_number)
#         else:
#             last_number = numbers_list[-1]
#             pre_last_number = numbers_list[-2]
#             current_number = last_number + pre_last_number
#             numbers_list.append(current_number)
#     return numbers_list


# def locate_function(search_number: int, numbers_list: list):
#     if search_number in numbers_list:
#         index = numbers_list.index(search_number)
#         return f"The number - {search_number} is at index {index}"
#     else:
#         return f"The number {search_number} is not in the sequence"


def fibonacci_function():
    fibonacci_list = []
    while True:
        command = input()
        if command == COMMAND_END:
            break
        elif command.startswith("Create Sequence"):
            command_list = command.split()
            count = int(command_list[-1])
            fibonacci_list = create_sequence_function(count)
            print(*fibonacci_list)
        elif command.startswith("Locate"):
            command_list = command.split()
            number = int(command_list[-1])
            locate = locate_function(number, fibonacci_list)
            print(locate)
        else:
            continue


COMMAND_END = "Stop"
fibonacci_function()
