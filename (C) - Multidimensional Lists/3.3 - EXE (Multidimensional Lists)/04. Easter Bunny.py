def return_matrix_list_function(current_count_nested_lists: int):
    current_matrix_list = []
    for current_nested_list_index in range(current_count_nested_lists):
        current_nested_list = input().split()
        current_update_nested_list = []
        for current_nested_element in current_nested_list:
            if current_nested_element.isalpha():
                current_update_nested_list.append(current_nested_element)
            else:
                current_nested_element = int(current_nested_element)
                current_update_nested_list.append(current_nested_element)
        current_matrix_list.append(current_update_nested_list)
    return current_matrix_list


def return_bunny_coordinates_list_function(current_matrix_list: list):
    for current_nested_list_index in range(len(current_matrix_list)):
        for current_nested_element_index in range(len(current_matrix_list[current_nested_list_index])):
            current_nested_element = current_matrix_list[current_nested_list_index][current_nested_element_index]
            if current_nested_element == "B":
                return [current_nested_list_index, current_nested_element_index]
            else:
                continue


def return_up_direction_info_function(current_matrix_list: list, current_bunny_coordinates_list: list):
    current_bunny_coordinates_nested_list = current_bunny_coordinates_list[0]
    current_bunny_coordinates_nested_element = current_bunny_coordinates_list[1]
    current_count_eggs = 0
    current_up_direction_matrix_list = []
    for current_nested_list in range(len(current_matrix_list) - 1, -1, -1):
        for current_nested_element in range(len(current_matrix_list[current_nested_list])):
            if current_nested_list < current_bunny_coordinates_nested_list \
                    and current_nested_element == current_bunny_coordinates_nested_element:
                current_eggs = current_matrix_list[current_nested_list][current_nested_element]
                if current_eggs == "X":
                    return {current_count_eggs: current_up_direction_matrix_list}
                elif current_eggs > 0:
                    current_count_eggs += current_eggs
                    current_up_direction_matrix_list.append([current_nested_list, current_nested_element])
                else:
                    current_up_direction_matrix_list.append([current_nested_list, current_nested_element])
            else:
                continue
    return {current_count_eggs: current_up_direction_matrix_list}


def return_down_direction_info_function(current_matrix_list: list, current_bunny_coordinates_list: list):
    current_bunny_coordinates_nested_list = current_bunny_coordinates_list[0]
    current_bunny_coordinates_nested_element = current_bunny_coordinates_list[1]
    current_count_eggs = 0
    current_down_direction_matrix_list = []
    for current_nested_list in range(len(current_matrix_list)):
        for current_nested_element in range(len(current_matrix_list[current_nested_list])):
            if current_nested_list > current_bunny_coordinates_nested_list \
                    and current_nested_element == current_bunny_coordinates_nested_element:
                current_eggs = current_matrix_list[current_nested_list][current_nested_element]
                if current_eggs == "X":
                    return {current_count_eggs: current_down_direction_matrix_list}
                elif current_eggs > 0:
                    current_count_eggs += current_eggs
                    current_down_direction_matrix_list.append([current_nested_list, current_nested_element])
                else:
                    current_down_direction_matrix_list.append([current_nested_list, current_nested_element])
            else:
                continue
    return {current_count_eggs: current_down_direction_matrix_list}


def return_left_direction_info_function(current_matrix_list: list, current_bunny_coordinates_list: list):
    current_bunny_coordinates_nested_list = current_bunny_coordinates_list[0]
    current_bunny_coordinates_nested_element = current_bunny_coordinates_list[1]
    current_count_eggs = 0
    current_left_direction_matrix_list = []
    for current_nested_list in range(len(current_matrix_list)):
        for current_nested_element in range(len(current_matrix_list[current_nested_list]) - 1, -1, -1):
            if current_nested_list == current_bunny_coordinates_nested_list \
                    and current_nested_element < current_bunny_coordinates_nested_element:
                current_eggs = current_matrix_list[current_nested_list][current_nested_element]
                if current_eggs == "X":
                    return {current_count_eggs: current_left_direction_matrix_list}
                elif current_eggs > 0:
                    current_count_eggs += current_eggs
                    current_left_direction_matrix_list.append([current_nested_list, current_nested_element])
                else:
                    current_left_direction_matrix_list.append([current_nested_list, current_nested_element])
            else:
                continue
    return {current_count_eggs: current_left_direction_matrix_list}


