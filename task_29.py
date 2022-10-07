# Найти НОК двух чисел
import math


def gcm(a: int, b: int) -> int:
    return a * b / math.gcd(a, b)


print(gcm(2, 3))
