from collections import deque


def ramen_shop_function(current_bowls_of_ramen_list, current_customers_list):
    def serve_the_customers_function():
        while True:
            if bowls_of_ramen_queue and customers_queue:
                bowl_of_ramen = bowls_of_ramen_queue.pop()
                customer = customers_queue.popleft()
                if bowl_of_ramen > customer:
                    bowl_of_ramen -= customer
                    bowls_of_ramen_queue.append(bowl_of_ramen)
                elif bowl_of_ramen < customer:
                    customer -= bowl_of_ramen
                    customers_queue.appendleft(customer)
                else:
                    continue
            else:
                break

    def print_function():
        print_list = []
        if not customers_queue:
            print_list.append("Great job! You served all the customers.")
            if bowls_of_ramen_queue:
                convert_bowls_of_ramen_list = ", ".join([str(bowl_of_ramen) for bowl_of_ramen in bowls_of_ramen_queue])
                print_list.append(f"Bowls of ramen left: {convert_bowls_of_ramen_list}")
        else:
            print_list.append("Out of ramen! You didn't manage to serve all customers.")
            if customers_queue:
                convert_customers_list = ", ".join([str(customer) for customer in customers_queue])
                print_list.append(f"Customers left: {convert_customers_list}")
        return print_list

    bowls_of_ramen_queue = deque(current_bowls_of_ramen_list)
    customers_queue = deque(current_customers_list)
    serve_the_customers_function()
    output = print_function()
    print("\n".join(output))


bowls_of_ramen_list = deque(map(int, input().split(", ")))
customers_list = deque(map(int, input().split(", ")))
ramen_shop_function(bowls_of_ramen_list, customers_list)

# from collections import deque
# bowls_of_ramen_queue = deque(map(int, input().split(", ")))
# customers_queue = deque(map(int, input().split(", ")))
# while True:
#     if bowls_of_ramen_queue and customers_queue:
#         bowl_of_ramen = bowls_of_ramen_queue.pop()
#         customer = customers_queue.popleft()
#         if bowl_of_ramen > customer:
#             bowl_of_ramen -= customer
#             bowls_of_ramen_queue.append(bowl_of_ramen)
#         elif bowl_of_ramen < customer:
#             customer -= bowl_of_ramen
#             customers_queue.appendleft(customer)
#         else:
#             continue
#     else:
#         break
# if not customers_queue:
#     print("Great job! You served all the customers.")
#     if bowls_of_ramen_queue:
#         print("Bowls of ramen left: ", end="")
#         print(*bowls_of_ramen_queue, sep=", ")
# else:
#     print("Out of ramen! You didn't manage to serve all customers.")
#     if customers_queue:
#         print("Customers left: ", end="")
#         print(* customers_queue, sep=", ")
