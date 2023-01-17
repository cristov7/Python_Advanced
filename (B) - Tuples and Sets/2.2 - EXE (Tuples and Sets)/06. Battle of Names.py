odd_set = set()
even_set = set()
count_names = int(input())
for name in range(1, count_names + 1):
    current_name = input()
    letters_list = list(current_name)
    values_list = [ord(letter) for letter in letters_list]
    value_sum = sum(values_list)
    result = int(value_sum / name)
    if result % 2:
        odd_set.add(result)
    else:
        even_set.add(result)
odd_set_sum = sum(odd_set)
even_set_sum = sum(even_set)
if odd_set_sum > even_set_sum:
    difference_set = odd_set.difference(even_set)
    print(*difference_set, sep=", ")
elif odd_set_sum < even_set_sum:
    symmetric_difference_set = even_set.symmetric_difference(odd_set)
    print(*symmetric_difference_set, sep=", ")
else:
    union_set = odd_set.union(even_set)
    print(*union_set, sep=", ")


# odd_set = set()
# even_set = set()
# for name in range(1, int(input()) + 1):
#     value_sum = sum([ord(letter) for letter in input()])
#     result = value_sum // name
#     if result % 2:
#         odd_set.add(result)
#     else:
#         even_set.add(result)
# odd_set_sum = sum(odd_set)
# even_set_sum = sum(even_set)
# difference_set = odd_set.difference(even_set)
# symmetric_difference_set = even_set.symmetric_difference(odd_set)
# union_set = odd_set.union(even_set)
# if odd_set_sum > even_set_sum:
#     print(*difference_set, sep=", ")
# elif odd_set_sum < even_set_sum:
#     print(*symmetric_difference_set, sep=", ")
# else:
#     print(*union_set, sep=", ")
