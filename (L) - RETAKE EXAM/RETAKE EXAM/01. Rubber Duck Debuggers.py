from collections import deque
time_per_task_queue = deque(map(int, input().split()))
number_of_tasks_queue = deque(map(int, input().split()))
rubber_ducks_info_dict = {"Darth Vader Ducky": [0, 60],
                          "Thor Ducky": [61, 120],
                          "Big Blue Rubber Ducky": [121, 180],
                          "Small Yellow Rubber Ducky": [181, 240]}
count_rubber_ducks_dict = {"Darth Vader Ducky": 0,
                           "Thor Ducky": 0,
                           "Big Blue Rubber Ducky": 0,
                           "Small Yellow Rubber Ducky": 0}
complete = False
while True:
    if not time_per_task_queue and not number_of_tasks_queue:
        break
    else:
        time = time_per_task_queue.popleft()
        task = number_of_tasks_queue.pop()
        current_time = time * task
        for rubber_ducky_type, time_needed_to_earn_it_list in rubber_ducks_info_dict.items():
            min_time = time_needed_to_earn_it_list[0]
            max_time = time_needed_to_earn_it_list[1]
            if min_time <= current_time <= max_time:
                count_rubber_ducks_dict[rubber_ducky_type] += 1
                complete = True
                break
            else:
                continue
        if complete:
            complete = False
        else:
            time_per_task_queue.append(time)
            task -= 2
            number_of_tasks_queue.append(task)
print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for rubber_ducky_type, count in count_rubber_ducks_dict.items():
    print(f"{rubber_ducky_type}: {count}")
