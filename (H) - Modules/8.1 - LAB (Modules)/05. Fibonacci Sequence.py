from module import create_sequence_function, locate_function


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
