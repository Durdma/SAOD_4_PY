import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def CreateKey():

    key = [None] * 6

    for i in range(0, len(key)):

        if i == 0 or i == 5:
            key[i] = np.random.randint(low = 48, high = 58)

        else:
            key[i] = np.random.randint(low = 65, high = 91)

    return key


def CheckKey(key):

    for letter in range(0, len(key)):
        if letter == 0 or letter == 5:
            if ord(key[letter]) < 48 or ord(key[letter]) > 58:
                print("Первый или последний символ ключа не является цифрой!")
                print("Повторите ввод!")
                return False

        else:
            if ord(key[letter]) < 65 or ord(key[letter]) > 91:
                print("2й, 3й, 4й или 5й символ ключа не является буквой!")
                print("Повторите ввод!")
                return False

    return True


def HashFunc(letterKey) -> int:

    coefficients = (11, 29, 31, 37, 41, 43)
    result = 0

    for i in range(0, len(letterKey)):
        if i == 0 or i == 5:
            letterKey[i] -= 48

        else:
            letterKey[i] -= 65

        result += letterKey[i] * coefficients[i]

    return result % 1500


def PlotGraphOfCollisions(table):

    fig, ax = plt.subplots()

    ax.bar(np.arange(len(table)), table)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(150))
    ax.set_title("Количество коллизий на 1 сегмент")
    ax.set_xlabel("Сегменты")
    ax.set_ylabel("Коллизии")
    plt.show()


def ShowCollisions():

    hashTable = np.zeros(1500, dtype = int)
    tmpTable = np.zeros(1500, dtype = int)

    for i in range(0, 3000):

        letterKey = CreateKey()
        key = HashFunc(letterKey)

        if hashTable[key] == 0:
            hashTable[key] += 1

        elif hashTable[key] >= 1:
            tmpTable[key] += 1
            hashTable[key] += 1

    PlotGraphOfCollisions(tmpTable)


def CreateHashTable(table):

    for i in range(0, len(table)):

        letterKey = CreateKey()
        dictKey = "".join(chr(letter) for letter in letterKey)
        key = HashFunc(letterKey)

        for j in range(0, len(table)):
            for k in table[j]:
                if letterKey == k:
                    print(f"Элемент с ключом {dictKey} уже существует! Выберете другой ключ!")

        if not any(table[key]):
            table[key] = {dictKey: i}

        elif len(table[key]) > 5:
            print(f"Сегмент {key} переполнен. Запись элемента с ключом {dictKey} невозможна.")

        else:
            table[key].update({dictKey: i})

    return table


def ShowHashTable(table):

    print("Полученная хеш-таблица:")
    print("Адрес")

    for i in range(0, len(table)):

        print(i, "\t", end="")

        for key in table[i]:
            print("||", key, " | ", table[i][key], "||  ", end="")

        print("")


def AddElem(table):

    print("Введите ключ в формате ЦББББЦ, где:")
    print("Ц - цифра от 0 до 9")
    print("Б - буква от A до Z")
    print("Введите свой ключ:")
    letterKey = str(input())
    print("")
    print("Введите значение:")
    data = int(input())

    letterKey = letterKey.upper()

    if not CheckKey(letterKey):
        return

    key = [None] * len(letterKey)

    for i in range(0, len(letterKey)):
        key[i] = ord(letterKey[i])

    key = HashFunc(key)

    for j in range(0, len(table)):
        for k in table[j]:
            if letterKey == k:
                print(f"Элемент с ключом {letterKey} уже существует! Выберете другой ключ!")
                return

    if not any(table[key]):
        table[key] = {letterKey: data}

    else:
        table[key].update({letterKey: data})


def FindElem(table):

    print("Введите ключ в формате ЦББББЦ, где:")
    print("Ц - цифра от 0 до 9")
    print("Б - буква от A до Z")
    print("Введите свой ключ:")
    letterKey = str(input())
    print("")

    letterKey = letterKey.upper()

    if not CheckKey(letterKey):
        return

    key = [None] * len(letterKey)

    for i in range(0, len(letterKey)):
        key[i] = ord(letterKey[i])

    key = HashFunc(key)

    for i in table[key]:
        if letterKey == i:
            print(key, "\t", end="")
            print("||", i, " | ", table[key][i], "||  ")
            print("")
            return

    print("Элемента с таким ключом нет!!!")
    print("")


def DeletElem(table):

    print("Введите ключ в формате ЦББББЦ, где:")
    print("Ц - цифра от 0 до 9")
    print("Б - буква от A до Z")
    print("Введите свой ключ:")
    letterKey = str(input())
    print("")

    letterKey = letterKey.upper()

    if not CheckKey(letterKey):
        return

    key = [None] * len(letterKey)

    for i in range(0, len(letterKey)):
        key[i] = ord(letterKey[i])

    key = HashFunc(key)

    for i in table[key]:
        if letterKey == i:
            table[key].pop(i)
            print("Элемент удачно удален!")
            return

    print("Элемента с таким ключом нет!!!")
    print("")


def main():

    table = [{}] * 1500
    choice = None

    while choice != 7:

        print("Выберите какое действие необходимо выполнить:")
        print("1 - Вывести график распределения коллизий;")
        print("2 - Заполнить хеш-таблицу;")
        print("3 - Вывести на экран хеш-таблицу;")
        print("4 - Добавить элемент по ключу;")
        print("5 - Найти элемент по ключу;")
        print("6 - Удалить элемент по ключу;")
        print("7 - Закончить работу с программой;")

        choice = int(input())
        print("")

        if choice == 1:
            ShowCollisions()

        elif choice == 2:
            table = CreateHashTable(table)

        elif choice == 3:
            ShowHashTable(table)

        elif choice == 4:
            AddElem(table)

        elif choice == 5:
            FindElem(table)

        elif choice == 6:
            DeletElem(table)


main()