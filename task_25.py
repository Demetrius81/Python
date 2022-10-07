# Написать программу преобразования десятичного числа в двоичное


def dec_to_bin(n: int) -> str:
    b: str = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    b = '0b' + b
    return b


print(dec_to_bin(255))
