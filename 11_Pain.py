def monetochka_001(a=3, x=5, b=3, y=2, z=16):
    '''
        Практика 1, Слайд 11 , Задание 1
        У Вас А монет по Х рублей и В монет по Y рублей. Можно ли с их помощью заплатить Z рублей, если да - то как?
    '''

    n = 0
    for i in range(a+1):
        for j in range(b+1):
            if x * i + y * j == z:
                n += 1
                sx = str(i) + " по " + str(x) if i > 0 else ""
                sy = str(j) + " по " + str(y) if j > 0 else ""
                print(sx, (" + " + sy) if sx != "" and  sy !="" else sy)
    if n ==0:
        print("Заплатить нельзя")


def razryady_002(n=0):
    '''
        Практика 1, Слайд 11 , Задание 2
        Вводится целое число. Вывести на экран количество разрядов в нем.
    '''

    r = 0
    while n > 0:
        r += 1
        n = n // 10

    print('r=', r)


def palyndrom_003(s=""):
    '''
        Практика 1, Слайд 11 , Задание 3
        input: строка
        ouput: Определить является ли она палиндромом и вывести соответствующее сообщение.
    '''

    print(s)
    if s == s[::-1]:
        print("Это пaлиндром")
    else:
        print("Это НЕ пaлиндром")


def mysubst_004(origstr, oldstr, newstr):
    '''
        Практика 1, Слайд 11 , Задание 3
        В строке найти и заменить одну подстроку на другую. Если одинаковых подстрок несколько, заменить все
    '''

    origstr = origstr.replace(oldstr, newstr)
    print(origstr)



#1
monetochka_001(z=16)
#2
razryady_002(1234567)

#3
palyndrom_003("123456")
palyndrom_003("12321")

#4
mysubst_004("1234567890345999", "345", "XXX")