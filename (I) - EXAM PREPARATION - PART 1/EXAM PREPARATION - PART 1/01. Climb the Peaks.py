from collections import deque


def climb_the_peaks_function():
    food_portions_queue = deque(map(int, input().split(", ")))
    stamina_queue = deque(map(int, input().split(", ")))
    mountain_peaks_queue = deque([("Vihren", 80), ("Kutelo", 90), ("Banski Suhodol", 100), ("Polezhan", 60), ("Kamenitza", 70)])
    conquered_peaks_queue = deque()
    days = 7
    for day in range(1, days + 1):
        if food_portions_queue and stamina_queue and mountain_peaks_queue:
            food = food_portions_queue.pop()
            stamina = stamina_queue.popleft()
            calculate = food + stamina
            peaks_tuple = mountain_peaks_queue.popleft()
            difficulty_level = peaks_tuple[1]
            if calculate >= difficulty_level:
                mountain_peaks = peaks_tuple[0]
                conquered_peaks_queue.append(mountain_peaks)
            else:
                mountain_peaks_queue.appendleft(peaks_tuple)
        else:
            break
    if mountain_peaks_queue:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
    else:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
    if conquered_peaks_queue:
        print("Conquered peaks:")
        while conquered_peaks_queue:
            mountain_peaks = conquered_peaks_queue.popleft()
            print(mountain_peaks)
    else:
        raise SystemExit


climb_the_peaks_function()


# from collections import deque
# food_portions_queue = deque(map(int, input().split(", ")))
# stamina_queue = deque(map(int, input().split(", ")))
# mountain_peaks_queue = deque([("Vihren", 80), ("Kutelo", 90), ("Banski Suhodol", 100), ("Polezhan", 60), ("Kamenitza", 70)])
# conquered_peaks_queue = deque()
# days = 7
# for day in range(1, days + 1):
#     if food_portions_queue and stamina_queue and mountain_peaks_queue:
#         food = food_portions_queue.pop()
#         stamina = stamina_queue.popleft()
#         calculate = food + stamina
#         peaks_tuple = mountain_peaks_queue.popleft()
#         difficulty_level = peaks_tuple[1]
#         if calculate >= difficulty_level:
#             mountain_peaks = peaks_tuple[0]
#             conquered_peaks_queue.append(mountain_peaks)
#         else:
#             mountain_peaks_queue.appendleft(peaks_tuple)
#     else:
#         break
# if mountain_peaks_queue:
#     print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
# else:
#     print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
# if conquered_peaks_queue:
#     print("Conquered peaks:")
#     while conquered_peaks_queue:
#         mountain_peaks = conquered_peaks_queue.popleft()
#         print(mountain_peaks)
# else:
#     raise SystemExit
