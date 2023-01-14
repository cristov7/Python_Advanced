from collections import deque
clothes_from_box_queue = deque(list(map(int, input().split())))
max_capacity_per_rack = int(input())
free_capacity_in_current_rack = max_capacity_per_rack
count_racks = 1
while clothes_from_box_queue:
    cloth = clothes_from_box_queue.pop()
    if cloth <= free_capacity_in_current_rack:
        free_capacity_in_current_rack -= cloth
    else:
        count_racks += 1
        free_capacity_in_current_rack = max_capacity_per_rack
        free_capacity_in_current_rack -= cloth
print(count_racks)
