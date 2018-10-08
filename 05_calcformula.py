def calculation_001(x, y , z, f):
    """
    Практика 1, Слайд 5 , Задание 1 из 1
    """

    res = (x*(y - x)/z + x + (f + z)/f**y - (z-f)/z) / ((z + f)/z**y -f)
    print('result: ', res)


calculation_001(1, 2, 3, 4)
