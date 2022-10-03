# Задать список из n чисел последовательности (1 + 1 / n) ** n и вывести на экран их сумму

num = 4


def create_list(n: int) -> list:
    ls = []
    if n <= 0:
        return ls
    for i in range(1, n + 1):
        ls.append((1 + 1 / i) ** i)
    return ls


print(create_list(num))
