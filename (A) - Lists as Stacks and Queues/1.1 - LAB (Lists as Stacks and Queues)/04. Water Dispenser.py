from collections import deque


def names_function():
    names = deque()
    while True:
        name = input()
        if name == "Start":
            break
        else:
            names.append(name)
    return names


def commands_function(water: int, people: deque):
    operations_deque = deque()
    while True:
        command = input()
        if command == "End":
            operation = f"{water} liters left"
            operations_deque.append(operation)
            break
        elif command.isdigit():
            liters = int(command)
            person_name = people.popleft()
            if liters <= water:
                operation = f"{person_name} got water"
                operations_deque.append(operation)
                water -= liters
            else:
                operation = f"{person_name} must wait"
                operations_deque.append(operation)
        elif command.startswith("refill"):
            command_list = command.split()
            add_liters = int(command_list[1])
            water += add_liters
        else:
            continue
    return operations_deque


starting_quantity_of_water = int(input())
names_deque = names_function()
result_deque = commands_function(starting_quantity_of_water, names_deque)
while result_deque:
    print(result_deque.popleft())


# from collections import deque
#
#
# def names_function():
#     names = deque()
#     while True:
#         name = input()
#         if name == "Start":
#             break
#         else:
#             names.append(name)
#     return names
#
#
# def commands_function(water: int, people: deque):
#     while True:
#         command = input()
#         if command == "End":
#             break
#         elif command.isdigit():
#             liters = int(command)
#             person_name = people.popleft()
#             if liters <= water:
#                 print(f"{person_name} got water")
#                 water -= liters
#             else:
#                 print(f"{person_name} must wait")
#         else:
#             command_list = command.split()
#             info = command_list[0]
#             if info == "refill":
#                 add_liters = int(command_list[1])
#                 water += add_liters
#             else:
#                 continue
#     return water
#
#
# starting_quantity_of_water = int(input())
# names_deque = names_function()
# left_liters = commands_function(starting_quantity_of_water, names_deque)
# print(f"{left_liters} liters left")


# from collections import deque
# quantity_of_water = int(input())
# names_deque = deque()
# while True:
#     name = input()
#     if name == "Start":
#         break
#     else:
#         names_deque.append(name)
# while True:
#     command = input()
#     if command == "End":
#         break
#     elif command.isdigit():
#         liters = int(command)
#         person_name = names_deque.popleft()
#         if liters <= quantity_of_water:
#             print(f"{person_name} got water")
#             quantity_of_water -= liters
#         else:
#             print(f"{person_name} must wait")
#     else:
#         command_list = command.split()
#         info = command_list[0]
#         if info == "refill":
#             add_liters = int(command_list[1])
#             quantity_of_water += add_liters
#         else:
#             continue
# print(f"{quantity_of_water} liters left")


# from collections import deque
# quantity_of_water = int(input())
# names_deque = deque()
# COMMAND_START = "Start"
# while True:
#     name = input()
#     if name == COMMAND_START:
#         break
#     else:
#         names_deque.append(name)
# COMMAND_END = "End"
# while True:
#     command = input()
#     if command == COMMAND_END:
#         break
#     elif command.isdigit():
#         liters = int(command)
#         if liters <= quantity_of_water:
#             person_name = names_deque.popleft()
#             print(f"{person_name} got water")
#             quantity_of_water -= liters
#         else:
#             person_name = names_deque.popleft()
#             print(f"{person_name} must wait")
#     else:
#         command_list = command.split()
#         info = command_list[0]
#         if info == "refill":
#             add_liters = int(command_list[1])
#             quantity_of_water += add_liters
#         else:
#             continue
# print(f"{quantity_of_water} liters left")
