from collections import deque
players_deque = deque(input().split())
count_toss = int(input())
counter = 0
while True:
    if len(players_deque) == 1:
        winner = players_deque.popleft()
        print(f"Last is {winner}")
        break
    else:
        counter += 1
        player = players_deque.popleft()
        if counter == count_toss:
            print(f"Removed {player}")
            counter = 0
        else:
            players_deque.append(player)


# from collections import deque
# names_deque = deque(input().split())
# counter = int(input())
# while len(names_deque) > 1:
#     for player in range(1, counter):
#         name = names_deque.popleft()
#         names_deque.append(name)
#     current_name = names_deque.popleft()
#     print(f"Removed {current_name}")
# winner = names_deque.pop()
# print(f"Last is {winner}")


# names_list = input().split()
# removed_list = []
# count_toss = int(input())
# toss = 0
# stop = False
# while names_list:
#     if stop:
#         break
#     else:
#         for index, kid in enumerate(names_list):
#             if kid in removed_list:
#                 continue
#             else:
#                 toss += 1
#                 if toss == count_toss:
#                     if len(names_list) - len(removed_list) == 1:
#                         winner = ""
#                         for player in names_list:
#                             if player not in removed_list:
#                                 winner = player
#                                 break
#                             else:
#                                 continue
#                         print(f"Last is {winner}")
#                         stop = True
#                         break
#                     print(f"Removed {kid}")
#                     removed_list.append(kid)
#                     toss = 0
#                 else:
#                     continue
