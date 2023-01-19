from collections import deque
cups_queue = deque(int(cup) for cup in input().split())
bottles_queue = deque(int(bottle) for bottle in input().split())
wasted_water = 0
while True:
    if len(cups_queue) > 0 and len(bottles_queue) > 0:
        current_cup = cups_queue.popleft()
        current_bottle = bottles_queue.pop()
        if current_bottle >= current_cup:
            water = current_bottle - current_cup
            wasted_water += water
        else:
            water = current_cup - current_bottle
            cups_queue.appendleft(water)
    else:
        break
if len(cups_queue) > 0:
    cups_list = [str(cup) for cup in cups_queue]
    print(f"Cups: {' '.join(cups_list)}")
if len(bottles_queue) > 0:
    bottles_list = [str(bottle) for bottle in bottles_queue]
    print(f"Bottles: {' '.join(bottles_list)}")
print(f"Wasted litters of water: {wasted_water}")
