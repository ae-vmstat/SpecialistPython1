# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here

import random

len_name = 0
long_name = []

max_name = max(names, key=len)
max_name = len(max_name)

for name in names:
    if (len(name)) >= max_name:
        long_name.append(name)

print(random.choice(long_name))
