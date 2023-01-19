from collections import deque


def considered_done_function(presents_dict: dict):
    if "Doll" in presents_dict.keys() and "Wooden train" in presents_dict.keys():
        return "The presents are crafted! Merry Christmas!"
    elif "Teddy bear" in presents_dict.keys() and "Bicycle" in presents_dict.keys():
        return "The presents are crafted! Merry Christmas!"
    else:
        return "No presents this Christmas!"


def materials_left_function(boxes_with_materials_queue: deque):
    materials_values_list = [str(material) for material in boxes_with_materials_queue]
    materials_values_list.reverse()
    return f"Materials left: {', '.join(materials_values_list)}"


def magic_left_function(magic_level_queue: deque):
    magic_values_list = [str(magic) for magic in magic_level_queue]
    return f"Magic left: {', '.join(magic_values_list)}"


def sorted_presents_function(presents_dict: dict):
    sorted_presents_list = sorted(presents_dict.items())
    presents_list = []
    for present_tuple in sorted_presents_list:
        present_name = present_tuple[0]
        count_presents = present_tuple[1]
        presents_list.append(f"{present_name}: {count_presents}")
    return presents_list


values_of_boxes_with_materials_queue = deque(map(int, input().split()))
values_of_magic_level_queue = deque(map(int, input().split()))
product_dict = {"Doll": 150, "Wooden train": 250, "Teddy bear": 300, "Bicycle": 400}
crafted_presents_dict = {}
while True:
    if len(values_of_boxes_with_materials_queue) > 0 and len(values_of_magic_level_queue) > 0:
        last_box_with_materials = values_of_boxes_with_materials_queue.pop()
        first_magic_level = values_of_magic_level_queue.popleft()
        total_magic_level = last_box_with_materials * first_magic_level
        if total_magic_level in product_dict.values():
            craft_present = ""
            for present, magic_needed in product_dict.items():
                if total_magic_level == magic_needed:
                    craft_present = present
                    break
                else:
                    continue
            if craft_present not in crafted_presents_dict.keys():
                crafted_presents_dict[craft_present] = 1
            else:
                crafted_presents_dict[craft_present] += 1
        else:
            if total_magic_level < 0:
                result = last_box_with_materials + first_magic_level
                values_of_boxes_with_materials_queue.append(result)
            elif total_magic_level > 0:
                result = last_box_with_materials + 15
                values_of_boxes_with_materials_queue.append(result)
            elif last_box_with_materials == 0 and first_magic_level == 0:
                continue
            elif last_box_with_materials == 0:
                values_of_magic_level_queue.appendleft(first_magic_level)
            else:   # first_magic_level == 0:
                values_of_boxes_with_materials_queue.append(last_box_with_materials)
    else:
        break
considered_done = considered_done_function(crafted_presents_dict)
print(considered_done)
if values_of_boxes_with_materials_queue:
    materials_left = materials_left_function(values_of_boxes_with_materials_queue)
    print(materials_left)
if values_of_magic_level_queue:
    magic_left = magic_left_function(values_of_magic_level_queue)
    print(magic_left)
sorted_crafted_presents_list = sorted_presents_function(crafted_presents_dict)
print(*sorted_crafted_presents_list, sep="\n")


# from collections import deque
# values_of_boxes_with_materials_queue = deque(map(int, input().split()))
# values_of_magic_level_queue = deque(map(int, input().split()))
# product_dict = {"Doll": 150, "Wooden train": 250, "Teddy bear": 300, "Bicycle": 400}
# crafted_presents_dict = {}
# while True:
#     if len(values_of_boxes_with_materials_queue) > 0 and len(values_of_magic_level_queue) > 0:
#         last_box_with_materials = values_of_boxes_with_materials_queue.pop()
#         first_magic_level = values_of_magic_level_queue.popleft()
#         total_magic_level = last_box_with_materials * first_magic_level
#         if total_magic_level in product_dict.values():
#             craft_present = ""
#             for present, magic_needed in product_dict.items():
#                 if total_magic_level == magic_needed:
#                     craft_present = present
#                     break
#                 else:
#                     continue
#             if craft_present not in crafted_presents_dict.keys():
#                 crafted_presents_dict[craft_present] = 1
#             else:
#                 crafted_presents_dict[craft_present] += 1
#         else:
#             if total_magic_level < 0:
#                 result = last_box_with_materials + first_magic_level
#                 values_of_boxes_with_materials_queue.append(result)
#             elif total_magic_level > 0:
#                 result = last_box_with_materials + 15
#                 values_of_boxes_with_materials_queue.append(result)
#             elif last_box_with_materials == 0 and first_magic_level == 0:
#                 continue
#             elif last_box_with_materials == 0:
#                 values_of_magic_level_queue.appendleft(first_magic_level)
#             else:   # first_magic_level == 0:
#                 values_of_boxes_with_materials_queue.append(last_box_with_materials)
#     else:
#         break
# if "Doll" in crafted_presents_dict.keys() and "Wooden train" in crafted_presents_dict.keys():
#     print("The presents are crafted! Merry Christmas!")
# elif "Teddy bear" in crafted_presents_dict.keys() and "Bicycle" in crafted_presents_dict.keys():
#     print("The presents are crafted! Merry Christmas!")
# else:
#     print("No presents this Christmas!")
# if values_of_boxes_with_materials_queue:
#     materials_values_list = [str(material) for material in values_of_boxes_with_materials_queue]
#     materials_values_list.reverse()
#     print(f"Materials left: {', '.join(materials_values_list)}")
# if values_of_magic_level_queue:
#     magic_values_list = [str(magic) for magic in values_of_magic_level_queue]
#     print(f"Magic left: {', '.join(magic_values_list)}")
# sorted_crafted_presents_list = sorted(crafted_presents_dict.items())
# for present_tuple in sorted_crafted_presents_list:
#     present_name = present_tuple[0]
#     count_presents = present_tuple[1]
#     print(f"{present_name}: {count_presents}")
