numbers_list = list(map(int, input().split()))
target_number = int(input())
targets_set = set()
numbers_dict = {}
for number in numbers_list:
    if number in targets_set:
        targets_set.remove(number)
        pair = numbers_dict[number]
        del numbers_dict[number]
        print(f"{pair} + {number} = {target_number}")
    else:
        resulting_number = target_number - number
        targets_set.add(resulting_number)
        numbers_dict[resulting_number] = number


# numbers_list = list(map(int, input().split()))
# target_number = int(input())
# for i in range(len(numbers_list)):
#     if numbers_list[i] == "":
#         continue
#     for j in range(i + 1, len(numbers_list)):
#         if numbers_list[j] == "":
#             continue
#         if numbers_list[i] + numbers_list[j] == target_number:
#             first_number = numbers_list[i]
#             second_number = numbers_list[j]
#             print(f"{first_number} + {second_number} = {target_number}")
#             numbers_list[i] = ""
#             numbers_list[j] = ""
#             break
