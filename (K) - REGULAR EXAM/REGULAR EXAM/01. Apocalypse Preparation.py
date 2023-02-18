from collections import deque
textiles_queue = deque(map(int, input().split()))
medicaments_queue = deque(map(int, input().split()))
healing_items_and_resources_dict = {"Patch": 30, "Bandage": 40, "MedKit": 100}
healing_items_and_amount_dict = {}
while True:
    if textiles_queue and medicaments_queue:   # if len(textiles_queue) > 0 and len(medicaments_queue) > 0:
        textile = textiles_queue.popleft()
        medicament = medicaments_queue.pop()
        resources = textile + medicament
        if resources in healing_items_and_resources_dict.values():
            for healing_item, resources_needed in healing_items_and_resources_dict.items():
                if resources == resources_needed:
                    if healing_item not in healing_items_and_amount_dict.keys():
                        healing_items_and_amount_dict[healing_item] = 1
                        break
                    else:   # elif healing_item in healing_items_and_amount_dict.keys():
                        healing_items_and_amount_dict[healing_item] += 1
                        break
                else:
                    continue
        else:   # elif resources not in healing_items_and_resources_dict.values():
            if resources > healing_items_and_resources_dict["MedKit"]:
                if "MedKit" not in healing_items_and_amount_dict.keys():
                    healing_items_and_amount_dict["MedKit"] = 1
                else:   # elif "MedKit" in healing_items_and_amount_dict.keys():
                    healing_items_and_amount_dict["MedKit"] += 1
                resources_left = resources - healing_items_and_resources_dict["MedKit"]
                medicament = medicaments_queue.pop()
                medicament += resources_left
                medicaments_queue.append(medicament)
            else:
                medicament += 10
                medicaments_queue.append(medicament)
    else:
        break
if not textiles_queue and not medicaments_queue:
    print("Textiles and medicaments are both empty.")
elif not textiles_queue:
    print("Textiles are empty.")
else:   # elif not medicaments_queue:
    print("Medicaments are empty.")
if healing_items_and_amount_dict:
    sorted_healing_items_and_amount_dict = dict(sorted(healing_items_and_amount_dict.items(), key=lambda x: (-x[1], x[0])))
    for item_name, amount_created in sorted_healing_items_and_amount_dict.items():
        print(f"{item_name} - {amount_created}")
if medicaments_queue:
    medicaments_queue.reverse()
    convert_medicaments_output = ", ".join([str(medicament) for medicament in medicaments_queue])
    print(f"Medicaments left: {convert_medicaments_output}")
if textiles_queue:
    convert_textiles_output = ", ".join([str(textile) for textile in textiles_queue])
    print(f"Textiles left: {convert_textiles_output}")
