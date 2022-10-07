# Найти произведение пар чисел в списке.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]


def product_of_pairs(ls: list) -> list:
    rez = []
    n = len(ls) / 2 if len(ls) % 2 == 0 else len(ls) // 2 + 1
    i: int = 0
    while i < n:
        rez.append(ls[i] * ls[-(i + 1)])
        i += 1
    return rez


print(product_of_pairs([2, 3, 5, 6]))
