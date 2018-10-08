'''
    Практика 1, Слайд 12 , Задание 5 -6
    Практика 1, Слайд 13 , Задание 1 -8
    Практика 1, Слайд 14 , Задание 1 -2
    Input: число в системе счисления baseFrom
    output: число в системе счисления baseTo
    baseFrom -> baseTo
'''

def conv_lowns2dec(n, baseFrom):
    '''
        Input: число в системе счисления baseFrom размерности 2 .. 9
        output: число в десятичной системе счисления
        baseFrom -> 10
    '''

    le = len(n)
    lst = list(n)
    pwr = []
    for x in lst:
        pwr.append(int(x))
    print(pwr)

    pos = 0
    result=0
    for x in pwr:
        pos += 1
        pwr[pos-1] = x*(baseFrom**(le-pos))
        result += pwr[pos-1]
    print(pwr)

    print("dig (baseFrom="+str(baseFrom)+"):" + n + " => dec:" + str(result))

    return result


def conv_highns2dec(num, baseFrom):
    '''
        Input: число в системе счисления baseFrom размерности 11 .. 36
        output: число в десятичной системе счисления
        baseFrom -> 10
    '''

    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    abclst = []
    cou = 0
    for i in alphabet:
        abclst.append([alphabet[cou], cou])
        cou += 1
    ref = dict(abclst)

    le = len(num)
    lst = list(num)
    print(lst)

    pwr = []
    pos = 0
    result=0
    for x16 in lst:
        pos += 1
        x10=ref[x16]
        pwr.append(x10*(baseFrom**(le-pos)))
        result += pwr[pos - 1]
    print(pwr)
    print(result)

    return result


def convert_base(snum, baseTo=10, baseFrom=10):
    # проверяем исходную систему счисления и приводим исходную систему счисления к десятичной
    if baseFrom <10:
        # n = int(snum, baseFrom)
        n = conv_lowns2dec(snum, baseFrom)
    elif baseFrom >10:
        n = conv_highns2dec(snum, baseFrom)
    else: # исходная система счисления десятичная
        n = int(snum)

    # конвертируем из десятичной в целевую систему счисления baseTo
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < baseTo:
        return alphabet[n]
    else:
        # немного рекурсии :)
        return convert_base(n // baseTo, baseTo) + alphabet[n % baseTo]



# test 1
#conv_lowns2dec("11111100010", baseFrom=2)
# test 2
#conv_lowns2dec("3742", baseFrom=8)
# test 3
#conv_highns2dec("7E2", baseFrom=16)
# test 3
#res = convert_base("11111100010", baseTo=3, baseFrom=2)
#print(res)
# test 5
#res = convert_base("11111100010", baseTo=16, baseFrom=2)
#print(res)

runit = True
while runit:
    num = input ("Введите исходное число: ")
    nsFrom = int(input ("Введите размерность системы счисления исходного числа [2..36]: "))
    nsTo = int(input ("Введите размерность системы счисления результата [2..36]: "))

    res = convert_base(num, nsTo, nsFrom)
    print("Результат: ", res)

    runit = (input ("Продолжить? [0 - выход] :") != "0")