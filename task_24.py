# В заданном списке вещественных чисел найдите разницу между
# максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def diff_max_min(ls: list) -> float:
    sortedls = []
    for i in ls:
        n = round((float(i) % 1), 2)
        sortedls.append(n)
    print(sortedls)
    sortedls.sort()
    print(sortedls)
    for i in sortedls:
        if i > 0:
            return sortedls[-1] - i


print(diff_max_min([10, 2.005, 5.019, 1.1, 1.2, 3.1, 5, 10.01]))

