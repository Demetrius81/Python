#  Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


def check_second(ls: list, st: str) -> int:
    if len(ls) == 0:
        return -1
    if str == '':
        return -1
    i: int = 0
    count: int = 0
    while i < len(ls):
        if not isinstance(ls[i], str):
            return -1
        n = ls[i] == st
        i += 1
        if n and count == 0:
            count += 1
            continue
        elif n and count != 0:
            return i - 1
    return -1


l1 = []
s = "123"

print(check_second(l1, s))
