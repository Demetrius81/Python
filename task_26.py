# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.
#  Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def negafibonacci(n: int) -> list:
    i: int = 2
    ls = [-1, 0, 1]
    if n == 0:
        return [0]
    if n == 1 or n == -1:
        return [-1, 0, 1]
    if n < 0:
        n = abs(n)
    while i <= n:
        x = ls[-2] + (ls[-1])
        ls.append(x)
        ls.insert(0, -x)
        i += 1
    return ls


print(negafibonacci(8))
