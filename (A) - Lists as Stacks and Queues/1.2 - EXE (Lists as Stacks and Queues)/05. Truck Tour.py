from collections import deque
pumps_queue = deque(list(map(int, input().split())) for _ in range(int(input())))
new_pumps_queue = pumps_queue.copy()
index = 0
tank = 0
while new_pumps_queue:
    amount_of_petrol, distance_from_that_petrol_pump = new_pumps_queue.popleft()
    tank += amount_of_petrol
    if distance_from_that_petrol_pump > tank:
        pumps_queue.rotate(-1)
        new_pumps_queue = pumps_queue.copy()
        index += 1
        tank = 0
    else:
        tank -= distance_from_that_petrol_pump
print(index)
