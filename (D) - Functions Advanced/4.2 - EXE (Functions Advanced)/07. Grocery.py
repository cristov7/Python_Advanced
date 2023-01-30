def grocery_store(**kwargs):
    sorted_kwargs = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    sorted_list = []
    for name, quantity in sorted_kwargs.items():
        info = f"{name}: {quantity}"
        sorted_list.append(info)
    return "\n".join(sorted_list)


# print(grocery_store(bread=5, pasta=12, eggs=12,))
# # print(grocery_store(bread=2, pasta=2, eggs=20, carrot=1,))


# def grocery_store(**kwargs):
#     sorted_list = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
#     return "\n".join([f"{name}: {quantity}" for name, quantity in sorted_list])
#
#
# print(grocery_store(bread=5, pasta=12, eggs=12,))
# # print(grocery_store(bread=2, pasta=2, eggs=20, carrot=1,))
