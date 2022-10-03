# Найти сумму чисел списка стоящих на нечетной позиции


def sum_odd(ls: list) -> int:
    b: bool = False
    rez: int = 0
    for i in ls:
        if b:
            rez += i
            b = not b
            continue
        b = not b
    return rez


l = [2323, 1, 283, 1, 3849, 1, 2323, 1]

print(sum_odd(l))
