from collections import deque
from datetime import datetime, timedelta
robots_info_queue = deque(input().split(";"))
robots_dict = {}
for robot in robots_info_queue:
    robot_list = robot.split("-")
    robot_name = robot_list[0]
    processing_time = int(robot_list[1])
    time_work = 0
    robots_dict[robot_name] = [processing_time, time_work]
factory_time = datetime.strptime(input(), "%H:%M:%S")
products_queue = deque()
COMMAND_END = "End"
while True:
    product = input()
    if product == COMMAND_END:
        break
    else:
        products_queue.append(product)
while products_queue:
    factory_time += timedelta(0, 1)
    product = products_queue.popleft()
    free_robots_list = []
    for robot_name, info_list in robots_dict.items():
        processing_time = info_list[0]
        time_work = info_list[1]
        if time_work != 0:
            robots_dict[robot_name][1] -= 1
        else:
            continue
    for robot_name, info_list in robots_dict.items():
        processing_time = info_list[0]
        time_work = info_list[1]
        if time_work == 0:
            free_robots_list.append([robot_name, info_list])
        else:
            continue
    if not free_robots_list:
        products_queue.append(product)
    else:
        robot_name, info_list = free_robots_list[0]
        robots_dict[robot_name][1] = info_list[0]
        print(f"{robot_name} - {product} [{factory_time.strftime('%H:%M:%S')}]")
