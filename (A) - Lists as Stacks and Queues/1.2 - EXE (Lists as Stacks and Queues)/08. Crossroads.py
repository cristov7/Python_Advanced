from collections import deque
green_window_time = int(input())
free_window_time = int(input())
cars_queue = deque()
total_cars = 0
COMMAND_END = "END"
while True:
    command = input()
    if command == COMMAND_END:
        break
    elif command == "green":
        current_green_time = green_window_time
        while current_green_time > 0 and cars_queue:
            current_car = cars_queue.popleft()
            length_current_car = len(current_car)
            time = current_green_time + free_window_time
            if length_current_car > time:
                print("A crash happened!")
                index = time
                character_hit = current_car[index]
                print(f"{current_car} was hit at {character_hit}.")
                raise SystemExit
            else:
                current_green_time -= length_current_car
                total_cars += 1
    else:
        car_model = command
        cars_queue.append(car_model)
print("Everyone is safe.")
print(f"{total_cars} total cars passed the crossroads.")
