from module import return_calculation_function


# def return_calculation_function(a: float, operation: str, b: int):
#     def return_divide_function():
#         if b != 0:
#             divide = a / b
#             return f"{divide:.2f}"
#         else:
#             raise SystemExit("Can not divide by zero!")
#
#     def return_multiply_function():
#         multiply = a * b
#         return f"{multiply:.2f}"
#
#     def return_subtract_function():
#         subtract = a - b
#         return f"{subtract:.2f}"
#
#     def return_add_function():
#         add = a + b
#         return f"{add:.2f}"
#
#     def return_raise_function():
#         degree = a ** b
#         return f"{degree:.2f}"
#
#     if operation == "/":
#         calculation = return_divide_function()
#         return calculation
#     elif operation == "*":
#         calculation = return_multiply_function()
#         return calculation
#     elif operation == "-":
#         calculation = return_subtract_function()
#         return calculation
#     elif operation == "+":
#         calculation = return_add_function()
#         return calculation
#     elif operation == "^":
#         calculation = return_raise_function()
#         return calculation
#     else:
#         raise SystemExit("Invalid operation!")


math_list = input().split()
first_number = float(math_list[0])
sign = math_list[1]
second_number = int(math_list[2])
result = return_calculation_function(first_number, sign, second_number)
print(result)


# import operator
#
#
# def mathematical_operations(first_number, option, second_number):
#     first_number, second_number = int(first_number), int(second_number)
#     calculation_dict = {"/": operator.truediv(first_number, second_number),
#                         "*": operator.mul(first_number, second_number),
#                         "-": operator.sub(first_number, second_number),
#                         "+": operator.add(first_number, second_number),
#                         "^": operator.xor(first_number, second_number)}
#     return calculation_dict[option]
#
#
# data = mathematical_operations(*input().split())
# print(f"{data:.2f}")
