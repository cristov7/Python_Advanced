count_same_values_dict = {}
numbers_tuple = tuple(map(float, input().split()))
for number in numbers_tuple:
    if number not in count_same_values_dict.keys():
        count_same_values_dict[number] = 1
    else:
        count_same_values_dict[number] += 1
for number, count in count_same_values_dict.items():
    print(f"{number} - {count} times")


# count_same_values_dict = {}
# numbers_tuple = tuple(map(float, input().split()))
# for number in numbers_tuple:
#     if number not in count_same_values_dict.keys():
#         count = numbers_tuple.count(number)
#         result = f"{number} - {count} times"
#         count_same_values_dict[number] = result
#     else:
#         continue
# for result in count_same_values_dict.values():
#     print(result)


# result_list = []
# numbers_tuple = tuple(map(float, input().split()))
# for number in numbers_tuple:
#     count = numbers_tuple.count(number)
#     result = f"{number} - {count} times"
#     if result not in result_list:
#         result_list.append(result)
#         print(result)
#     else:
#         continue


# numbers_tuple = tuple(map(float, input().split()))
# numbers_dict = {number: numbers_tuple.count(number) for number in numbers_tuple}
# [print(f"{number} - {count} times") for number, count in numbers_dict.items()]
