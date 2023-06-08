# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import exrex


# Здесь пишем код
def generate_random_name():
    while True:
        list_string = []
        for i in range(2):
            len_string = random.randint(1, 15)
            word = exrex.getone('[A-Z]{%d}[a-z]{%d}' % (len_string, 0))
            list_string.append(word)
        name = " ".join(list_string)
        yield name


gen = generate_random_name()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