def return_right_direction_info_function(current_matrix_list: list, current_bunny_coordinates_list: list):
    current_bunny_coordinates_nested_list = current_bunny_coordinates_list[0]
    current_bunny_coordinates_nested_element = current_bunny_coordinates_list[1]
    current_count_eggs = 0
    current_right_direction_matrix_list = []
    for current_nested_list in range(len(current_matrix_list)):
        for current_nested_element in range(len(current_matrix_list[current_nested_list])):
            if current_nested_list == current_bunny_coordinates_nested_list \
                    and current_nested_element > current_bunny_coordinates_nested_element:
                current_eggs = current_matrix_list[current_nested_list][current_nested_element]
                if current_eggs == "X":
                    return {current_count_eggs: current_right_direction_matrix_list}
                elif current_eggs > 0:
                    current_count_eggs += current_eggs
                    current_right_direction_matrix_list.append([current_nested_list, current_nested_element])
                else:
                    current_right_direction_matrix_list.append([current_nested_list, current_nested_element])
            else:
                continue
    return {current_count_eggs: current_right_direction_matrix_list}


def return_info_list_functions(current_up_direction_dict: dict, current_down_direction_dict: dict, current_left_direction_dict: dict, current_right_direction_dict: dict):
    current_direction = ""
    current_direction_matrix_list = []
    current_collecting_eggs = 0
    for current_count_eggs, current_matrix_list in current_up_direction_dict.items():
        if current_count_eggs >= current_collecting_eggs:
            current_direction = "up"
            current_direction_matrix_list = current_matrix_list
            current_collecting_eggs = current_count_eggs
            break
        else:
            break
    for current_count_eggs, current_matrix_list in current_down_direction_dict.items():
        if current_count_eggs >= current_collecting_eggs:
            current_direction = "down"
            current_direction_matrix_list = current_matrix_list
            current_collecting_eggs = current_count_eggs
            break
        else:
            break
    for current_count_eggs, current_matrix_list in current_left_direction_dict.items():
        if current_count_eggs >= current_collecting_eggs:
            current_direction = "left"
            current_direction_matrix_list = current_matrix_list
            current_collecting_eggs = current_count_eggs
            break
        else:
            break
    for current_count_eggs, current_matrix_list in current_right_direction_dict.items():
        if current_count_eggs >= current_collecting_eggs:
            current_direction = "right"
            current_direction_matrix_list = current_matrix_list
            current_collecting_eggs = current_count_eggs
            break
        else:
            break
    return [current_direction, current_direction_matrix_list, current_collecting_eggs]


size_of_the_field = int(input())
matrix_list = return_matrix_list_function(size_of_the_field)
bunny_coordinates_list = return_bunny_coordinates_list_function(matrix_list)
up_direction_dict = return_up_direction_info_function(matrix_list, bunny_coordinates_list)
down_direction_dict = return_down_direction_info_function(matrix_list, bunny_coordinates_list)
left_direction_dict = return_left_direction_info_function(matrix_list, bunny_coordinates_list)
right_direction_dict = return_right_direction_info_function(matrix_list, bunny_coordinates_list)
info_list = return_info_list_functions(up_direction_dict, down_direction_dict, left_direction_dict, right_direction_dict)
direction = info_list[0]
direction_matrix_list = info_list[1]
collecting_eggs = info_list[2]
print(direction)
[print(direction_nested_list) for direction_nested_list in direction_matrix_list]
print(collecting_eggs)
