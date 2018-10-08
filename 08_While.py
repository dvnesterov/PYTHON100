def kvadratDvoikiRunner_001(ctrlkm=1000):
    '''
        Практика 1, Слайд 8 (While. Спортивный слайд)
        Задание 1
        Каждый день я пробегаю «следующий квадрат двойки» км. Сколько дней пройдет, пока я в сумме пробегу 1000 км? 1000?
    '''

    totalkm = 0
    days = 0
    while totalkm < ctrlkm:
        days += 1
        km = 2**days
        totalkm += km
        print(days, km, totalkm)

    return days


def primeRunner_002(clrlkm=1000):
    '''
        Практика 1, Слайд 8 (While. Спортивный слайд)
        Задание 2
        Каждый день я пробегаю «следующее простое число» км. Сколько дней пройдет, пока я в сумме пробегу 1000 км? 1000?
    '''

    totalkm = 1
    days = 1
    km = 1
    print(days, km, totalkm)

    while totalkm < clrlkm:
        isPrime = False
        while not isPrime:
            km += 1
            isPrime = True
            for i in range(2, int(km/2)):
                if km % i ==0:
                    isPrime = False
                    break
            totalkm += km
            days += 1
            print(days, km, totalkm)

    return days


def FifteenPercentRunner_003(clrldays=30):
    '''
        Практика 1, Слайд 8 (While. Спортивный слайд)
        Задание 3
        Начав тренировки, спортсмен в первый день пробежал 10 км.
        Для увеличения выносливости ему необходимо повышать норму бега через одну тренировку на 15% от нормы предыдущей тренировки.
        Спортсмен трени­руется каждый день. Какой суммарный путь он пробежит за 30 дней
    '''

    day = 1
    km = 10
    totalkm = km
    print(day, km, totalkm)

    day = 2
    while day <= 30:
        if day % 2 != 0:
            km += km*0.15
        totalkm += km
        print(day, km, totalkm)
        day += 1

    return totalkm


def TenPercentRunner_004(clrlDayKm=20, ctrlTotalKm=100):
    '''
        Практика 1, Слайд 8 (While. Спортивный слайд)
        Задание 4
        Начав тренировки, спортсмен в первый день пробежал  10 км.
        Каждый следующий день он увеличивал дневную норму на 10% от нормы предыдущего дня. Через сколько дней:
            а) спортсмен будет пробегать в день больше 20 км;
            b) пробежит суммарный путь 100 км.
    '''
    day = 1
    km = 10
    totalKm = km
    print(day, km, totalKm)

    run20 = True
    run1e = True
    day = 2
    d20 = 0
    d1e = 0
    while run20 or run1e:
        km += km * 0.1
        totalKm += km
        print(day, km, totalKm)

        if (km > clrlDayKm) and (d20 == 0):
            d20 = day
            print('d20=', d20)
            run20 = False

        if (totalKm >= ctrlTotalKm) and (d1e == 0):
            d1e = day
            print('d1e=', d1e)
            run1e = False

        day += 1


#kvadratDvoikiRunner_001()
#primeRunner_002()
#FifteenPercentRunner_003()
TenPercentRunner_004()