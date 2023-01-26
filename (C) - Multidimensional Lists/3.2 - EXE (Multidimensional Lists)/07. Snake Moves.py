from collections import deque
info_list = list(map(int, input().split()))
count_nested_lists = info_list[0]
count_nested_elements = info_list[1]
snake_list = list(input())
snake_queue = deque(snake_list)
matrix_list = []
for nested_list_index in range(count_nested_lists):
    nested_list = []
    for nested_element_index in range(count_nested_elements):
        if len(snake_queue) == 0:
            snake_queue = deque(snake_list)
            char = snake_queue.popleft()
            nested_list.append(char)
        else:
            char = snake_queue.popleft()
            nested_list.append(char)
    if nested_list_index % 2 == 0:
        matrix_list.append(nested_list)
    else:
        # nested_list.reverse()
        matrix_list.append(nested_list[::-1])
for nested_list in matrix_list:
    print("".join(nested_list))


# from collections import deque
# info_list = list(map(int, input().split()))
# count_nested_lists = info_list[0]
# count_nested_elements = info_list[1]
# snake_list = list(input())
# snake_queue = deque(snake_list)
# for nested_list_index in range(count_nested_lists):
#     nested_list = []
#     for nested_element_index in range(count_nested_elements):
#         if len(snake_queue) == 0:
#             snake_queue = deque(snake_list)
#             char = snake_queue.popleft()
#             nested_list.append(char)
#         else:
#             char = snake_queue.popleft()
#             nested_list.append(char)
#     if nested_list_index % 2 == 0:
#         print("".join(nested_list))
#     else:
#         nested_list.reverse()
#         print("".join(nested_list))


# from collections import deque
# count_nested_lists, count_nested_elements = list(map(int, input().split()))
# snake_list = list(input())
# snake_queue = deque(snake_list)
# for nested_list_index in range(count_nested_lists):
#     while len(snake_queue) < count_nested_elements:
#         snake_queue.extend(snake_list)
#     if nested_list_index % 2 == 0:
#         nested_list = [snake_queue.popleft() for nested_element_index in range(count_nested_elements)]
#         print("".join(nested_list))
#     else:
#         nested_list = [snake_queue.popleft() for nested_element_index in range(count_nested_elements)]
#         print("".join(nested_list[::-1]))
