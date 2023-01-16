names_list = []
count_names = int(input())
for name in range(1, count_names + 1):
    current_name = input()
    names_list.append(current_name)
unique_names_comprehension_set = {name for name in names_list}
for name in unique_names_comprehension_set:
    print(name)


# names_list = []
# count_names = int(input())
# for name in range(1, count_names + 1):
#     current_name = input()
#     names_list.append(current_name)
# unique_names_comprehension_set = {name for name in names_list}
# while unique_names_comprehension_set:
#     print(unique_names_comprehension_set.pop())


# unique_names_comprehension_set = {input() for name in range(1, int(input()) + 1)}
# for name in unique_names_comprehension_set:
#     print(name)


# unique_names_comprehension_set = {input() for name in range(1, int(input()) + 1)}
# while unique_names_comprehension_set:
#     print(unique_names_comprehension_set.pop())


# unique_names_comprehension_set = {input() for name in range(1, int(input()) + 1)}
# [print(name) for name in unique_names_comprehension_set]
