def func_executor(*functions_info_in_tuples):
    result_list = []
    for function_name, values_in_tuple in functions_info_in_tuples:
        operation = function_name.__name__
        calculation = function_name(*values_in_tuple)
        result = f"{operation} - {calculation}"
        result_list.append(result)
    return "\n".join(result_list)


# def func_executor(*functions):
#     result_list = []
#     for func, args in functions:
#         result_list.append(f"{func.__name__} - {func(*args)}")
#     return "\n".join(result_list)


# def func_executor(*functions):
#     result_list = [f"{func.__name__} - {func(*args)}" for func, args in functions]
#     return "\n".join(result_list)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


# print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))


# def func_executor(*functions):
#     result_list = [f"{func.__name__} - {func(*args)}" for func, args in functions]
#     return "\n".join(result_list)
#
#
# def make_upper(*strings):
#     result = tuple(s.upper() for s in strings)
#     return result
#
#
# def make_lower(*strings):
#     result = tuple(s.lower() for s in strings)
#     return result
#
#
# # print(func_executor((make_upper, ("Python", "softUni")), (make_lower, ("PyThOn",)),))

