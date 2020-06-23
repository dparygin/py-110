"""
Модуль генерации случайных адресов
"""
import json
import random
import re

english_pattern = re.compile(r'(([A-z])+-?\s?([A-z])+\b)')


def import_data_json():
    """
     Импорт пользовательских данных
    :return:  json file
    """
    with open("ndtname.json", 'r') as read_file:
        return json.load(read_file)

def check_data(data):
    """
     Проверка корректности данных
    :param data:
    :return: True or False
    """
    if not isinstance(data, dict):
        return False
    if len(data) <= 3:
        return False
    for key in iter(data):
        if not isinstance(data[key], list):
            return False
        if len(data[key]) >= 2:
            for word in data[key]:
                if not isinstance(word,int):
                    if not re.match(english_pattern, word):
                        # Проверяем соответствие паттерну
                        return False
    return True

def my_decorator(test):
    """
     Декоратор
    :param test:  code word
    :return: Messege
    """
    def dec(wrapped):
        def inner(*args, **kwargs):
            if not (test in [c for d, c in import_data_json().items()]):
                return wrapped(*args, **kwargs)
            else:
                print('message arg')
        return inner
    return dec

#@my_decorator('xaxa')
def gen_add_num_ranodm(data):
    """
    Генерация случайной выборки
    :param data:
    :return:
    """
    retur = {}
    for k1ery in data:
        if not (k1ery == 'bild' and random.randrange(0, 2, 1)):
            retur.update({k1ery: random.choice(data[k1ery])})
    return retur

def main():
    if check_data(import_data_json()):
        h = 0
        while h <= 6: # Число сгенерированных адресов
            for key, vaule in gen_add_num_ranodm(import_data_json()).items():
                print(key, vaule)
            h += 1
            print('\n')
    else:
        print("Файл содержит некорректные данные!")


if __name__ == "__main__":
    main()