def NthMembetOfSeq_001(n=0):
    '''
        Практика 1, Слайд 9 , Задание 1
        Найти N-й член последовательности 1, 1, 2, 3, 5, 8, 13...
    '''

    a = [1, 1]
    if n <= 1:
        return a[n]

    for i in range(1, n):
        a.append(a[i]+a[i-1])
        print(a)

    return a[-1]


def NthMembetOfSeq_002(n=0):
    '''
        Практика 1, Слайд 9 , Задание 2
        Найти N-й член последовательности 1, 1, 1, 3, 5, 9, 17…
    '''

    a = [1, 1, 1]
    if n <= 2:
        return a[n]

    for i in range(2, n):
        a.append(a[i]+a[i-1]+a[i-2])
        print(a)

    return a[-1]


def OddsPower_003(n=0):
    '''
        Практика 1, Слайд 9 , Задание 3
        Вывести квадраты нечетных чисел до N
    '''
    lst=[]
    for i in range(1, n, 2):
        lst.append(i**2)

    return lst


def StarFrame_004(a=5, b=5):
    '''
       Практика 1, Слайд 9 , Задание 4
       Вывести прямоугольную рамочку из звёздочек, шириной А звёздочек и высотой В.
    '''

    for y in range(1,b+1):
        if y == 1 or y == b:
            print ("*"*a, end="\n")
        else:
            print("*" + " " * (a-2) + "*", end="\n")


def SumNaturalNums_005(a=0, b=10):
    '''
       Практика 1, Слайд 9 , Задание 5
       Вычислить сумму и произведение всех натуральных чисел от А до В включительно.
    '''

    prod=1
    sum = 0
    for i in range(a,b+1):
        prod *= i
        sum += i
        print(i, prod, sum)

    print("prod=", prod)
    print("sum=", sum)


def Selection_006(a=0, b=10):
    '''
       Практика 1, Слайд 9 , Задание 6
       Даны натуральные числа А и В. Вывести сначала все чётные числа, заключённые между ними, потом все нечётные
    '''
    odds = []
    even = []

    if a % 2 == 0:
        # соответсвенно, первое число "между" будет нечетным
        for x in range(a+1, b, 2):
            odds.append(x)
        for x in range(a + 2, b, 2):
            even.append(x)
    else:
        # соответсвенно, первое число "между" будет четным
        for x in range(a+1, b, 2):
            even.append(x)
        for x in range(a + 2, b, 2):
            odds.append(x)

    print("Четные:\n", even)
    print("Нечетные:\n", odds)

    # ну и можно еще так, конечно
    even.clear()
    odds.clear()

    for x in range(a+1, b):
        if x % 2 == 0:
            even.append(x)
        else:
            odds.append(x)

    print("*Четные:\n", even)
    print("*Нечетные:\n", odds)


def Selection_007(lst):
    '''
       Практика 1, Слайд 9 , Задание 7
       Исходный список содержит положительные и отрицательные числа.
       Требуется положительные поместить в один список, а отрицательные - в другой
    '''

    plus=[]
    minus=[]
    for x in lst:
        if x>0:
            plus.append(x)
        elif x<0:
            minus.append(x)

    print(plus)
    print(minus)


# 1
# result = NthMembetOfSeq_001(10)
# print('result=', result)

# 2
# result = NthMembetOfSeq_002(10)
# print('result=', result)

# 3
# result = OddsPower_003(10)
# print('result:\n', result)

#4
# StarFrame_004()

#5
# a = int(input("a="))
# b = int(input("b="))
# SumNaturalNums_005(a,b)

#6
Selection_006()

#7
Selection_007([2, 4, 7, -66, 2, 5, -54, 0, -76, 6, -42, -45, 3, 9, 7])