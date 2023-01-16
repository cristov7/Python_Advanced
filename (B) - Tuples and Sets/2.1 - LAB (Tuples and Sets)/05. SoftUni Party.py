reservation_vip_guests_set = set()
reservation_regular_guests_set = set()
count_guests = int(input())
for guest in range(1, count_guests + 1):
    reservation_code = input()
    if len(reservation_code) == 8:
        first_char = reservation_code[0]
        if first_char.isdigit():
            reservation_vip_guests_set.add(reservation_code)
        else:
            reservation_regular_guests_set.add(reservation_code)
    else:
        continue
COMMAND_END = "END"
receiving_vip_guest_set = set()
receiving_regular_guest_set = set()
while True:
    guest_code = input()
    if guest_code == COMMAND_END:
        break
    elif guest_code in reservation_vip_guests_set:
        receiving_vip_guest_set.add(guest_code)
    elif guest_code in reservation_regular_guests_set:
        receiving_regular_guest_set.add(guest_code)
    else:
        continue
union_reservation_guests_set = reservation_vip_guests_set.union(reservation_regular_guests_set)
union_receiving_guests_set = receiving_vip_guest_set.union(receiving_regular_guest_set)
missing_guests_set = union_reservation_guests_set.difference(union_receiving_guests_set)
print(len(missing_guests_set))
missing_vip_guests_set = reservation_vip_guests_set.difference(receiving_vip_guest_set)
sorted_missing_vip_guests_list = sorted([guest for guest in missing_vip_guests_set])
for guest in sorted_missing_vip_guests_list:   # for guest in sorted(missing_vip_guests_set):
    print(guest)
missing_regular_guests_set = reservation_regular_guests_set.difference(receiving_regular_guest_set)
sorted_missing_regular_guests_list = sorted([guest for guest in missing_regular_guests_set])
for guest in sorted_missing_regular_guests_list:   # # for guest in sorted(missing_regular_guests_set):
    print(guest)
# for guest in sorted(missing_guests_set):
#     print(guest)


# reservation_guest_set = set()
# count_guests = int(input())
# for guest in range(1, count_guests + 1):
#     reservation = input()
#     reservation_guest_set.add(reservation)
# arrived_guest_set = set()
# while True:
#     guest = input()
#     if guest == "END":
#         break
#     else:
#         arrived_guest_set.add(guest)
# missing_guest_set = reservation_guest_set.difference(arrived_guest_set)
# print(len(missing_guest_set))
# for guest in sorted(missing_guest_set):
#     print(guest)
# # sorted_missing_guest_vip_list = sorted([guest for guest in missing_guest_set if guest[0].isdigit()])
# # for guest in sorted_missing_guest_vip_list:
# #     print(guest)
# # sorted_missing_guest_regular_list = sorted([guest for guest in missing_guest_set if not guest[0].isdigit()])
# # for guest in sorted_missing_guest_regular_list:
# #     print(guest)
