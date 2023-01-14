from collections import deque
quantity_of_food = int(input())
orders_queue = deque(list(map(int, input().split())))
print(max(orders_queue))
while orders_queue:
    order = orders_queue.popleft()
    if order <= quantity_of_food:
        quantity_of_food -= order
    else:
        orders_queue.appendleft(order)
        break
if orders_queue:
    print(f"Orders left:", end=" ")
    print(*orders_queue)
else:
    print("Orders complete")


# from collections import deque
# quantity_of_food = int(input())
# orders_queue = deque([int(order) for order in input().split()])
# print(max(orders_queue))
# for order in orders_queue.copy():
#     if order <= quantity_of_food:
#         orders_queue.popleft()
#         quantity_of_food -= order
#     else:
#         print(f"Orders left: {' '.join([str(order) for order in orders_queue])}")
#         break
# else:
#     print("Orders complete")
