# Найти корни квадратного уравнения Ax² + Bx + C = 0
# -Математикой
# -Используя дополнительные библиотеки*
import math


def solution_of_a_quadratic_equation(a: int, b: int, c: int):
    d = (b ** 2) - (4 * a * c)
    if d < 0:
        return None
    elif d == 0:
        return (- b) / (2 * a)
    else:
        return (-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)


print(solution_of_a_quadratic_equation(2, 4, 2))
