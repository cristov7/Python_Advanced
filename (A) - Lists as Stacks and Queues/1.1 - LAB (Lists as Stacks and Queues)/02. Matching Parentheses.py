algebraic_expression = input()
open_parentheses_indices_list = []
for index, char in enumerate(algebraic_expression):
    if char == "(":
        open_parentheses_index = index
        open_parentheses_indices_list.append(open_parentheses_index)
    elif char == ")":
        open_parentheses_index = open_parentheses_indices_list.pop()
        close_parentheses_index = index + 1
        result = algebraic_expression[open_parentheses_index: close_parentheses_index]
        print(result)
    else:
        continue


# algebraic_expression = input()
# indices_parentheses_list = []
# for index in range(len(algebraic_expression)):
#     if algebraic_expression[index] == "(":
#         start_index = index
#         indices_parentheses_list.append(start_index)
#     elif algebraic_expression[index] == ")":
#         start_index = indices_parentheses_list.pop()
#         end_index = index + 1
#         print(algebraic_expression[start_index: end_index])
#     else:
#         continue
