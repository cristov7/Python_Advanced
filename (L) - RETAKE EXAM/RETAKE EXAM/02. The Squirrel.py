def set_coordinates_func() -> None:
    global current_index_nested_list
    global current_index_nested_element
    for index_nested_list, nested_list in enumerate(matrix_list):
        for index_nested_element, nested_element in enumerate(nested_list):
            if nested_element == "s":
                current_index_nested_list = index_nested_list
                current_index_nested_element = index_nested_element
                break


def check_position_func() -> None:
    global collected_hazelnuts
    current_position = matrix_list[current_index_nested_list][current_index_nested_element]
    if current_position == "h":
        collected_hazelnuts += 1
        matrix_list[current_index_nested_list][current_index_nested_element] = "s"
        if collected_hazelnuts == 3:
            print(f"Good job! You have collected all hazelnuts!")
            print(f"Hazelnuts collected: {collected_hazelnuts}")
            raise SystemExit
    elif current_position == "t":
        matrix_list[current_index_nested_list][current_index_nested_element] = "s"
        print("Unfortunately, the squirrel stepped on a trap...")
        print(f"Hazelnuts collected: {collected_hazelnuts}")
        raise SystemExit
    else:
        matrix_list[current_index_nested_list][current_index_nested_element] = "s"


def out_of_the_field_func() -> None:
    global collected_hazelnuts
    print("The squirrel is out of the field.")
    print(f"Hazelnuts collected: {collected_hazelnuts}")
    raise SystemExit


collected_hazelnuts = 0
size_of_a_square_matrix = int(input())
directions_list = input().split(", ")
matrix_list = [list(input()) for index_nested_list in range(size_of_a_square_matrix)]
current_index_nested_list = 0
current_index_nested_element = 0
set_coordinates_func()
for direction in directions_list:
    matrix_list[current_index_nested_list][current_index_nested_element] = "*"
    if direction == "left":
        if current_index_nested_element - 1 < 0:
            out_of_the_field_func()
        else:
            current_index_nested_element -= 1
            check_position_func()
    elif direction == "right":
        if current_index_nested_element + 1 == size_of_a_square_matrix:
            out_of_the_field_func()
        else:
            current_index_nested_element += 1
            check_position_func()
    elif direction == "down":
        if current_index_nested_list + 1 == size_of_a_square_matrix:
            out_of_the_field_func()
        else:
            current_index_nested_list += 1
            check_position_func()
    elif direction == "up":
        if current_index_nested_list - 1 < 0:
            out_of_the_field_func()
        else:
            current_index_nested_list -= 1
            check_position_func()
print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {collected_hazelnuts}")
