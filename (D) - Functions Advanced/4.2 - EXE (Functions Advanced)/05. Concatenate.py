def concatenate(*args, **kwargs):
    text_list = list(args)
    text = "".join(text_list)
    dictionary = dict(kwargs)
    for key, value in dictionary.items():
        if key in text:
            while key in text:
                text = text.replace(key, value)
        else:
            continue
    return text


# print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
# # print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
