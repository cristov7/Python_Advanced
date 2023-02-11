from math import log


def return_log_function(number, base):
    if base == "natural":
        return f"{log(number):.2f}"
    else:
        base = int(base)
        return f"{log(number, base):.2f}"


current_number = int(input())
current_base = input()
current_log = return_log_function(current_number, current_base)
print(current_log)


# from math import log
# number = int(input())
# base = input()
# if base == "natural":
#     print(f"{log(number):.2f}")
# else:
#     base = int(base)
#     print(f"{log(number, base):.2f}")
