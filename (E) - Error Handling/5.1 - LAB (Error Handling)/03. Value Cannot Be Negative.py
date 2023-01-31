class ValueCannotBeNegative(Exception):
    """Number is below zero"""
    pass


for number in range(5):
    current_number = int(input())
    if current_number < 0:
        raise ValueCannotBeNegative()
    else:
        continue
