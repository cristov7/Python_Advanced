size_of_the_square_matrix = int(input())
matrix_list = []
for nested_list_index in range(size_of_the_square_matrix):
    nested_list = input().split()
    matrix_list.append(nested_list)
alice_coordinates_bool = False
alice_nested_list_index = None
alice_nested_element_index = None
for nested_list_index in range(len(matrix_list)):
    if alice_coordinates_bool:
        break
    else:
        for nested_element_index in range(len(matrix_list[nested_list_index])):
            nested_element = matrix_list[nested_list_index][nested_element_index]
            if nested_element == "A":
                alice_nested_list_index = nested_list_index
                alice_nested_element_index = nested_element_index
                alice_coordinates_bool = True
                matrix_list[nested_list_index][nested_element_index] = "*"
                break
            else:
                continue
collects_tea_bags = 0
COMMAND_UP = "up"
COMMAND_DOWN = "down"
COMMAND_LEFT = "left"
COMMAND_RIGHT = "right"
while True:
    command = input()
    if command == COMMAND_UP:
        if alice_nested_list_index > 0:
            alice_nested_list_index -= 1
            nested_element = matrix_list[alice_nested_list_index][alice_nested_element_index]
            if nested_element == "R":
                print("Alice didn't make it to the tea party.")
                matrix_list[alice_nested_list_index][alice_nested_element_index] = "*"
                break
            elif nested_element.isdigit():
                nested_element = int(nested_element)
                collects_tea_bags += nested_element
                if collects_tea_bags >= 10:
                    print("She did it! She went to the party.")
                    matrix_list[alice_nested_list_index][alice_nested_element_index] = "*"
                    break
                else:
                    matrix_list[alice_nested_list_index][alice_nested_element_index] = "*"
            elif nested_element == ".":
                matrix_list[alice_nested_list_index][alice_nested_element_index] = "*"
            else:
                continue
        else:
            print("Alice didn't make it to the tea party.")
            break
    elif command == COMMAND_DOWN:
        if alice_nested_list_index < len(matrix_list) - 1:
            alice_nested_list_index += 1
            nested_element = matrix_list[alice_nested_list_index][alice_nested_element_index]
            if nested_element == "R":
                print("Alice didn't make it to the tea party.")
                matrix_list[alice_nested_list_index][alice_nested_element_index] = "*"
                break
            elif nested_element.isdigit():
                nested_element = int(nested_element)
                collects_tea_bags += nested_element
                if collects_tea_bags >= 10:
                    print("She did it! She went to the party.")
                    matrix_list[alice_nested_list_index][alice_nested_element_index] = "*"
                    break
                else:
                    matrix_list[alice_nested_list_index][alice_nested_element_index] = "*"
            elif nested_element == ".":
                matrix_list[alice_nested_list_index][alice_nested_element_index] = "*"
            else:
                continue
        else:
            print("Alice didn't make it to the tea party.")
            break
    elif command == COMMAND_LEFT:
        if alice_nested_element_index > 0:
            alice_nested_element_index -= 1
            nested_element = matrix_list[alice_nested_list_index][alice_nested_element_index]
            if nested_element == "R":
                print("Alice didn't make it to the tea party.")
                matrix_list[alice_nested_list_index][alice_nested_element_index] = "*"
                break
            elif nested_element.isdigit():
                nested_element = int(nested_element)
                collects_tea_bags += nested_element
                if collects_tea_bags >= 10:
                    print("She did it! She went to the party.")
                    matrix_list[alice_nested_list_index][alice_nested_element_index] = "*"
                    break
                else:
                    matrix_list[alice_nested_list_index][alice_nested_element_index] = "*"
            elif nested_element == ".":
                matrix_list[alice_nested_list_index][alice_nested_element_index] = "*"
            else:
                continue
        else:
            print("Alice didn't make it to the tea party.")
            break
    elif command == COMMAND_RIGHT:
        if alice_nested_element_index < len(matrix_list[alice_nested_list_index]) - 1:
            alice_nested_element_index += 1
            nested_element = matrix_list[alice_nested_list_index][alice_nested_element_index]
            if nested_element == "R":
                print("Alice didn't make it to the tea party.")
                matrix_list[alice_nested_list_index][alice_nested_element_index] = "*"
                break
            elif nested_element.isdigit():
                nested_element = int(nested_element)
                collects_tea_bags += nested_element
                if collects_tea_bags >= 10:
                    print("She did it! She went to the party.")
                    matrix_list[alice_nested_list_index][alice_nested_element_index] = "*"
                    break
                else:
                    matrix_list[alice_nested_list_index][alice_nested_element_index] = "*"
            elif nested_element == ".":
                matrix_list[alice_nested_list_index][alice_nested_element_index] = "*"
            else:
                continue
        else:
            print("Alice didn't make it to the tea party.")
            break
    else:
        print("Alice didn't make it to the tea party.")
        break
for nested_list_index in range(len(matrix_list)):
    for nested_element_index in range(len(matrix_list[nested_list_index])):
        nested_element = matrix_list[nested_list_index][nested_element_index]
        if nested_element.isdigit():
            nested_element = int(nested_element)
            print(nested_element, end=" ")
        else:
            print(nested_element, end=" ")
    print()
