"""
ВАЖНОЕ ЗАМЕЧАНИЕ ПО ЗАДАНИЮ СЛАЙДА #6

DENIS NESTEROV  =>  ФИО из 13 букв => 13% 5 = 3  =>  Set

Делать было нужно задание со структурой Set, но что-то пошло не так с подсчетом букв в ФИО и я сначала все сделал для List.
А для Set сделал дополнительно, потому что там все равно все через преобразования List <-> Set как бы можно и нужно делать.

ЧАСТЬ 1:  LIST
"""


def listGenerator_001(n=0):
    '''
        Практика 1, Слайд 6 , Задание 1
        Сгенерировать [тип] размера (N  + 2) * 2 (если есть ключи – пусть совпадают с индексами, например)
    '''

    lst = list(range((n+2)**2))  # lst = [num for num in range((n+2)**2)]
    return lst


def listGenerator_002(lst):
    '''
        Практика 1, Слайд 6 , Задание 2
        Продублировать все значения из сгенерированного массива, и каждое из продублированных увеличить на 1
    '''
    lst += [num + 1 for num in lst]
    return lst


def listGenerator_003(lst):
    '''
            Практика 1, Слайд 6 , Задание 3
            Выбрать из пункта 2 значения, начиная со второго по убыванию числа и до предпоследнего числа.
    '''

    sortLst = sorted(lst, reverse=True) # сортируем список по убыванию
    firstMax = sortLst[0] # максимальное число в списке - на первой позиции
    # print('firstMax=', firstMax)
    for secondMax in sortLst[1:len(sortLst)]: # ищем со второго элемента в списке и до конца второе максимальное число
        if secondMax < firstMax:
            # второе минимальное найдено
            # print('secondMax=', secondMax)
            break

    return lst[lst.index(secondMax):-1]


def listGenerator_004(lst):
    '''
        Практика 1, Слайд 6 , Задание 4
        Выбрать из пункта 2 только те значения, индексы (ключи) которых в остатке от деления на 3 дают 1.
    '''

    sublst = []
    for i in range(len(lst)):
        if i % 3 == 1:
            # print(i, i % 3, lst[i])
            sublst.append(lst[i])

    return sublst


def listGenerator_005(lst):
    '''
        Практика 1, Слайд 6 , Задание 5
        Выбрать из пункта 2 любую треть чисел (округляя по правилам округления)

        Выберем первую треть :)
    '''

    return lst[0:round(len(lst)/3)]


lst = listGenerator_001(int(input("Введите количество элементов n=")))
print("\nИсходный сгенерированный список:\n", lst)

lst = listGenerator_002(lst)
print("\nСписок с продублированными значениями и увеличением на +1:\n", lst)

sublst = listGenerator_003(lst)
print("\nСписок от (первого вхождения в список) второго по убыванию числа и до предпоследнего числа:\n", sublst)

sublst = listGenerator_004(lst)
print("\nСписок индексы (ключи) которых в остатке от деления на 3 дают 1:\n", sublst)

sublst = listGenerator_005(lst)
print("\nПервая треть чисел из списка:\n", sublst)
print("-- всего чисел в выборке:\n", len(sublst), " из ", len(lst))