stack = list(map(int, input().split()))
while stack:
    print(stack.pop(), end=" ")


# from collections import deque
# queue = deque(input().split())
# queue.reverse()
# print(" ".join(queue))


# numbers_list = [int(number) for number in input().split()]
# stack = numbers_list[::-1]
# print(*stack)


# print(*input().split()[::-1], sep=" ")
