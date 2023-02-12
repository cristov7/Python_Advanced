def return_matrix_list_function(size_of_the_square_racing_track):
    current_matrix_list = []
    for index_nested_list in range(size_of_the_square_racing_track):
        current_nested_list = input().split()
        current_matrix_list.append(current_nested_list)
    return current_matrix_list


def return_tunnels_coordinates_function(current_matrix_list):
    current_tunnels_coordinates_list = []
    for index_nested_list in range(len(current_matrix_list)):
        current_nested_list = current_matrix_list[index_nested_list]
        for index_nested_element, current_nested_element in enumerate(current_nested_list):
            if current_nested_element == "T":
                if len(current_tunnels_coordinates_list) == 0:
                    first_tunnel_coordinates_list = [index_nested_list, index_nested_element]
                    current_tunnels_coordinates_list.append(first_tunnel_coordinates_list)
                else:   # elif len(current_tunnels_coordinates_list) == 1:
                    second_tunnel_coordinates_list = [index_nested_list, index_nested_element]
                    current_tunnels_coordinates_list.append(second_tunnel_coordinates_list)
                    return current_tunnels_coordinates_list
            else:
                continue


def rally_racing_function(current_matrix_list, current_racing_number, current_car_coordinates_list, current_tunnels_coordinates_list):
    def print_function():
        current_matrix_list[car_index_nested_list][car_index_nested_element] = "C"
        if race_finish:
            print(f"Racing car {current_racing_number} finished the stage!")
        else:   # elif not race_finish:
            print(f"Racing car {current_racing_number} DNF.")
        print(f"Distance covered {distance_km} km.")
        for current_nested_list in current_matrix_list:
            print("".join(current_nested_list))

    def tunnels_function(current_car_index_nested_list, current_car_index_nested_element):
        first_tunnel_coordinates_list = current_tunnels_coordinates_list[0]
        second_tunnel_coordinates_list = current_tunnels_coordinates_list[1]
        if current_car_index_nested_list == first_tunnel_coordinates_list[0] and current_car_index_nested_element == first_tunnel_coordinates_list[1]:
            current_car_index_nested_list = second_tunnel_coordinates_list[0]
            current_car_index_nested_element = second_tunnel_coordinates_list[1]
        elif current_car_index_nested_list == second_tunnel_coordinates_list[0] and current_car_index_nested_element == second_tunnel_coordinates_list[1]:
            current_car_index_nested_list = first_tunnel_coordinates_list[0]
            current_car_index_nested_element = first_tunnel_coordinates_list[1]
        else:
            raise SystemExit("Error operation...")
        current_matrix_list[first_tunnel_coordinates_list[0]][first_tunnel_coordinates_list[1]] = "."
        current_matrix_list[second_tunnel_coordinates_list[0]][second_tunnel_coordinates_list[1]] = "."
        return current_car_index_nested_list, current_car_index_nested_element

    car_index_nested_list = current_car_coordinates_list[0]
    car_index_nested_element = current_car_coordinates_list[1]
    race_finish = False
    distance_km = 0
    while True:
        command = input()
        if command == "End":
            break
        elif command == "left":
            if 0 <= car_index_nested_element - 1:
                car_index_nested_element -= 1
                current_nested_element = current_matrix_list[car_index_nested_list][car_index_nested_element]
                if current_nested_element == ".":
                    distance_km += 10
                elif current_nested_element == "T":
                    car_index_nested_list, car_index_nested_element = tunnels_function(car_index_nested_list, car_index_nested_element)
                    distance_km += 30
                elif current_nested_element == "F":
                    race_finish = True
                    distance_km += 10
                    break
                else:
                    raise SystemExit("Invalid char...")
            else:
                continue
        elif command == "right":
            if car_index_nested_element + 1 < len(current_matrix_list):
                car_index_nested_element += 1
                current_nested_element = current_matrix_list[car_index_nested_list][car_index_nested_element]
                if current_nested_element == ".":
                    distance_km += 10
                elif current_nested_element == "T":
                    car_index_nested_list, car_index_nested_element = tunnels_function(car_index_nested_list, car_index_nested_element)
                    distance_km += 30
                elif current_nested_element == "F":
                    race_finish = True
                    distance_km += 10
                    break
                else:
                    raise SystemExit("Invalid char...")
            else:
                continue
        elif command == "up":
            if 0 <= car_index_nested_list - 1:
                car_index_nested_list -= 1
                current_nested_element = current_matrix_list[car_index_nested_list][car_index_nested_element]
                if current_nested_element == ".":
                    distance_km += 10
                elif current_nested_element == "T":
                    car_index_nested_list, car_index_nested_element = tunnels_function(car_index_nested_list, car_index_nested_element)
                    distance_km += 30
                elif current_nested_element == "F":
                    race_finish = True
                    distance_km += 10
                    break
                else:
                    raise SystemExit("Invalid char...")
            else:
                continue
        elif command == "down":
            if car_index_nested_list + 1 < len(current_matrix_list):
                car_index_nested_list += 1
                current_nested_element = current_matrix_list[car_index_nested_list][car_index_nested_element]
                if current_nested_element == ".":
                    distance_km += 10
                elif current_nested_element == "T":
                    car_index_nested_list, car_index_nested_element = tunnels_function(car_index_nested_list, car_index_nested_element)
                    distance_km += 30
                elif current_nested_element == "F":
                    race_finish = True
                    distance_km += 10
                    break
                else:
                    raise SystemExit("Invalid char...")
            else:
                continue
        else:
            raise SystemExit("Invalid command...")
    print_function()


