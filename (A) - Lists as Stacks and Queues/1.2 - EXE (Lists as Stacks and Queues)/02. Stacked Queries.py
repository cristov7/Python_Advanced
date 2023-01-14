stack = []
count_queries = int(input())
for query in range(1, count_queries + 1):
    current_query = input()
    if current_query.isdigit():
        command = int(current_query)
        if command == 2:
            if len(stack) > 0:
                stack.pop()
            else:
                continue
        elif command == 3:
            if len(stack) > 0:
                max_number = max(stack)
                print(max_number)
            else:
                continue
        elif command == 4:
            if len(stack) > 0:
                min_number = min(stack)
                print(min_number)
            else:
                continue
        else:
            continue
    else:
        info_list = current_query.split()
        command = int(info_list[0])
        if command == 1:
            number = int(info_list[1])
            stack.append(number)
        else:
            continue
reverse_stack = stack[::-1]
print(*reverse_stack, sep=", ")


# from collections import deque
# numbers = deque()
# command_dict = {
#     1: lambda x: numbers.append(x[1]),
#     2: lambda x: numbers.pop() if numbers else None,
#     3: lambda x: print(max(numbers)) if numbers else None,
#     4: lambda x: print(min(numbers)) if numbers else None
# }
# count_commands = int(input())
# for command in range(1, count_commands + 1):
#     command_list = [int(number) for number in input().split()]
#     command_dict[command_list[0]](command_list)
# numbers.reverse()
# print(*numbers, sep=", ")
