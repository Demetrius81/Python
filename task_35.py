# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.


def createnumbers_writetofile(n, path):
    st = ''
    for i in range(1, n + 1):
        st = f'{st} {i}'
    try:
        f = open(path, 'w')
        f.write(st)
    except FileNotFoundError:
        return None
    finally:
        f.close()


def read_from_file_and_parse(path: str):
    try:
        f = open(path, 'r')
        st = f.read()
    except FileNotFoundError:
        return None
    finally:
        f.close()
    return [int(i) for i in (st.split())]


#createnumbers_writetofile(10, 'somenumbers.txt')
lis = read_from_file_and_parse('somenumbers.txt')


def find(ls):
    i = 1
    while i < len(ls):
        if ls[i] - 1 != ls[i - 1]:
            return ls[i - 1] + 1
        i += 1
    return None


print(find(lis))
