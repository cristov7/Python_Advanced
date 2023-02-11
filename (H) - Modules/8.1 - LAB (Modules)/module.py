def return_triangle_function(size: int):
    triangle = ""
    for line in range(1, size + 1):
        last_number = line
        for number in range(1, last_number + 1):
            triangle += f"{number} "
        triangle += "\n"
    for line in range(size - 1, 0, - 1):
        last_number = line
        for number in range(1, last_number + 1):
            triangle += f"{number} "
        triangle += "\n"
    return triangle


def return_calculation_function(a: float, operation: str, b: int):
    def return_divide_function():
        if b != 0:
            divide = a / b
            return f"{divide:.2f}"
        else:
            raise SystemExit("Can not divide by zero!")

    def return_multiply_function():
        multiply = a * b
        return f"{multiply:.2f}"

    def return_subtract_function():
        subtract = a - b
        return f"{subtract:.2f}"

    def return_add_function():
        add = a + b
        return f"{add:.2f}"

    def return_raise_function():
        degree = a ** b
        return f"{degree:.2f}"

    if operation == "/":
        calculation = return_divide_function()
        return calculation
    elif operation == "*":
        calculation = return_multiply_function()
        return calculation
    elif operation == "-":
        calculation = return_subtract_function()
        return calculation
    elif operation == "+":
        calculation = return_add_function()
        return calculation
    elif operation == "^":
        calculation = return_raise_function()
        return calculation
    else:
        raise SystemExit("Invalid operation!")


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


def create_sequence_function(count_numbers: int):
    numbers_list = []
    for count_number in range(1, count_numbers + 1):
        if count_number == 1:
            current_number = 0
            numbers_list.append(current_number)
        elif count_number == 2:
            current_number = 1
            numbers_list.append(current_number)
        else:
            last_number = numbers_list[-1]
            pre_last_number = numbers_list[-2]
            current_number = last_number + pre_last_number
            numbers_list.append(current_number)
    return numbers_list


def locate_function(search_number: int, numbers_list: list):
    if search_number in numbers_list:
        index = numbers_list.index(search_number)
        return f"The number - {search_number} is at index {index}"
    else:
        return f"The number {search_number} is not in the sequence"
