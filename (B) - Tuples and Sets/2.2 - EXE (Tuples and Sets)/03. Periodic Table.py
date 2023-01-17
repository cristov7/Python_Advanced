chemical_elements_set = set()
count_lines = int(input())
for line in range(1, count_lines + 1):
    elements_list = input().split()
    elements_set = {element for element in elements_list}
    chemical_elements_set.update(elements_set)
print(*chemical_elements_set, sep="\n")


# chemical_elements_set = set()
# count_lines = int(input())
# for line in range(1, count_lines + 1):
#     elements_list = input().split()
#     for element in elements_list:
#         chemical_elements_set.add(element)
# print(*chemical_elements_set, sep="\n")


# chemical_elements_list = []
# count_lines = int(input())
# for line in range(1, count_lines + 1):
#     elements_list = input().split()
#     chemical_elements_list.extend(elements_list)
# set_chemical_elements_list = set(chemical_elements_list)
# print("\n".join(set_chemical_elements_list))


# from collections import deque
# chemical_elements_queue = deque()
# count_lines = int(input())
# for line in range(1, count_lines + 1):
#     elements_list = input().split()
#     for element in elements_list:
#         if element not in chemical_elements_queue:
#             chemical_elements_queue.append(element)
#         else:
#             continue
# while chemical_elements_queue:
#     print(chemical_elements_queue.popleft())
