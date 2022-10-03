# Подсчитать сумму цифр в вещественном числе

num = 1.111


def sum_new(n: float) -> int:
    return int(n)

def sum(n: float) -> int:
    s = str(n)
    rez: int = 0
    for i in s:
        if i != '.':
            rez += int(i)
    return rez


print(sum(num))
