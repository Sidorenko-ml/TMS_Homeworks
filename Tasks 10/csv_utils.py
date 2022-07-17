# Написать функции по работе с csv файлами в файле csv_utils.py. Чтение.
# Запись. Добавление записи(по позиции, по-умолчанию в конец). Удаление
# записи(по позиции, по-умолчанию последнюю).
# В файле task_10_08 импортировать функции. С помощью функций создать
# файл с информацией о товарах(Имя товара, цена, количество,
# комментарий).
# Прочесть файл, Добавить новую позицию в конец. Удалить третью строку
import csv

def csvReader(file):
    with open('{}'.format(file), 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for i in reader:
            print(i)

def csvWriter(file):
    vvod = input('Введите название столбцов через запятую - ')
    fields = vvod.split(', ')
    with open('{}'.format(file), 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        while True:
            print('Введите строки, либо завершите и нажмите "n"')
            GoOrNot = input()
            if GoOrNot == 'n':
                break
            else:
                row = GoOrNot.split(', ')
            csvwriter.writerow(row)

def csvAppender(file):
    with open('{}'.format(file), 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        while True:
            vvod = input('Введите данные, либо завершите и нажмите "0" - ')
            if vvod == "0":
                break
            else:
                rows = vvod.split(', ')
                writer.writerow(rows)

def csvDeleter(file):
    with open('{}'.format(file), 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        SpCopy = list(reader)
        SpNew = SpCopy.copy()
        while 1 == 1:
            vvod = int(input("Введите номер строки, которую хотите удалить, либо нажмите 0 для отмены - "))
            if vvod == 0:
                break
            else:
                del SpNew[vvod - 1]
                with open('{}'.format(file), 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(SpNew)
            vvod2 = input("Если хотите продолжить - нажмите Enter. Если хотите откатить изменения, нажмите на 'r' - ")
            if vvod2 == "r":
                writer.writerows(SpCopy)


def Sum_of_all_products(file):
    sp = []
    Summ = 0
    with open('{}'.format(file), 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sp.append(float(row['Цена,руб.']) * float(row['Количество']))
    for i in sp:
        Summ += float(i)
    return print(f"Полная сумма всех товаров - {Summ} руб.")


def Very_expensive_product(file):
    pr = []
    names_pr = []
    with open('{}'.format(file), 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pr.append(float(row['Цена,руб.']))
            names_pr.append(str(row['Имя товара']))
    print(f'Самый дорогой товар - {names_pr[pr.index(max(pr))]} с ценой {max(pr)} бел. руб.')


def Very_cheap_product(file):
    pr = []
    names_pr = []
    with open('{}'.format(file), 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pr.append(float(row['Цена,руб.']))
            names_pr.append(str(row['Имя товара']))
    print(f'Самый дешевый товар - {names_pr[pr.index(min(pr))]} с ценой {min(pr)} бел. руб.')

def decrease_of_a_lot(file):
    with open('{}'.format(file), 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        SpCopy = list(reader)
        SpNew = SpCopy.copy()
        while 1 == 1:
            vvod1 = int(input("Введите позицию товара, количество которого хотите уменьшить, либо нажмите '0' для отмены - "))
            if vvod1 == 0:
                1 != 1
                break
            else:
                vvod2 = int(input("Насколько необходимо уменьшить? - "))
                SpNew[int(vvod1)][2] = str((int(SpNew[vvod1][2]) - int(vvod2)))
                with open('{}'.format(file), 'w', newline="") as csvfile1:
                    writer = csv.writer(csvfile1)
                    writer.writerows(SpNew)
