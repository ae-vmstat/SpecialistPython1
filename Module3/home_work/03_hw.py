# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here

import random
numbers = []
numbers_sum = 0
i = 1

n = 45

while i <= n:
    numbers.append(random.randint(-100, 100))
    i += 1

for number in numbers:
    if (number >= 1) and (number % 2 == 0):
        numbers_sum += number

# if numbers_sum % 2 == 0:
#     print("OK")
print(numbers_sum)
