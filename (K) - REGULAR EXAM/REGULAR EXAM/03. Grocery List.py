def shop_from_grocery_list(budget, grocery_list, *products_and_prices_tuples_in_tuple):
    def return_current_output_list_function():
        current_output_list = []
        current_purchased_products_set = set(purchased_products_list)
        current_grocery_set = set(grocery_list)
        if current_purchased_products_set.issuperset(current_grocery_set):
            current_output = f"Shopping is successful. Remaining budget: {budget:.2f}."
            current_output_list.append(current_output)
        else:
            current_missing_products_set = current_grocery_set.difference(current_purchased_products_set)
            convert_missing_products = ", ".join(current_missing_products_set)
            current_output = f"You did not buy all the products. Missing products: {convert_missing_products}."
            current_output_list.append(current_output)
        return current_output_list

    purchased_products_list = []
    not_enough_money = False
    for product_and_price_tuple in products_and_prices_tuples_in_tuple:
        product = product_and_price_tuple[0]
        price = product_and_price_tuple[1]
        if not_enough_money:
            break
        elif product in grocery_list:
            for product_to_buy in grocery_list:
                if product == product_to_buy and product not in purchased_products_list:
                    if budget >= price:
                        budget -= price
                        purchased_products_list.append(product)
                        break
                    else:
                        not_enough_money = True
                        break
                else:
                    continue
        else:
            continue
    output_list = return_current_output_list_function()
    return "\n".join(output_list)


# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola"],
#     ("cola", 5.8), ("tomato", 10.0), ("tomato", 20.45)))


# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat"],
#     ("cola", 5.8), ("tomato", 10.0), ("meat", 22)))


# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat", "chocolate"],
#     ("cola", 15.8), ("chocolate", 30), ("tomato", 15.85), ("chips", 50), ("meat", 22.99)))
