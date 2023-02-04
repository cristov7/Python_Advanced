# # In "numbers.txt" file            # 1
#                                    # 2
#                                    # 3
#                                    # 4
#                                    # 5


def return_sum_numbers_function(file_name):
    file = open(file_name, "r")
    total_sum = 0
    for line in file:
        number = int(line)
        total_sum += number
    return total_sum


result = return_sum_numbers_function("numbers.txt")
print(result)


# # In "numbers.txt" file            # 1
#                                    # 2
#                                    # 3
#                                    # 4
#                                    # 5
# file = open("numbers.txt", "r")
# numbers_list = [int(number) for number in file]
# numbers_sum = sum(numbers_list)
# print(numbers_sum)


# # In "numbers.txt" file            # 1
#                                    # 2
#                                    # 3
#                                    # 4
#                                    # 5
# file = open("numbers.txt", "r")
# lines_list = file.readlines()
# numbers_list = [int(number) for number in lines_list]
# numbers_sum = sum(numbers_list)
# print(numbers_sum)
