import json
import random
import re

english_pattern = re.compile(r'(([A-z])+-?\s?([A-z])+\b)')

def import_data_json():##Проверка и получение пользовательских данных
    with open("ndtname.json", 'r') as read_file:
        return json.load(read_file)

def input_data(data):  # Проверка корректности данных
    if not isinstance(dict, data):
        return False
    if len(data) >= 2:
        return False
    for key, listd in iter(data):
        if not isinstance(list, listd):
            return False
        if len(listd) >= 2:
        for word in listd:
            if not re.match(english_pattern, word):
                return False
    return True

def my_decorator(test):
    def dec(wrapped):
        def inner(*args, **kwargs):
            if not (test in [c for d, c in import_data_json().items()]):
                return wrapped(*args, **kwargs)
            else:
                print('message arg')
        return inner
    return dec

@my_decorator('xaxa')
def GenAddNum_ranodm(dic):
    print("Генерация случайных адресов: ")
    for key in dic:
        if key == 'bild':
            if random.randrange(0, 2, 1):
                print(key, random.choice(dic[key]))
        else:
            print(key, random.choice(dic[key]))

def main():
    GenAddNum_ranodm(import_data_json())


if __name__ == "__main__":
    main()