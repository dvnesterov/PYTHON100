import numpy as np
import math

def createArray():
    '''
        Практика NumPy, Задание 1
        Создать массив рандомных чисел
    '''
    #
    a = np.random.randint(0, 100, 100)
    print(a)
    return a


def midVal(a):
    '''
        Практика NumPy, Задание 2
        Посчитать среднее значение
    '''
    i = 0
    tot = 0
    for x in a:
        tot += x
        i += 1
    m = tot / i
    print('m=', m)
    return  m, i

def sigma(a, mi):
    '''
        Практика NumPy, Задание 3
        Посчитать стандартное отклонение по формуле сигма = корень((сумма (x - x_среднее)^2) / длина_массива)
    '''

    z = 0
    for x in a:
        z += (x - mi[0])**2

    sig = math.sqrt(z/mi[1])
    return sig


def sysEq():
    '''
        Практика NumPy, Задание 4
        Найти решение системы уравнений
        3 * x0 + x1 = 9
        x0 + 2 * x1 = 8
    '''

    M1 = np.array([[3.0, 1.0], [1.0, 2.0]]) # Матрица (левая часть системы)
    v1 = np.array([9.0, 8.0]) # Вектор (правая часть системы)
    result=np.linalg.solve(M1, v1)

    return result



# 1
myArr = createArray()
# 2
mi = midVal(myArr)
print(mi)
# 3
sig = sigma(myArr,mi)
print('sigma=', sig)
# 4
answ=sysEq()
print('(x,y)=', answ)