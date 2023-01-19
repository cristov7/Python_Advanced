from collections import deque


def chocolate_milkshakes_function(chocolate_milkshakes: int):
    if chocolate_milkshakes == 5:
        return "Great! You made all the chocolate milkshakes needed!"
    else:
        return "Not enough milkshakes."


def chocolates_function(chocolates: deque):
    if len(chocolates) > 0:
        return f"Chocolate: {', '.join([str(number) for number in chocolates])}"
    else:
        return "Chocolate: empty"


def milk_function(milk: deque):
    if len(milk) > 0:
        return f"Milk: {', '.join([str(number) for number in milk])}"
    else:
        return "Milk: empty"


chocolates_queue = deque(map(int, input().split(", ")))
cups_of_milk_queue = deque(map(int, input().split(", ")))
count_chocolate_milkshakes = 0
while True:
    if len(chocolates_queue) > 0 and len(cups_of_milk_queue) > 0 and count_chocolate_milkshakes < 5:
        last_chocolate = chocolates_queue[-1]
        first_cup_of_milk = cups_of_milk_queue[0]
        if last_chocolate <= 0 and first_cup_of_milk <= 0:
            chocolates_queue.pop()
            cups_of_milk_queue.popleft()
        elif last_chocolate <= 0:
            chocolates_queue.pop()
        elif first_cup_of_milk <= 0:
            cups_of_milk_queue.popleft()
        else:
            if last_chocolate == first_cup_of_milk:
                chocolates_queue.pop()
                cups_of_milk_queue.popleft()
                count_chocolate_milkshakes += 1
            else:
                chocolates_queue[-1] -= 5
                cup_of_milk = cups_of_milk_queue.popleft()
                cups_of_milk_queue.append(cup_of_milk)
    else:
        break
chocolate_milkshakes_info = chocolate_milkshakes_function(count_chocolate_milkshakes)
print(chocolate_milkshakes_info)
chocolates_info = chocolates_function(chocolates_queue)
print(chocolates_info)
milk_info = milk_function(cups_of_milk_queue)
print(milk_info)


# from collections import deque
# chocolates_queue = deque(map(int, input().split(", ")))
# cups_of_milk_queue = deque(map(int, input().split(", ")))
# count_chocolate_milkshakes = 0
# while True:
#     if len(chocolates_queue) > 0 and len(cups_of_milk_queue) > 0 and count_chocolate_milkshakes < 5:
#         last_chocolate = chocolates_queue[-1]
#         first_cup_of_milk = cups_of_milk_queue[0]
#         if last_chocolate <= 0 and first_cup_of_milk <= 0:
#             chocolates_queue.pop()
#             cups_of_milk_queue.popleft()
#         elif last_chocolate <= 0:
#             chocolates_queue.pop()
#         elif first_cup_of_milk <= 0:
#             cups_of_milk_queue.popleft()
#         else:
#             if last_chocolate == first_cup_of_milk:
#                 chocolates_queue.pop()
#                 cups_of_milk_queue.popleft()
#                 count_chocolate_milkshakes += 1
#             else:
#                 chocolates_queue[-1] -= 5
#                 cup_of_milk = cups_of_milk_queue.popleft()
#                 cups_of_milk_queue.append(cup_of_milk)
#     else:
#         break
# if count_chocolate_milkshakes == 5:
#     print("Great! You made all the chocolate milkshakes needed!")
# else:
#     print("Not enough milkshakes.")
# if len(chocolates_queue) > 0:
#     print(f"Chocolate: {', '.join([str(number) for number in chocolates_queue])}")
# else:
#     print("Chocolate: empty")
# if len(cups_of_milk_queue) > 0:
#     print(f"Milk: {', '.join([str(number) for number in cups_of_milk_queue])}")
# else:
#     print("Milk: empty")
