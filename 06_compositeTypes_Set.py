"""
ВАЖНОЕ ЗАМЕЧАНИЕ ПО ЗАДАНИЮ СЛАЙДА #6

DENIS NESTEROV  =>  ФИО из 13 букв => 13% 5 = 3  =>  Set

Делать было нужно задание со структурой Set, но что-то пошло не так с подсчетом букв в ФИО и я сначала все сделал для List.
А для Set сделал дополнительно, потому что там все равно все через преобразования List <-> Set как бы можно и нужно делать.


ЧАСТЬ 2:  SET
"""


def setGenerator_001(n=0):
    '''
        Практика 1, Слайд 6 , Задание 1
        Сгенерировать [тип] размера (N  + 2) * 2 (если есть ключи – пусть совпадают с индексами, например)
    '''

    myset = set(range((n+2)**2))  # lst = [num for num in range((n+2)**2)]
    return myset


def setGenerator_002(dset):
    '''
        Практика 1, Слайд 6 , Задание 2
        Продублировать все значения из сгенерированного массива, и каждое из продублированных увеличить на 1
    '''
    lst = list(dset)
    lst += [num + 1 for num in lst]
    dset = set (lst)  # сюрприз =) в сет попадут только недублирующиеся значения списка
    return dset


def setGenerator_003(dset):
    '''
            Практика 1, Слайд 6 , Задание 3
            Выбрать из пункта 2 значения, начиная со второго по убыванию числа и до предпоследнего числа.
    '''

    lst = list(dset)
    sortLst = sorted(lst, reverse=True) # сортируем список по убыванию
    firstMax = sortLst[0] # максимальное число в списке - на первой позиции
    # print('firstMax=', firstMax)
    for secondMax in sortLst[1:len(sortLst)]: # ищем со второго элемента в списке и до конца второе максимальное число
        if secondMax < firstMax:
            # второе минимальное найдено
            # print('secondMax=', secondMax)
            break

    return set(lst[lst.index(secondMax):-1])


def setGenerator_004(dset):
    '''
        Практика 1, Слайд 6 , Задание 4
        Выбрать из пункта 2 только те значения, индексы (ключи) которых в остатке от деления на 3 дают 1.
    '''

    lst = list(dset)
    sublst = []
    for i in range(len(lst)):
        if i % 3 == 1:
            sublst.append(lst[i])

    return set(sublst)


def setGenerator_005(dset):
    '''
        Практика 1, Слайд 6 , Задание 5
        Выбрать из пункта 2 любую треть чисел (округляя по правилам округления)

        Выберем первую треть :)
    '''
    lst = list(dset)
    return set(lst[0:round(len(lst)/3)])


myset = setGenerator_001(int(input("Введите количество элементов n=")))
print("\nИсходный сгенерированный сет:\n", myset)

myset = setGenerator_002(myset)
print("\nМножество с продублированными значениями и увеличением на +1:\n", myset)

subset = setGenerator_003(myset)
print("\nМножество от (первого вхождения в список) второго по убыванию числа и до предпоследнего числа:\n", subset)

subset = setGenerator_004(myset)
print("\nСписок индексы (ключи) которых в остатке от деления на 3 дают 1:\n", subset)

subset = setGenerator_005(myset)
print("\nПервая треть чисел из множества:\n", subset)
print("-- всего чисел в выборке:\n", len(subset), " из ", len(myset))