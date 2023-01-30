from collections import deque


def math_operations(*args, **kwargs):
    numbers_queue = deque(args)
    dictionary = dict(kwargs)
    counter = 0
    while numbers_queue:
        counter += 1
        number = numbers_queue.popleft()
        if counter == 1:
            dictionary["a"] += number
        elif counter == 2:
            dictionary["s"] -= number
        elif counter == 3:
            if number != 0:
                dictionary["d"] /= number
            else:
                continue
        elif counter == 4:
            dictionary["m"] *= number
            counter = 0
    sorted_dictionary = dict(sorted(dictionary.items(), key=lambda x: (-x[1], x[0])))
    info_list = []
    for letter, value in sorted_dictionary.items():
        info = f"{letter}: {value:.1f}"
        info_list.append(info)
    return "\n".join(info_list)


# print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
# # print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
# # print(math_operations(6.0, a=0, s=0, d=5, m=0))


# def math_operations(*args, **kwargs):
#     numbers_list = list(args)
#     dictionary = dict(kwargs)
#     for index, number in enumerate(numbers_list):
#         letter = list(dictionary.keys())[index % 4]
#         if letter == "a":
#             dictionary[letter] += number
#         elif letter == "s":
#             dictionary[letter] -= number
#         elif letter == "d":
#             if number != 0:
#                 dictionary[letter] /= number
#             else:
#                 continue
#         elif letter == "m":
#             dictionary[letter] *= number
#         else:
#             continue
#     sorted_dictionary = dict(sorted(dictionary.items(), key=lambda x: (-x[1], x[0])))
#     info_list = []
#     for letter, value in sorted_dictionary.items():
#         info = f"{letter}: {value:.1f}"
#         info_list.append(info)
#     return "\n".join(info_list)
#
#
# print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
# # print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
# # print(math_operations(6.0, a=0, s=0, d=5, m=0))
