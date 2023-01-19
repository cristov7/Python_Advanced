from collections import deque
bullet_price = int(input())
size_barrel = int(input())
bullets_list = input().split()
bullets_queue = deque([int(item) for item in bullets_list])
org_bullets_queue = deque(bullets_queue)
locks_list = input().split()
locks_queue = deque([int(item) for item in locks_list])
intelligence = int(input())
shoot = 0
while True:
    if len(bullets_queue) > 0 and len(locks_queue) > 0:
        if len(bullets_queue) > 0 and shoot == size_barrel:
            print("Reloading!")
            shoot = 0
        elif bullets_queue[-1] <= locks_queue[0]:
            print("Bang!")
            bullets_queue.pop()
            locks_queue.popleft()
            shoot += 1
        else:
            print("Ping!")
            bullets_queue.pop()
            shoot += 1
    else:
        if len(bullets_queue) > 0 and shoot == size_barrel:
            print("Reloading!")
            shoot = 0
            break
        else:
            break
if len(locks_queue) > 0:
    locks_left = len(locks_queue)
    print(f"Couldn't get through. Locks left: {locks_left}")
else:
    cost = (len(org_bullets_queue) - len(bullets_queue)) * bullet_price
    profit = intelligence - cost
    bullets_left = len(bullets_queue)
    print(f"{bullets_left} bullets left. Earned ${profit}")
