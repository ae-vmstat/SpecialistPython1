# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

# TODO: your code here
def circles (x1, y1, x2,y2, R1, R2):
    return ((((x1 - x2 ) + (y1 - y2))**2) < ((R1 - R2)**2))

x1, y1 = 20, 16
x2, y2 = 2, 4
R1, R2 = 60, 20
print(circles(x1, y1, x2, y2, R1, R2))
