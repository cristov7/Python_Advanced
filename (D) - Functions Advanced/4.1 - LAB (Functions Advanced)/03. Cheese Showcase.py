def sorting_cheeses(**kwargs):
    cheeses_dict = kwargs
    sorted_cheeses_as_tuples_in_list = sorted(cheeses_dict.items(), key=lambda x: (-len(x[1]), x[0]))
    sorting_cheeses_list = []
    for tuple_as_element in sorted_cheeses_as_tuples_in_list:
        cheese_name = tuple_as_element[0]
        cheese_list = tuple_as_element[1]
        sorted_cheese_list = sorted(cheese_list, reverse=True)
        sorting_cheeses_list.append(cheese_name)
        for quantity in sorted_cheese_list:
            quantity = str(quantity)
            sorting_cheeses_list.append(quantity)
    return "\n".join(sorting_cheeses_list)


# print(sorting_cheeses(Parmesan=[102, 120, 135], Camembert=[100, 100, 105, 500, 430], Mozzarella=[50, 125],))
# print(sorting_cheeses(Parmigiano=[165, 215], Feta=[150, 515], Brie=[150, 125]))
