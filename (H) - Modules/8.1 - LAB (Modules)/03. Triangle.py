from module import return_triangle_function


# def return_triangle_function(size: int):
#     triangle = ""
#     for line in range(1, size + 1):
#         last_number = line
#         for number in range(1, last_number + 1):
#             triangle += f"{number} "
#         triangle += "\n"
#     for line in range(size - 1, 0, - 1):
#         last_number = line
#         for number in range(1, last_number + 1):
#             triangle += f"{number} "
#         triangle += "\n"
#     return triangle


size_of_triangle = int(input())
figure = return_triangle_function(size_of_triangle)
print(figure)


# current_number = int(input())
# numbers_list = [number for number in range(1, current_number + 1)]
# for index in range(1, current_number + 1):
#     line_list = numbers_list[: index]
#     print(*line_list)
# for index in range(current_number - 1, 0, - 1):
#     line_list = numbers_list[: index]
#     print(*line_list)
