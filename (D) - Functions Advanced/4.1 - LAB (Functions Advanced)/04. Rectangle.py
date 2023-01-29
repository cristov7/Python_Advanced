def rectangle(length, width):
    def area(a, b):
        return a * b

    def perimeter(a, b):
        return 2 * (a + b)
    if type(length) == int and type(width) == int:
        ract_area = area(length, width)
        rect_perim = perimeter(length, width)
        return f"Rectangle area: {ract_area}\nRectangle perimeter: {rect_perim}"
    else:
        return "Enter valid values!"


# print(rectangle(2, 10))
# print(rectangle('2', 10))


# def rectangle(length, width):
#     def area():
#         return length * width
#
#     def perimeter():
#         return 2 * (length + width)
#
#     if type(length) == int and type(width) == int:
#         return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"
#     else:
#         return "Enter valid values!"
#
#
# # print(rectangle(2, 10))
# # print(rectangle('2', 10))
