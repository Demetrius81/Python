# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k. *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def generate_polynomial(k):
    rez: str = ''
    for i in range(0, k+1):
        temp = polynomial_term(i)
        if not temp:
            continue
        if i == 0:
            rez = f'{temp} = 0'
        else:
            rez = f'{temp} + {rez}'
    return rez


def polynomial_term(n):
    a = random.randint(0, 100)
    if n == 0:
        return f'{a}'
    if a == 0:
        return ''
    return f'{a}x^{n}'


def writetofile(msg):
    f = open('test.txt', "a")
    f.write(msg + '\n')
    f.close()

writetofile(generate_polynomial(8))
