import numpy as np


def GuessTheNumber(maxIteration=10):
    '''
        Практика 1, Слайд 10 , Задание 1-3
        Автор задумывает число (натуральное, из интервала от 1 до 100).
        Пользователь это число отгадывает: вводит свои варианты, получает ответы "больше, "меньше" или "да, это оно".
        
        Реализован: 
        Уровень 3: у пользователя есть лимит в 50 ходов на все партии, пока он его не исчерпал - играет. 
        Ведётся подсчёт законченных партий
        
        Улучшение: автор задумывает число с помощью ГСЧ
    '''

    secdig = int(np.random.randint(0, 101))
    print(secdig) # подсказка ;)

    iTot = 1
    att = 1
    partNum = 1
    x = 0
    playon = True

    while playon:
        while (x != secdig) and (iTot<=maxIteration):
            legend = "[I:" + str(iTot) + " из " + str(maxIteration) + "][P:" + str(partNum) + "][A:" + str(att) + "] "
            x = int(input((legend + "Ваш вариант:")))
            if x == secdig:
                print(legend, 'ДА! Вы угадали число! Это ', x)
            elif x < secdig:
                print(legend, 'Загаданное число БОЛЬШЕ, чем ', x)
            else:
                print(legend, 'Загаданное число МЕНЬШЕ, чем ', x)
            att += 1
            iTot += 1

        if iTot > maxIteration:
            print('Превышено максимальное число итераций в играх: maxIteration=', str(maxIteration))
            playon = False
        else:
            if input('Будем угадывать следующее число? [0/1] ') == "1":
                secdig = int(np.random.randint(0, 101))
                print(secdig) # подсказка ;)
                partNum += 1
                att = +1
                x = 0

            else:
                playon = False

    print('*** ^~^ GAME OVER ^~^ ***')


GuessTheNumber()

