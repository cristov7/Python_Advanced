def even_odd(*args):
    def even_function(tpl):
        lst = [element for element in tpl if element % 2 == 0]
        return lst

    def odd_function(tpl):
        lst = [element for element in tpl if element % 2]
        return lst

    numbers_tuple = args[:-1]
    command = args[-1]
    if command == "even":
        numbers_list = even_function(numbers_tuple)
        return numbers_list
    elif command == "odd":
        numbers_list = odd_function(numbers_tuple)
        return numbers_list
    else:
        raise SystemExit


# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# # print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
