# Реализовать алгоритм задания случайных чисел. Без использования встроенного
# генератора псевдослучайных чисел

import datetime


def gen_random_int(first: int, second: int) -> int:
    if not isinstance(first, int) or not isinstance(second, int):
        raise ValueError("First value and secod value must be int type")
    if first > second:
        raise ValueError("Second value must be greater than first value")

    date_now = str(datetime.datetime.now())[-6:]
    integer_for_gen = int(date_now + date_now)
    generated = 0
    while (True):
        if generated >= first and generated <= second:
            break
        elif first == second:
            return first
        integer_for_gen /= 17
        generated = integer_for_gen
    return int(round(generated))


def main():
    print(gen_random_int(1, 10))


if __name__ == "__main__":
    main()
