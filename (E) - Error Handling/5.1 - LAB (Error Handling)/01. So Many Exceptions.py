numbers_list = list(map(int, input().split(", ")))
result = 1.0
for index in range(len(numbers_list)):
    number = numbers_list[index]
    if number <= 5:
        result *= number
    elif number <= 10:
        result /= number
    else:
        continue
print(result)
