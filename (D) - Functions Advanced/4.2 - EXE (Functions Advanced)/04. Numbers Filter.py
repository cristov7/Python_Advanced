def even_odd_filter(**kwargs):
    def even_function(lst):
        even_numbers_list = [element for element in lst if element % 2 == 0]
        return even_numbers_list

    def odd_function(lst):
        odd_numbers_list = [element for element in lst if element % 2]
        return odd_numbers_list

    def merge_function(dict_1, dict_2):
        dict_1.update(dict_2)
        return dict_1

    even_dict = {}
    odd_dict = {}
    for key, values_list in kwargs.items():
        if key == "even":
            even_list = even_function(values_list)
            even_dict[key] = even_list
        elif key == "odd":
            odd_list = odd_function(values_list)
            odd_dict[key] = odd_list
        else:
            continue
    numbers_dict = merge_function(even_dict, odd_dict)
    sorted_dict = dict(sorted(numbers_dict.items(), key=lambda x: (-len(x[1]))))
    return sorted_dict


# print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5], even=[3, 4, 5, 7, 10, 2, 5, 5, 2],))
# # print(even_odd_filter(odd=[2, 2, 30, 44, 10, 5],))


# def even_odd_filter(**kwargs):
#     for key, values_list in kwargs.items():
#         if key == "even":
#             values_list = list(filter(lambda x: x % 2 == 0, kwargs["even"]))
#             kwargs["even"] = values_list
#         elif key == "odd":
#             values_list = list(filter(lambda x: x % 2, kwargs["odd"]))
#             kwargs["odd"] = values_list
#         else:
#             raise SystemExit
#     sorted_dict = dict(sorted(kwargs.items(), key=lambda x: (-len(x[1]))))
#     return sorted_dict
#
#
# print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5], even=[3, 4, 5, 7, 10, 2, 5, 5, 2],))
# # print(even_odd_filter(odd=[2, 2, 30, 44, 10, 5],))
