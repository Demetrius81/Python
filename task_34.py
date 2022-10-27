# Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.

def read_from_file(path) -> str:
    f = open(path, 'r')
    st = f.read();
    f.close()
    return st


def get_list_members(pol):
    pol = pol.split(' = 0\n')
    pol = pol[0]
    pol = pol.split(' + ')
    return pol


def parce_member(mem):
    mem = mem.split('x^')
    return mem


def sum_mem(x: int, y: int):
    return x + y


pol1 = read_from_file("test.txt")
pol2 = read_from_file("test1.txt")

pol1 = get_list_members(pol1)
pol2 = get_list_members(pol2)

pol1 = [parce_member(i) for i in pol1]
pol2 = [parce_member(i) for i in pol2]

print(pol1)
print(pol2)

