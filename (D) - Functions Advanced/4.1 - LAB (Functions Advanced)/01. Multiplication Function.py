def multiply(*args):
    numbers_tuple = args
    multiply_number = 1
    for number in numbers_tuple:
        multiply_number *= number
    return multiply_number


# print(multiply(1, 4, 5))
# print(multiply(4, 5, 6, 1, 3))
# print(multiply(2, 0, 1000, 5000))


# from functools import reduce
#
#
# def multiply(*args):
#     return reduce(lambda x, y: x * y, args)
#
#
# # print(multiply(1, 4, 5))
# # print(multiply(4, 5, 6, 1, 3))
# # print(multiply(2, 0, 1000, 5000))
