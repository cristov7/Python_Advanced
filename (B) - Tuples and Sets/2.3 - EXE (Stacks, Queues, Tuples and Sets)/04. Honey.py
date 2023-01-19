from collections import deque


def honey_calculation_function(first_number: int, second_number: int, operator: str):
    result = 0
    if operator == "+":
        result = abs(first_number + second_number)
    elif operator == "-":
        result = abs(first_number - second_number)
    elif operator == "*":
        result = abs(first_number * second_number)
    elif operator == "/":
        result = abs(first_number / second_number)
    else:
        raise SystemExit
    return result


def bees_left_function(current_bees_queue: deque):
    bees_list = [str(bee) for bee in current_bees_queue]
    return bees_list


def nectar_left_function(current_nectar_queue: deque):
    nectar_list = [str(nectar) for nectar in current_nectar_queue]
    return nectar_list


working_bees_queue = deque(map(int, input().split()))
nectar_queue = deque(map(int, input().split()))
symbols_queue = deque(input().split())
total_honey = 0
while True:
    if len(working_bees_queue) > 0 and len(nectar_queue) > 0:
        first_bee = working_bees_queue.popleft()
        last_nectar = nectar_queue.pop()
        if last_nectar > first_bee:
            symbol = symbols_queue.popleft()
            honey = honey_calculation_function(first_bee, last_nectar, symbol)
            total_honey += honey
        elif last_nectar < first_bee:
            working_bees_queue.appendleft(first_bee)
        else:
            continue
    else:
        break
print(f"Total honey made: {total_honey}")
if len(working_bees_queue) > 0:
    bees_left_list = bees_left_function(working_bees_queue)
    print(f"Bees left: {', '.join(bees_left_list)}")
if len(nectar_queue) > 0:
    nectar_left_list = nectar_left_function(nectar_queue)
    print(f"Nectar left: {', '.join(nectar_left_list)}")


# from collections import deque
# working_bees_queue = deque(map(int, input().split()))
# nectar_queue = deque(map(int, input().split()))
# symbols_queue = deque(input().split())
# total_honey = 0
# while True:
#     if len(working_bees_queue) > 0 and len(nectar_queue) > 0:
#         first_bee = working_bees_queue.popleft()
#         last_nectar = nectar_queue.pop()
#         if last_nectar > first_bee:
#             symbol = symbols_queue.popleft()
#             honey = 0
#             if symbol == "+":
#                 honey = abs(first_bee + last_nectar)
#             elif symbol == "-":
#                 honey = abs(first_bee - last_nectar)
#             elif symbol == "*":
#                 honey = abs(first_bee * last_nectar)
#             elif symbol == "/":
#                 honey = abs(first_bee / last_nectar)
#             else:
#                 raise SystemExit
#             total_honey += honey
#         elif last_nectar < first_bee:
#             working_bees_queue.appendleft(first_bee)
#         else:
#             continue
#     else:
#         break
# print(f"Total honey made: {total_honey}")
# if len(working_bees_queue) > 0:
#     bees_left_list = [str(bee) for bee in working_bees_queue]
#     print(f"Bees left: {', '.join(bees_left_list)}")
# if len(nectar_queue) > 0:
#     nectar_left_list = [str(nectar) for nectar in nectar_queue]
#     print(f"Nectar left: {', '.join(nectar_left_list)}")
