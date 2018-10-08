def strGenerator_001(n=0, s=''):
    '''
        Практика 1, Слайд 7 (Составные типы. Строки)
        Задание 1
        input: натуральное число n и строку s. 
        output: этa строкa n раз.
    '''

    return s*n


def porchGenerator_002(n=3):
    '''

        Практика 1, Слайд 7 (Составные типы. Строки)
        Задание 2
        input: натуральное число N.
        output: "крылечко" из знаков "=": в первой строке 1, во второй 2, в N-й N
    '''

    for i in range(1, n):
        print("="*i)


def letterCounter_003(s=''):
    '''
        Практика 1, Слайд 7 (Составные типы. Строки)
        Задание 3
        input: строка
        output: сколько раз каждая буква встречалась в строке
    '''
    myletters = {}
    for a in s:
        if a in myletters:
            myletters[a] += 1
        else:
            myletters[a] = 1

    return myletters


def wordsLengthCounter_004(s=''):
    '''
        Практика 1, Слайд 7 (Составные типы. Строки)
        Задание 4
        input: предложение (строка)
        output: распределение длин слов
    '''
    mywords = s.split(' ')

    mywordslen = []
    for w in mywords:
        mywordslen.append(len(w))

    mywordslen = sorted(mywordslen)
    lendict = {}

    for x in mywordslen:
        if x in lendict:
            lendict[x] += 1
        else:
            lendict[x] = 1
    return lendict


print("\nПрактика 1, Слайд 7 , Задание 1\nПовторение фрагмента текста\n")
print("Результат:", strGenerator_001(input('Введите текст:'), int(input('Число повторений:'))))

print("\nПрактика 1, Слайд 7 , Задание 2\nПостроитель лесенки\n")
porchGenerator_002(5)

print("\nПрактика 1, Слайд 7 , Задание 3\nПодстчет букв в строке\n")
d=letterCounter_003(input('Введите текст:'))
print(d)

print("\nПрактика 1, Слайд 7 , Задание 4\nРаспределение длин слов\n")
d=wordsLengthCounter_004(input('Введите текст:'))
print(d)
