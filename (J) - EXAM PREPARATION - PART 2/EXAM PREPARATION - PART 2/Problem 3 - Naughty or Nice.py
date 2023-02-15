def naughty_or_nice_list(kids_info_tuples_in_list, *commands_info_in_tuple, **commands_info_in_dict):
    def return_output_list_function():
        current_output_list = []
        if kids_in_nice_list:
            convert_info = ", ".join(kids_in_nice_list)
            current_output = f"Nice: {convert_info}"
            current_output_list.append(current_output)
        if kids_in_naughty_list:
            convert_info = ", ".join(kids_in_naughty_list)
            current_output = f"Naughty: {convert_info}"
            current_output_list.append(current_output)
        if kids_in_not_found_list:
            convert_info = ", ".join(kids_in_not_found_list)
            current_output = f"Not found: {convert_info}"
            current_output_list.append(current_output)
        return current_output_list

    def first_check_function():
        counter = 0
        kid = ""
        index = 0
        for index_tuple, kid_tuple in enumerate(kids_info_tuples_in_list):
            kid_number = kid_tuple[0]
            kid_name = kid_tuple[1]
            if number == kid_number:
                counter += 1
                if counter == 1:
                    kid = kid_name
                    index = index_tuple
                else:
                    break
            else:
                continue
        if counter == 1:
            del kids_info_tuples_in_list[index]
            if info == "Nice":
                kids_in_nice_list.append(kid)
            elif info == "Naughty":
                kids_in_naughty_list.append(kid)

    def second_check_function():
        counter = 0
        kid = ""
        index = 0
        for index_tuple, kid_tuple in enumerate(kids_info_tuples_in_list):
            kid_name = kid_tuple[1]
            if name == kid_name:
                counter += 1
                if counter == 1:
                    kid = name
                    index = index_tuple
                else:
                    break
            else:
                continue
        if counter == 1:
            del kids_info_tuples_in_list[index]
            if info == "Nice":
                kids_in_nice_list.append(kid)
            elif info == "Naughty":
                kids_in_naughty_list.append(kid)

    kids_in_nice_list = []
    kids_in_naughty_list = []
    kids_in_not_found_list = []
    for command_string in commands_info_in_tuple:
        command_list = command_string.split("-")
        number = int(command_list[0])
        info = command_list[1]
        first_check_function()
    for name, info in commands_info_in_dict.items():
        second_check_function()
    for rest_tuple in kids_info_tuples_in_list:
        name = rest_tuple[1]
        kids_in_not_found_list.append(name)
    output_list = return_output_list_function()
    return "\n".join(output_list)


# def naughty_or_nice_list(kids_info_tuples_in_list, *commands_info_in_tuple, **commands_info_in_dict):
#     def check_for_kid_function():
#         if len(kids_tuples_in_list) == 1:
#             nice_kids_tuples_in_list.extend(kids_tuples_in_list) if info == "Nice" else naughty_kids_tuples_in_list.extend(kids_tuples_in_list)
#             kids_info_tuples_in_list.remove(*kids_tuples_in_list)
#
#     nice_kids_tuples_in_list = []
#     naughty_kids_tuples_in_list = []
#     for command_string in commands_info_in_tuple:
#         command_list = command_string.split("-")
#         number = int(command_list[0])
#         info = command_list[1]
#         kids_tuples_in_list = [kid_tuple for kid_tuple in kids_info_tuples_in_list if kid_tuple[0] == number]
#         check_for_kid_function()
#     for name, info in commands_info_in_dict.items():
#         kids_tuples_in_list = [kid_tuple for kid_tuple in kids_info_tuples_in_list if kid_tuple[1] == name]
#         check_for_kid_function()
#     output_list = []
#     if nice_kids_tuples_in_list:
#         output_list.append(f"Nice: {', '.join(kid_tuple[1] for kid_tuple in nice_kids_tuples_in_list)}")
#     if naughty_kids_tuples_in_list:
#         output_list.append(f"Naughty: {', '.join(kid_tuple[1] for kid_tuple in naughty_kids_tuples_in_list)}")
#     if kids_info_tuples_in_list:
#         output_list.append(f"Not found: {', '.join(kid_tuple[1] for kid_tuple in kids_info_tuples_in_list)}")
#     return "\n".join(output_list)


# print(naughty_or_nice_list(
#     [(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy")],
#     "3-Nice", "1-Naughty",
#     Amy="Nice", Katy="Naughty"))


# print(naughty_or_nice_list(
#     [(7, "Peter"), (1, "Lilly"), (2, "Peter"), (12, "Peter"), (3, "Simon")],
#     "3-Nice", "5-Naughty", "2-Nice", "1-Nice"))


# print(naughty_or_nice_list(
#     [(6, "John"), (4, "Karen"), (2, "Tim"), (1, "Merry"), (6, "Frank")],
#     "6-Nice", "5-Naughty", "4-Nice", "3-Naughty", "2-Nice", "1-Naughty",
#     Frank="Nice", Merry="Nice", John="Naughty"))
