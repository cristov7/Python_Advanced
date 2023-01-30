def age_assignment(*args, **kwargs):
    names_list = list(args)
    dictionary = dict(kwargs)
    names_dict = {}
    for capital_letter, years_old in dictionary.items():
        for name in names_list:
            if name.startswith(capital_letter):
                info = f"{name} is {years_old} years old."
                names_dict[name] = info
            else:
                continue
    sorted_names_dict = dict(sorted(names_dict.items()))
    return "\n".join([info for name, info in sorted_names_dict.items()])


# print(age_assignment("Peter", "George", G=26, P=19))
# # print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
