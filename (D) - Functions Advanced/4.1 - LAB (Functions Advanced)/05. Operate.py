def operate(operator, *numbers_tuple):
    def addition():
        result = sum(numbers_tuple)
        return result

    def subtraction():
        first_number = numbers_tuple[0]
        other_numbers_tuple = numbers_tuple[1:]
        result = first_number
        for number in other_numbers_tuple:
            result -= number
        return result

    def multiplication():
        result = 1
        for number in numbers_tuple:
            result *= number
        return result

    def division():
        first_number = numbers_tuple[0]
        other_numbers_tuple = numbers_tuple[1:]
        if 0 in other_numbers_tuple:
            raise SystemExit("Can't divide by zero!")
        else:
            result = first_number
            for number in other_numbers_tuple:
                result /= number
            return result

    if operator == "+":
        return addition()
    elif operator == "-":
        return subtraction()
    elif operator == "*":
        return multiplication()
    elif operator == "/":
        return division()
    else:
        raise SystemExit("Invalid operator!")


# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))


# from functools import reduce
#
#
# def operate(operator, *numbers_tuple):
#     def add():
#         return reduce(lambda x, y: x + y, numbers_tuple)
#
#     def subtract():
#         return reduce(lambda x, y: x - y, numbers_tuple)
#
#     def multiply():
#         return reduce(lambda x, y: x * y, numbers_tuple)
#
#     def division():
#         return reduce(lambda x, y: x / y, numbers_tuple)
#
#     if operator == "+":
#         return add()
#     elif operator == "-":
#         return subtract()
#     elif operator == "*":
#         return multiply()
#     elif operator == "/":
#         return division()
#     else:
#         raise SystemExit("Invalid operator!")
#
#
# # print(operate("+", 1, 2, 3))
# # print(operate("*", 3, 4))
