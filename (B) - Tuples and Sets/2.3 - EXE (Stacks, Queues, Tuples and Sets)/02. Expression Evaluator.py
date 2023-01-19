from collections import deque
from math import floor


def multiplication_function(queue: deque):
    while True:
        if len(queue) > 1:
            first_number = queue.popleft()
            second_number = queue.popleft()
            result = first_number * second_number
            queue.appendleft(result)
        else:
            break
    return queue


def gathering_function(queue: deque):
    while True:
        if len(queue) > 1:
            first_number = queue.popleft()
            second_number = queue.popleft()
            result = first_number + second_number
            queue.appendleft(result)
        else:
            break
    return queue


def subtraction_function(queue: deque):
    while True:
        if len(queue) > 1:
            first_number = queue.popleft()
            second_number = queue.popleft()
            result = first_number - second_number
            queue.appendleft(result)
        else:
            break
    return queue


def division_function(queue: deque):
    while True:
        if len(queue) > 1:
            first_number = queue.popleft()
            second_number = queue.popleft()
            result = floor(first_number / second_number)
            queue.appendleft(result)
        else:
            break
    return queue


numbers_queue = deque()
string_expression = input()
expression_list = string_expression.split()
for element in expression_list:
    if element == "*":
        numbers_queue = multiplication_function(numbers_queue)
    elif element == "+":
        numbers_queue = gathering_function(numbers_queue)
    elif element == "-":
        numbers_queue = subtraction_function(numbers_queue)
    elif element == "/":
        numbers_queue = division_function(numbers_queue)
    else:
        number = int(element)
        numbers_queue.append(number)
print(numbers_queue.popleft())


# from collections import deque
# from math import floor
# numbers_queue = deque()
# string_expression = input()
# expression_list = string_expression.split()
# for element in expression_list:
#     if element == "*":
#         while True:
#             if len(numbers_queue) > 1:
#                 first_number = numbers_queue.popleft()
#                 second_number = numbers_queue.popleft()
#                 result = first_number * second_number
#                 numbers_queue.appendleft(result)
#             else:
#                 break
#     elif element == "+":
#         while True:
#             if len(numbers_queue) > 1:
#                 first_number = numbers_queue.popleft()
#                 second_number = numbers_queue.popleft()
#                 result = first_number + second_number
#                 numbers_queue.appendleft(result)
#             else:
#                 break
#     elif element == "-":
#         while True:
#             if len(numbers_queue) > 1:
#                 first_number = numbers_queue.popleft()
#                 second_number = numbers_queue.popleft()
#                 result = first_number - second_number
#                 numbers_queue.appendleft(result)
#             else:
#                 break
#     elif element == "/":
#         while True:
#             if len(numbers_queue) > 1:
#                 first_number = numbers_queue.popleft()
#                 second_number = numbers_queue.popleft()
#                 result = floor(first_number / second_number)
#                 numbers_queue.appendleft(result)
#             else:
#                 break
#     else:
#         number = int(element)
#         numbers_queue.append(number)
# print(numbers_queue.popleft())
