from collections import deque
sequence_of_parentheses_queue = deque(input())
parentheses_stack = []
parentheses_dict = {
    "(": ")",
    "{": "}",
    "[": "]"
}
balanced = True
for parentheses in sequence_of_parentheses_queue:
    if parentheses == "(" or parentheses == "{" or parentheses == "[":
        open_parentheses = parentheses
        parentheses_stack.append(open_parentheses)
        balanced = False
    elif parentheses == ")" or parentheses == "}" or parentheses == "]":
        if parentheses_stack:
            open_parentheses = parentheses_stack.pop()
            close_parentheses = parentheses
            if parentheses_dict[open_parentheses] == close_parentheses:
                if len(parentheses_stack) == 0:
                    balanced = True
                else:
                    continue
            else:
                balanced = False
                break
        else:
            balanced = False
            break
    else:
        continue
if balanced:
    print("YES")
else:
    print("NO")


# from collections import deque
# sequence_of_parentheses_queue = deque(input())
# open_parentheses_queue = deque()
# while sequence_of_parentheses_queue:
#     parenthesis = sequence_of_parentheses_queue.popleft()
#     if parenthesis in "({[":
#         left_parenthesis = parenthesis
#         open_parentheses_queue.append(left_parenthesis)
#     else:
#         right_parenthesis = parenthesis
#         if not open_parentheses_queue:
#             print("NO")
#             break
#         else:
#             left_parenthesis = open_parentheses_queue.pop()
#             if f"{left_parenthesis + right_parenthesis}" not in "(){}[]":
#                 print("NO")
#                 break
#             else:
#                 continue
# else:
#     print("YES")
