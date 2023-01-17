def unique_names_function(number_of_names: int):
    names_in_set = set()
    for name in range(1, number_of_names + 1):
        current_name = input()
        names_in_set.add(current_name)
    return names_in_set


count_names = int(input())
names_set = unique_names_function(count_names)
print("\n".join(names_set))


# names_set = set()
# count_names = int(input())
# for name in range(1, count_names + 1):
#     current_name = input()
#     names_set.add(current_name)
# for name in names_set:
#     print(name)


# from collections import deque
# names_queue = deque()
# count_names = int(input())
# for name in range(1, count_names + 1):
#     current_name = input()
#     if current_name not in names_queue:
#         names_queue.append(current_name)
#     else:
#         continue
# while names_queue:
#     print(names_queue.popleft())


# print("\n".join({input() for name in range(int(input()))}))


# print(*{input() for name in range(int(input()))}, sep="\n")
