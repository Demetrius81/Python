# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел

def max_min_number(st: str) -> tuple:
    ls = st.split(' ')
    li = []
    for i in ls:
        li.append(int(i))
    ma = max(li)
    mi = min(li)
    return ma, mi


print(max_min_number('1 2 -3 876876876 4 5 6'))
