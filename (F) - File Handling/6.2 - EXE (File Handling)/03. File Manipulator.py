import os


def return_modification_lines_list_function(current_lines_list: list, remove_string: str, add_string: str):
    modification_list = []
    for line in current_lines_list:
        modification_line = line.replace(remove_string, add_string)
        modification_list.append(modification_line)
    return modification_list


COMMAND_END = "End"
while True:
    command = input()
    if command == COMMAND_END:
        break
    else:
        command_list = command.split("-")
        info = command_list[0]
        if info == "Create":
            file_name = command_list[1]
            file = open(f"{file_name}", "w")
            file.close()
        elif info == "Add":
            file_name = command_list[1]
            content = command_list[2]
            file = open(f"{file_name}", "a")
            file.write(f"{content}\n")
            file.close()
        elif info == "Replace":
            file_name = command_list[1]
            old_string = command_list[2]
            new_string = command_list[3]
            if os.path.exists(file_name):
                with open(f"{file_name}", "r") as file:
                    lines_list = file.readlines()
                new_lines_list = return_modification_lines_list_function(lines_list, old_string, new_string)
                file = open(file_name, "w")
                file.writelines(new_lines_list)
                file.close()
            else:
                print("An error occurred")
        elif info == "Delete":
            file_name = command_list[1]
            if os.path.exists(file_name):
                os.remove(f"{file_name}")
            else:
                print("An error occurred")
        else:
            continue
