# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]

import random
numbers = []
numbers_sqrt = []
i = 1
n = random.randint(10, 100)

#numbers = [-20, -3, -1, 0, 1, 3, 20, 25, -25]
#numbers = [2, -5, 8, 9, -25, 25, 4]

while i <= n:
    numbers.append(random.randint(-100, 100))
    i += 1

for number in numbers:
    if (number >= 4) and ((number ** (0.5)) % 1 == 0):
    # if (number >= 4) and ((number ** (0.5)).is_integer()):
        numbers_sqrt.append(int(number ** (0.5)))

print(numbers_sqrt)
