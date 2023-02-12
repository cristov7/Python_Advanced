def shopping_cart(*shopping_info_tuple):
    def soup_function(current_meal_and_products_dict, current_product_info):
        current_max_products = 3
        current_meal = current_product_info[0]
        current_product = current_product_info[1]
        current_product_list = current_meal_and_products_dict[current_meal]
        if current_product not in current_product_list:
            current_count_products = len(current_product_list)
            if current_count_products < current_max_products:
                current_meal_and_products_dict[current_meal].append(current_product)
                return current_meal_and_products_dict
            else:
                return current_meal_and_products_dict
        else:
            return current_meal_and_products_dict

    def pizza_function(current_meal_and_products_dict, current_product_info):
        current_max_products = 4
        current_meal = current_product_info[0]
        current_product = current_product_info[1]
        current_product_list = current_meal_and_products_dict[current_meal]
        if current_product not in current_product_list:
            current_count_products = len(current_product_list)
            if current_count_products < current_max_products:
                current_meal_and_products_dict[current_meal].append(current_product)
                return current_meal_and_products_dict
            else:
                return current_meal_and_products_dict
        else:
            return current_meal_and_products_dict

    def dessert_function(current_meal_and_products_dict, current_product_info):
        current_max_products = 2
        current_meal = current_product_info[0]
        current_product = current_product_info[1]
        current_product_list = current_meal_and_products_dict[current_meal]
        if current_product not in current_product_list:
            current_count_products = len(current_product_list)
            if current_count_products < current_max_products:
                current_meal_and_products_dict[current_meal].append(current_product)
                return current_meal_and_products_dict
            else:
                return current_meal_and_products_dict
        else:
            return current_meal_and_products_dict

    def sorted_function(current_meal_and_products_dict):
        current_meal_and_products_dict = dict(sorted(current_meal_and_products_dict.items(), key=lambda x: (-len(x[1]), x)))
        current_shopping_list = []
        for current_meal, current_product_list in current_meal_and_products_dict.items():
            current_shopping_list.append(f"{current_meal}:")
            current_product_list.sort()
            for current_product in current_product_list:
                current_shopping_list.append(f" - {current_product}")
        if len(current_shopping_list) == 3:
            return "No products in the cart!"
        else:
            return "\n".join(current_shopping_list)

    meal_and_products_dict = {"Soup": [], "Pizza": [], "Dessert": []}
    for product_info in shopping_info_tuple:
        if product_info == "Stop":
            break
        else:
            meal = product_info[0]
            if meal == "Soup":
                meal_and_products_dict = soup_function(meal_and_products_dict, product_info)
            elif meal == "Pizza":
                meal_and_products_dict = pizza_function(meal_and_products_dict, product_info)
            elif meal == "Dessert":
                meal_and_products_dict = dessert_function(meal_and_products_dict, product_info)
            else:
                continue
    sorted_shopping_list = sorted_function(meal_and_products_dict)
    return sorted_shopping_list


# def shopping_cart(*args):
#     max_soups_products = 3
#     max_pizza_products = 4
#     max_desserts_products = 2
#     meal_and_products_dict = {"Soup": [], "Pizza": [], "Dessert": []}
#     shopping_info_tuple = args
#     for product_info in shopping_info_tuple:
#         if product_info == "Stop":
#             break
#         else:
#             meal = product_info[0]
#             product = product_info[1]
#             if meal in meal_and_products_dict.keys():
#                 product_list = meal_and_products_dict[meal]
#                 if product not in product_list:
#                     count_products = len(product_list)
#                     if meal == "Soup" and count_products < max_soups_products:
#                         meal_and_products_dict[meal].append(product)
#                     elif meal == "Pizza" and count_products < max_pizza_products:
#                         meal_and_products_dict[meal].append(product)
#                     elif meal == "Dessert" and count_products < max_desserts_products:
#                         meal_and_products_dict[meal].append(product)
#                     else:
#                         continue
#                 else:
#                     continue
#             else:
#                 continue
#     sorted_meal_and_products_dict = dict(sorted(meal_and_products_dict.items(), key=lambda x: (-len(x[1]), x)))
#     shopping_list = []
#     for meal, product_list in sorted_meal_and_products_dict.items():
#         shopping_list.append(f"{meal}:")
#         product_list.sort()
#         for product in product_list:
#             shopping_list.append(f" - {product}")
#     if len(shopping_list) == 3:
#         return "No products in the cart!"
#     else:
#         return "\n".join(shopping_list)


# print(shopping_cart(('Pizza', 'ham'),
#                     ('Soup', 'carrots'),
#                     ('Pizza', 'cheese'),
#                     ('Pizza', 'flour'),
#                     ('Dessert', 'milk'),
#                     ('Pizza', 'mushrooms'),
#                     ('Pizza', 'tomatoes'),
#                     'Stop'))


# print(shopping_cart(('Pizza', 'ham'),
#                     ('Dessert', 'milk'),
#                     ('Pizza', 'ham'),
#                     'Stop'))


# print(shopping_cart('Stop',
#                     ('Pizza', 'ham'),
#                     ('Pizza', 'mushrooms')))
