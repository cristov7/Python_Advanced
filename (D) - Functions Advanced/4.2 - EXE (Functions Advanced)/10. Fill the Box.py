def fill_the_box(*args):
    height = args[0]
    length = args[1]
    width = args[2]
    size_of_the_box = height * length * width
    cubes_list = list(args[3:])
    for index, cube in enumerate(cubes_list):
        if cube == "Finish":
            return f"There is free space in the box. You could put {size_of_the_box} more cubes."
        else:
            if size_of_the_box - cube >= 0:
                size_of_the_box -= cube
            else:
                more_cubes_list = cubes_list[index:]
                more_cubes_list.remove("Finish")
                more_cubes = sum(more_cubes_list) - size_of_the_box
                return f"No more free space! You have {more_cubes} more cubes."


# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
# # print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
# # print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