size_of_the_square_matrix = int(input())
racing_number = input()
matrix_list = return_matrix_list_function(size_of_the_square_matrix)
car_coordinates_list = [0, 0]
tunnels_coordinates_list = return_tunnels_coordinates_function(matrix_list)
rally_racing_function(matrix_list, racing_number, car_coordinates_list, tunnels_coordinates_list)


# size_of_the_square_matrix = int(input())
# racing_number = input()
# matrix_list = []
# first_tunnel_list = []
# second_tunnel_list = []
# for index_nested_list in range(size_of_the_square_matrix):
#     nested_list = input().split()
#     for index_nested_element, nested_element in enumerate(nested_list):
#         if nested_element == "T":
#             coordinates_list = [index_nested_list, index_nested_element]
#             if len(first_tunnel_list) == 0:
#                 first_tunnel_list = coordinates_list
#             else:
#                 second_tunnel_list = coordinates_list
#         else:
#             continue
#     matrix_list.append(nested_list)
# car_index_nested_list = 0
# car_index_nested_element = 0
# distance_km = 0
# COMMAND_END = "End"
# COMMAND_LEFT = "left"
# COMMAND_RIGHT = "right"
# COMMAND_UP = "up"
# COMMAND_DOWN = "down"
# while True:
#     command = input()
#     if command == COMMAND_END:
#         print(f"Racing car {racing_number} DNF.")
#         break
#     elif command == COMMAND_LEFT:
#         if 0 <= car_index_nested_element - 1:
#             car_index_nested_element -= 1
#             nested_element = matrix_list[car_index_nested_list][car_index_nested_element]
#             if nested_element == ".":
#                 distance_km += 10
#             elif nested_element == "T":
#                 first_index_nested_list = first_tunnel_list[0]
#                 first_index_nested_element = first_tunnel_list[1]
#                 second_index_nested_list = second_tunnel_list[0]
#                 second_index_nested_element = second_tunnel_list[1]
#                 matrix_list[first_index_nested_list][first_index_nested_element] = "."
#                 matrix_list[second_index_nested_list][second_index_nested_element] = "."
#                 if (car_index_nested_list == first_index_nested_list) and\
#                         (car_index_nested_element == first_index_nested_element):
#                     car_index_nested_list = second_index_nested_list
#                     car_index_nested_element = second_index_nested_element
#                 else:   # elif (car_index_nested_list == second_index_nested_list) and\
#                     # (car_index_nested_element == second_index_nested_element):
#                     car_index_nested_list = first_index_nested_list
#                     car_index_nested_element = first_index_nested_element
#                 distance_km += 30
#             else:  # elif nested_element == "F":
#                 print(f"Racing car {racing_number} finished the stage!")
#                 distance_km += 10
#                 break
#         else:
#             continue
#     elif command == COMMAND_RIGHT:
#         if car_index_nested_element + 1 < size_of_the_square_matrix:
#             car_index_nested_element += 1
#             nested_element = matrix_list[car_index_nested_list][car_index_nested_element]
#             if nested_element == ".":
#                 distance_km += 10
#             elif nested_element == "T":
#                 first_index_nested_list = first_tunnel_list[0]
#                 first_index_nested_element = first_tunnel_list[1]
#                 second_index_nested_list = second_tunnel_list[0]
#                 second_index_nested_element = second_tunnel_list[1]
#                 matrix_list[first_index_nested_list][first_index_nested_element] = "."
#                 matrix_list[second_index_nested_list][second_index_nested_element] = "."
#                 if (car_index_nested_list == first_index_nested_list) and \
#                         (car_index_nested_element == first_index_nested_element):
#                     car_index_nested_list = second_index_nested_list
#                     car_index_nested_element = second_index_nested_element
#                 else:  # elif (car_index_nested_list == second_index_nested_list) and\
#                     # (car_index_nested_element == second_index_nested_element):
#                     car_index_nested_list = first_index_nested_list
#                     car_index_nested_element = first_index_nested_element
#                 distance_km += 30
#             else:  # elif nested_element == "F":
#                 print(f"Racing car {racing_number} finished the stage!")
#                 distance_km += 10
#                 break
#         else:
#             continue
#     elif command == COMMAND_UP:
#         if 0 <= car_index_nested_list - 1:
#             car_index_nested_list -= 1
#             nested_element = matrix_list[car_index_nested_list][car_index_nested_element]
#             if nested_element == ".":
#                 distance_km += 10
#             elif nested_element == "T":
#                 first_index_nested_list = first_tunnel_list[0]
#                 first_index_nested_element = first_tunnel_list[1]
#                 second_index_nested_list = second_tunnel_list[0]
#                 second_index_nested_element = second_tunnel_list[1]
#                 matrix_list[first_index_nested_list][first_index_nested_element] = "."
#                 matrix_list[second_index_nested_list][second_index_nested_element] = "."
#                 if (car_index_nested_list == first_index_nested_list) and \
#                         (car_index_nested_element == first_index_nested_element):
#                     car_index_nested_list = second_index_nested_list
#                     car_index_nested_element = second_index_nested_element
#                 else:  # elif (car_index_nested_list == second_index_nested_list) and\
#                     # (car_index_nested_element == second_index_nested_element):
#                     car_index_nested_list = first_index_nested_list
#                     car_index_nested_element = first_index_nested_element
#                 distance_km += 30
#             else:  # elif nested_element == "F":
#                 print(f"Racing car {racing_number} finished the stage!")
#                 distance_km += 10
#                 break
#         else:
#             continue
#     elif command == COMMAND_DOWN:
#         if car_index_nested_list + 1 < size_of_the_square_matrix:
#             car_index_nested_list += 1
#             nested_element = matrix_list[car_index_nested_list][car_index_nested_element]
#             if nested_element == ".":
#                 distance_km += 10
#             elif nested_element == "T":
#                 first_index_nested_list = first_tunnel_list[0]
#                 first_index_nested_element = first_tunnel_list[1]
#                 second_index_nested_list = second_tunnel_list[0]
#                 second_index_nested_element = second_tunnel_list[1]
#                 matrix_list[first_index_nested_list][first_index_nested_element] = "."
#                 matrix_list[second_index_nested_list][second_index_nested_element] = "."
#                 if (car_index_nested_list == first_index_nested_list) and \
#                         (car_index_nested_element == first_index_nested_element):
#                     car_index_nested_list = second_index_nested_list
#                     car_index_nested_element = second_index_nested_element
#                 else:  # elif (car_index_nested_list == second_index_nested_list) and\
#                     # (car_index_nested_element == second_index_nested_element):
#                     car_index_nested_list = first_index_nested_list
#                     car_index_nested_element = first_index_nested_element
#                 distance_km += 30
#             else:  # elif nested_element == "F":
#                 print(f"Racing car {racing_number} finished the stage!")
#                 distance_km += 10
#                 break
#         else:
#             continue
#     else:
#         continue
# matrix_list[car_index_nested_list][car_index_nested_element] = "C"
# print(f"Distance covered {distance_km} km.")
# for nested_list in matrix_list:
#     print("".join(nested_list))
