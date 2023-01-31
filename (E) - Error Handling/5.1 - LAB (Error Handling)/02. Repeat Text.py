def repeat_text_func(some_text: str, some_number: int):
    some_repeat_text = some_text * some_number
    return some_repeat_text


try:
    text = input()
    number = int(input())
    repeat_text = repeat_text_func(text, number)
    print(repeat_text)
except ValueError:   # except:
    print("Variable times must be an integer")


# try:
#     text = input()
#     number = int(input())
# except ValueError:   # except:
#     print("Variable times must be an integer")
# else:
#     repeat_text = text * number
#     print(repeat_text)
