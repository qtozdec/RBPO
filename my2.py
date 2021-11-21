from multiprocessing import Process
from hashlib import sha256
from itertools import product
import time

char_string = 'abcdefghijklmnopqrstuvwxyz'
with open("sha.txt") as file:
    sha_string = []
    for row in file:
        sha_string.append(row.strip())


def func(first_char):
    for _ in product(first_char, char_string, char_string, char_string, char_string):
        if sha256(''.join(_).encode('utf-8')).hexdigest() in sha_string:
            print(f'' + sha256(''.join(_).encode('utf-8')).hexdigest() + ' - ' + ''.join(_))


def main():
    number_of_processes = []
    number_of_parts = int(input('Введите кол-во потоков(1-26): '))
    partition_size = len(char_string) // number_of_parts
    start = time.perf_counter()
    for i in range(number_of_parts):
        if i == number_of_parts - 1:
            first_bit = char_string[partition_size * i:]
        else:
            first_bit = char_string[partition_size * i: partition_size * (i + 1)]
        p = Process(target=func, args=(first_bit,))
        number_of_processes.append(p)
        p.start()
    for proc in number_of_processes:
        proc.join()
    end = time.perf_counter()

    print(f"Вычисление заняло {end - start:0.2f} секунд")


if __name__ == "__main__":
    main()
