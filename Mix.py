# Реализовать алгоритм перемешивания списка.
import random
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def mix(lst: list) -> list:
    i: int = 0
    while i < len(lst):
        n = random.randint(i, len(lst) - 1)
        (lst[i], lst[n]) = (lst[n], lst[i])
        i += 1
    return lst


print(mix(ls))
