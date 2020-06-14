import json
import random
import re

# /////

didict = {}
english_pattern = re.compile(r'(([A-z])+-?\s?([A-z])+\b)')




##Проверка и получение пользовательских данных
def import_data_json():
    try:
        with open("ndtname.json", 'r') as read_file:
            data = json.load(read_file)
            m1 = data
    except FileNotFoundError:
        print("Файл пуст, создаем новый.")
        m1 = input_data()
        export_data_json(m1)

    return m1



def export_data_json(data):  # запись и переоткрытие внесенных данных
    with open("ndtname.json", 'w') as savefile:
        json.dump(data, savefile, indent=4)



def input_data():  # Функция внесения данных
    dictindex = {}
    for key, value in ({'contry': 'страну', 'city': "город", 'street': "улицу"}).items():
        listtrue = [] #Обнуляем список
        listerorr = []
        while len(listtrue) < 1:  # Цикл с проверкой заполнения
            for word in input("Введите " + value + " (eng.) используя пробелы: ").split():
                if not re.match(english_pattern, word):  # Проверка ввода
                    listerorr.append(word)
                else:
                    listtrue.append(word)
            # Отчет
            if (len(listerorr) == 0) and (len(listtrue) > 0):
                print("Добавлены все: ", listtrue)
            elif (len(listerorr) > 0) and (len(listtrue) > 0):
                print("Добавлено: ", len(listtrue), listtrue)
                print("Отфильтровано: ", len(listerorr), listerorr)
            else:
                print("Ничего не добавлено:( \nВведите строку повторно.")
            dictindex.update({key: listtrue})
    for value in ('bild', 'kv'):
        i1 = int(0)
        listbild = []
        while i1 < 9:
            i1 = i1 + 1
            listbild.append(random.randint(0, 100))
        dictindex.update({value: listbild})
    return dictindex

print(('vuyug' in [c for d, c in import_data_json().items()]))

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
