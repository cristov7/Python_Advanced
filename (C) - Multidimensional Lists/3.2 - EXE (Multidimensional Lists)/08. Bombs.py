count_nested_lists = int(input())
matrix_list = []
for nested_list_index in range(count_nested_lists):
    nested_list = list(map(int, input().split()))
    matrix_list.append(nested_list)
coordinates_of_bombs_list = []
coordinates_list = input().split()
for coordinates in coordinates_list:
    bomb_list = list(map(int, coordinates.split(",")))
    coordinates_of_bombs_list.append(bomb_list)
for bomb_list in coordinates_of_bombs_list:
    coordinate_nested_list_index = bomb_list[0]
    coordinate_nested_element_index = bomb_list[1]
    bomb = matrix_list[coordinate_nested_list_index][coordinate_nested_element_index]
    if bomb > 0:
        for nested_list_index in range(len(matrix_list)):
            if nested_list_index == coordinate_nested_list_index - 1:
                for nested_element_index in range(len(matrix_list[nested_list_index])):
                    if nested_element_index == coordinate_nested_element_index - 1:
                        cell = matrix_list[nested_list_index][nested_element_index]
                        if cell > 0:
                            matrix_list[nested_list_index][nested_element_index] -= bomb
                        else:
                            continue
                    elif nested_element_index == coordinate_nested_element_index:
                        cell = matrix_list[nested_list_index][nested_element_index]
                        if cell > 0:
                            matrix_list[nested_list_index][nested_element_index] -= bomb
                        else:
                            continue
                    elif nested_element_index == coordinate_nested_element_index + 1:
                        cell = matrix_list[nested_list_index][nested_element_index]
                        if cell > 0:
                            matrix_list[nested_list_index][nested_element_index] -= bomb
                        else:
                            continue
                    else:
                        continue
            elif nested_list_index == coordinate_nested_list_index:
                for nested_element_index in range(len(matrix_list[nested_list_index])):
                    if nested_element_index == coordinate_nested_element_index - 1:
                        cell = matrix_list[nested_list_index][nested_element_index]
                        if cell > 0:
                            matrix_list[nested_list_index][nested_element_index] -= bomb
                        else:
                            continue
                    elif nested_element_index == coordinate_nested_element_index:
                        cell = matrix_list[nested_list_index][nested_element_index]
                        if cell > 0:
                            matrix_list[nested_list_index][nested_element_index] -= bomb
                        else:
                            continue
                    elif nested_element_index == coordinate_nested_element_index + 1:
                        cell = matrix_list[nested_list_index][nested_element_index]
                        if cell > 0:
                            matrix_list[nested_list_index][nested_element_index] -= bomb
                        else:
                            continue
                    else:
                        continue
            elif nested_list_index == coordinate_nested_list_index + 1:
                for nested_element_index in range(len(matrix_list[nested_list_index])):
                    if nested_element_index == coordinate_nested_element_index - 1:
                        cell = matrix_list[nested_list_index][nested_element_index]
                        if cell > 0:
                            matrix_list[nested_list_index][nested_element_index] -= bomb
                        else:
                            continue
                    elif nested_element_index == coordinate_nested_element_index:
                        cell = matrix_list[nested_list_index][nested_element_index]
                        if cell > 0:
                            matrix_list[nested_list_index][nested_element_index] -= bomb
                        else:
                            continue
                    elif nested_element_index == coordinate_nested_element_index + 1:
                        cell = matrix_list[nested_list_index][nested_element_index]
                        if cell > 0:
                            matrix_list[nested_list_index][nested_element_index] -= bomb
                        else:
                            continue
                    else:
                        continue
            else:
                continue
    else:
        continue
alive_cells = 0
sum_alive_cells = 0
for nested_list in matrix_list:
    for nested_element in nested_list:
        if nested_element > 0:
            alive_cells += 1
            sum_alive_cells += nested_element
        else:
            continue
print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_alive_cells}")
for nested_list in matrix_list:
    print(*nested_list, sep=" ")
