# Дан текст:
text = "World War II began on Sep 1939 and ended on Sep 1945. Victory Day has been celebrated since 1945."
# Найдите и выведите все года, которым предшествует месяц.
# Уточнение: вывести ТОЛЬКО года, но те, ПЕРЕД которыми стоит месяц!

import re

years = (re.findall(r'\b\w{3} \d{4}\b',text))

for year in years:
    year_only = re.findall(r'\b\d{4}\b', year)
    print(year_only)
    
