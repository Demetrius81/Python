# Определить, присутствует ли в заданном списке строк, некоторое число

lst = ['djfh', 'fdkj', '45', 'sldfk', 58.4, 'sdj']


def has_number(ls: list) -> bool:
    for i in ls:
        if isinstance(i, int) or isinstance(i, float):
            return True
    return False


print(has_number(lst))
