'''

Вывести всю внутреннюю структуру папок и файлов в виде:
| Папка 1
|   | Папка 2
|   |    | Файл 0
|   | Файл 1
| Папка 3
|  | Файл 2
|  | Файл 3
При чем названия файлов должны напечатаны быть жирным тестом

Дополнительно: еще и голубым цветом :)
Дополнительно-2: предварительно генерируем тестовую папку со структурой, чтобы экспериметнтировать в ней

!!! Проблема: переименование пока не получилось - вылетает по ошибке на 109 строке =(

'''

import os
import numpy as np
# import matplotlib.pyplot as plt

def createDir(xpath):
    if not os.path.exists(xpath):
        os.mkdir(xpath)
        print('Каталог ', xpath , ' создан')
    else:
        print('Каталог ', xpath, ' уже существует')
    # os.listdir(os.getcwd())


def createTestStructure(rootpath):

    '''
        Наверное можно заморочиться, найти регулярность и сделать через циклы
        Но сходу однозначно читаемой реулярности не увидел, есть шероховатости

        Для ускорения процесса сделаем некреативно и тупо ;)
    '''

    # создаем на C тестовый каталог rootpath, если он не существует
    # все эксперименты будем делать в нём
    createDir(rootpath)
    os.chdir(rootpath)

    createDir("test1")
    createDir("test1\\test2")
    createDir("test1\\test2\\test3")
    createDir("test1\\test2\\test3\\test4")
    createDir("test1\\test2\\test3\\test4\\file4")
    createDir("test1\\test2\\test4")

    createDir("test1\\test3")
    createDir("test1\\test3\\test4")
    createDir("test1\\test3\\test4\\file4")
    createDir("test1\\test4")

    createDir("test2")
    createDir("test2\\test3")
    createDir("test2\\test3\\test4")
    createDir("test2\\test3\\test4\\file4")
    createDir("test2\\test3")
    createDir("test2\\test3\\file4")

    createDir("test3")
    createDir("test3\\test4")
    createDir("test3\\test4\\file4")

    createDir("test4")
    createDir("test4\\file4")


def printItem(level, name, ftype, fullname):
    spaces = '    '
    if ftype == "FILE":
        name = '\033[96m\033[1m' + name + '\033[0m'
    print(spaces * (level + 1), name, '[' + ftype + ']' ,'[' + fullname + ']')

def getNewName(name):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a = np.random.randint(0, 35, len(name))  # новое имя пусть будет той же длины и капслоком для красоты ;)
    # print(a)
    ns = ''
    for i in a:
        ns += alphabet[i]
    return  ns

def findAndRenameDirs(mypath):
    tree = []
    dirtree = []
    for root, dirs, files in os.walk(mypath):
        print(root, dirs, files)
        if os.path.isdir(root):
            dirtree += [root]

    print ('DIRTREE:')
    for i in dirtree:
         print(i)

    print('statr renaming >>>')
    for fullname in dirtree:
        if fullname == mypath:
            print('PASS')
            continue
        name =fullname[fullname.rfind('\\')+1:]
        newname = getNewName(name)
        print(fullname,':' , name, '->',newname)
        os.chdir(fullname)
        print(os.getcwd())
        os.rename(fullname, newname)

    return tree

def showMe(mypath):

    print(mypath)
    level = 0
    print(mypath[0])
    tree = []

    # LEVEL 0
    tree.append(os.listdir(mypath[level]))
    for name in tree[level]:
        fullname = mypath[level] + name
        if os.path.isdir(fullname):
            printItem(level, name, 'DIR ', fullname)
            mypath.append(fullname + "\\")
            level += 1
            tree.append(os.listdir(mypath[level]))

            # LEVEL 1
            for name in tree[level]:
                fullname = mypath[level] + name
                if os.path.isdir(fullname):
                    printItem(level, name, 'DIR ', fullname)
                elif os.path.isfile(fullname):
                    printItem(level, name, 'FILE', fullname)
            level -= 1

        elif os.path.isfile(fullname):
            printItem(level, name, 'FILE', fullname)

print("Шаг 1: создаем тестовую структуру папаок, если нужно")
if input("Создать тестовую структуру папок? [1 - ДА 0 - НЕТ ]") == "1":
    mypath = input("Path (empty for TEST c:\\pyostest2 structure):")
    if mypath == '':
        mypath = 'c:\\pyostest2'
    createTestStructure(mypath)

print("Шаг 2: выводим дерево папок и файлов и переименовываем их (по запросу, доступно только в тестовой структуре)")
isRandomRename = False # переименование по-умолчанию отключено
mypath = input("Path (empty for TEST folder):")
if mypath == '':
    mypath = 'c:\\pyostest2\\' # mypath = '.\\'
    isRandomRename = input("Переименовать папки в тестовой структуре? [1 - ДА 0 - НЕТ ]") == "1"
    if isRandomRename:
        findAndRenameDirs(mypath)


showMe([mypath])
while isRandomRename and input("Переименуем еще раз? Это же весело! [1 - ДА 0 - НЕТ ]") == "1":
    showMeAndRename([mypath], isRandomRename)