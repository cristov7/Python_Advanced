input_string = input()
stack_list = []
for char in input_string:
    stack_list.append(char)
while True:
    if len(stack_list) > 0:   # if stack_list:
        element = stack_list.pop()   # .pop(-1)
        print(element, end="")
    else:
        break


# stack_list = [char for char in input()]   # stack_list = list(input())
# while len(stack_list) > 0:   # while stack_list:
#     print(stack_list.pop(), end="")   # .pop(-1)


# text_list = list(input())
# stack_list = []
# for count_chars in range(1, len(text_list) + 1):
#     current_char = text_list.pop()   # .pop(-1)
#     stack_list.append(current_char)
# print("".join(stack_list))


# text = input()
# reverse_text = text[::-1]
# print(reverse_text)


# text_list = [char for char in input()]   # text_list = list(input())
# text_list.reverse()
# print("".join(text_list))


# stack = list(input())
# while stack:
#     print(stack.pop(), end="")
