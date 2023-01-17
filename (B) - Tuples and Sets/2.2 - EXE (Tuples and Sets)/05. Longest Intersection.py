def creating_set_function(range_list: list):
    start = int(range_list[0])
    end = int(range_list[1])
    current_set = {number for number in range(start, end + 1)}
    return current_set


longest_intersection_list = []
longest_length = 0
count_ranges = int(input())
for number_range in range(1, count_ranges + 1):
    current_range_list = input().split("-")
    first_range = current_range_list[0]
    first_range_list = first_range.split(",")
    first_set = creating_set_function(first_range_list)
    second_range = current_range_list[1]
    second_range_list = second_range.split(",")
    second_set = creating_set_function(second_range_list)
    intersection_list = list(first_set.intersection(second_set))
    length = len(intersection_list)
    if length > longest_length:
        longest_intersection_list = intersection_list
        longest_length = length
    else:
        continue
print(f"Longest intersection is {longest_intersection_list} with length {longest_length}")


# longest_intersection_list = []
# longest_length = 0
# count_ranges = int(input())
# for number_range in range(1, count_ranges + 1):
#     first_range_list, second_range_list = [current_range.split(",") for current_range in input().split("-")]
#     first_set = {number for number in range(int(first_range_list[0]), int(first_range_list[1]) + 1)}
#     second_set = {number for number in range(int(second_range_list[0]), int(second_range_list[1]) + 1)}
#     intersection_list = list(first_set.intersection(second_set))
#     length = len(intersection_list)
#     if length > longest_length:
#         longest_intersection_list = intersection_list
#         longest_length = length
#     else:
#         continue
# print(f"Longest intersection is {longest_intersection_list} with length {longest_length}")


# intersection_dict = {}
# count_ranges = int(input())
# for number_range in range(1, count_ranges + 1):
#     current_range_list = input().split("-")
#     first_range = current_range_list[0]
#     first_range_list = first_range.split(",")
#     first_start = int(first_range_list[0])
#     first_end = int(first_range_list[1])
#     first_set = {number for number in range(first_start, first_end + 1)}
#     second_range = current_range_list[1]
#     second_range_list = second_range.split(",")
#     second_start = int(second_range_list[0])
#     second_end = int(second_range_list[1])
#     second_set = {number for number in range(second_start, second_end + 1)}
#     intersection_set = first_set.intersection(second_set)
#     intersection_list = [number for number in intersection_set]
#     length = len(intersection_list)
#     if length not in intersection_dict.keys():
#         intersection_dict[length] = intersection_list
#     else:
#         continue
# sorted_intersection_list = sorted(intersection_dict.items(), key=lambda key: key[0], reverse=True)
# for sorted_tuple in sorted_intersection_list:
#     longest_length = sorted_tuple[0]
#     longest_list = sorted_tuple[1]
#     print(f"Longest intersection is {longest_list} with length {longest_length}")
#     break
