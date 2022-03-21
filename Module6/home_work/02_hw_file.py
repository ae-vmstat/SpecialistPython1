# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения

with open("data/info.txt", "r") as f:
    total = 0
    for line in f:
        if line.strip().isdigit():
            total += int(line)

print(total)
