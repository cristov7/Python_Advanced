def separate_numbers_function():
    def negative_numbers_function(lst):
        return [number for number in lst if number < 0]

    def positive_numbers_function(lst):
        return [number for number in lst if number > 0]

    def sum_numbers_function(lst):
        return sum(lst)

    def print_function(negative, positive):
        print(negative)
        print(positive)
        if abs(negative) > positive:
            print("The negatives are stronger than the positives")
        elif positive > abs(negative):
            print("The positives are stronger than the negatives")
        else:
            raise SystemExit

    numbers_list = list(map(int, input().split()))
    negative_numbers_list = negative_numbers_function(numbers_list)
    positive_numbers_list = positive_numbers_function(numbers_list)
    negative_numbers_sum = sum_numbers_function(negative_numbers_list)
    positive_numbers_sum = sum_numbers_function(positive_numbers_list)
    print_function(negative_numbers_sum, positive_numbers_sum)


separate_numbers_function()


# def separate_numbers_function():
#     numbers_list = list(map(int, input().split()))
#     negative_numbers_list = [number for number in numbers_list if number < 0]
#     positive_numbers_list = [number for number in numbers_list if number > 0]
#     negative_numbers_sum = sum(negative_numbers_list)
#     positive_numbers_sum = sum(positive_numbers_list)
#     print(negative_numbers_sum)
#     print(positive_numbers_sum)
#     if abs(negative_numbers_sum) > positive_numbers_sum:
#         print("The negatives are stronger than the positives")
#     elif positive_numbers_sum > abs(negative_numbers_sum):
#         print("The positives are stronger than the negatives")
#     else:
#         raise SystemExit
#
#
# separate_numbers_function()


# def separate_numbers_function():
#     numbers_list = list(map(int, input().split()))
#     negative_numbers_sum = 0
#     positive_numbers_sum = 0
#     for number in numbers_list:
#         if number < 0:
#             negative_numbers_sum += number
#         elif number > 0:
#             positive_numbers_sum += number
#         else:
#             continue
#     print(negative_numbers_sum)
#     print(positive_numbers_sum)
#     if abs(negative_numbers_sum) > positive_numbers_sum:
#         print("The negatives are stronger than the positives")
#     elif positive_numbers_sum > abs(negative_numbers_sum):
#         print("The positives are stronger than the negatives")
#     else:
#         raise SystemExit
#
#
# separate_numbers_function()
