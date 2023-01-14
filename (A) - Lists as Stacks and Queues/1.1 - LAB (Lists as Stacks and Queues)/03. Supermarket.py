from collections import deque
names_deque = deque()
while True:
    name = input()
    if name == "End":
        count = len(names_deque)
        print(f"{count} people remaining.")
        break
    elif name == "Paid":
        while names_deque:
            current_name = names_deque.popleft()
            print(current_name)
    else:
        names_deque.append(name)


# from _collections import deque
# names_deque = deque()
# COMMAND_END = "End"
# COMMAND_PAID = "Paid"
# while True:
#     name = input()
#     if name == COMMAND_END:
#         count = len(names_deque)
#         print(f"{count} people remaining.")
#         break
#     elif name == COMMAND_PAID:
#         while names_deque:
#             current_name = names_deque.popleft()
#             print(current_name)
#     else:
#         names_deque.append(name)


# from collections import deque
# queue = deque()
# while True:
#     command = input()
#     if command == "Paid":
#         while len(queue):
#             print(queue.popleft())
#     elif command == "End":
#         print(f"{len(queue)} people remaining.")
#         break
#     else:
#         queue.append(command)


# names_list = []
# while True:
#     name = input()
#     if name == "End":
#         count = len(names_list)
#         print(f"{count} people remaining.")
#         break
#     elif name == "Paid":
#         [print(name) for name in names_list]
#         names_list = []
#     else:
#         names_list.append(name)
