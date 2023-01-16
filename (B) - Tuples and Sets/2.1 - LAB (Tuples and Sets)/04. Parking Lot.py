parking_set = set()
DIRECTION_IN = "IN"
DIRECTION_OUT = "OUT"
count_commands = int(input())
for command in range(1, count_commands + 1):
    current_command = input()
    command_list = current_command.split(", ")
    direction = command_list[0]
    car_number = command_list[1]
    if direction == DIRECTION_IN:
        parking_set.add(car_number)
    elif direction == DIRECTION_OUT:
        if car_number in parking_set:
            parking_set.remove(car_number)
        else:
            continue
    else:
        continue
if len(parking_set) == 0:
    print("Parking Lot is Empty")
else:
    for car_number in parking_set:
        print(car_number)


# parking_list = []
# count_commands = int(input())
# for command in range(1, count_commands + 1):
#     direction, car_number = input().split(", ")
#     if direction == "IN":
#         parking_list.append(car_number)
#     elif direction == "OUT":
#         if car_number in parking_list:
#             parking_list.remove(car_number)
#         else:
#             continue
#     else:
#         continue
# parking_set = {car_number for car_number in parking_list}
# if len(parking_set) == 0:
#     print("Parking Lot is Empty")
# else:
#     for car_number in parking_set:
#         print(car_number)
