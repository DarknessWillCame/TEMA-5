from math import sqrt

def calc_truangle_square_gerone_calc(a, b, c):
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

print(
    'Площадь из минимальных сторон треугольника:',
    calc_truangle_square_gerone_calc(min(one), min(two), min(three))
)
print(
    'Площадь из максимальных сторон треугольника:',
    calc_truangle_square_gerone_calc(max(one), max(two), max(three))
)
