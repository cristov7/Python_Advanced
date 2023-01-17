lengths_tuple = tuple(map(int, input().split()))
length_of_first_set = lengths_tuple[0]
length_of_second_set = lengths_tuple[1]
first_set = set()
second_set = set()
for number in range(1, length_of_first_set + 1):
    current_number = int(input())
    first_set.add(current_number)
for number in range(1, length_of_second_set + 1):
    current_number = int(input())
    second_set.add(current_number)
intersection_set = first_set.intersection(second_set)
print(*intersection_set, sep="\n")


# length_of_first_set, length_of_second_set = input().split()
# first_set = {int(input()) for number in range(int(length_of_first_set))}
# second_set = {int(input()) for number in range(int(length_of_second_set))}
# intersection_set = first_set.intersection(second_set)
# print(*intersection_set, sep="\n")


# def creating_set_function(length_of_elements: int):
#     current_set = set()
#     for element in range(length_of_elements):
#         current_element = input()
#         current_set.add(current_element)
#     return current_set
#
#
# def intersection_set_function(set_one: set, set_two: set):
#     current_intersection_set = set_one.intersection(set_two)
#     return current_intersection_set
#
#
# lengths_tuple = tuple(map(int, input().split()))
# length_of_first_set = lengths_tuple[0]
# length_of_second_set = lengths_tuple[1]
# first_set = creating_set_function(length_of_first_set)
# second_set = creating_set_function(length_of_second_set)
# intersection_set = intersection_set_function(first_set, second_set)
# print(*intersection_set, sep="\n")
