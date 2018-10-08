def conv_dec2bin_001(d):
    '''
        Практика 1, Слайд 12 , Задание 1
        Input: число в десятеричной системе счисления
        output: число в двоичной системе счисления
        10 -> 2
    '''

    # словарь соответсвия чисел. Можно сделать для систем счисления свыще 16
    ref2 = {0:'0', 1:'1'}

    result = ""
    memd = d

    while d != 0:
        r = d % 2
        d = d // 2
        result += ref2[r]
        print (r, d, ref2[r])

    print(result)
    result = result[::-1]
    print("dec :" + str(memd) + " => bin " + result)


def conv_bin2dec_002(n):
    '''
        Практика 1, Слайд 12 , Задание 2
        Input: число в двоичной системе счисления
        output: число в десятичной системе счисления
        2 -> 10
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
        pwr[pos-1] = x*(2**(le-pos))
        result += pwr[pos-1]
    print(pwr)

    print("bin:" + n + " => dec:" + str(result))


def conv_hex2dec_003(hexnum):
    '''
        Практика 1, Слайд 12 , Задание 3
        Input: число в шестнадцатеричной системе счисления
        output: число в десятичной системе счисления
        16 -> 10
    '''
    ref16to10 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                 'A': 10, 'B': 11, 'C' : 12, 'D' : 13, 'E': 14, 'F': 15}

    le = len(hexnum)
    lst = list(hexnum)
    print(lst)

    pwr = []
    pos = 0
    result=0
    for x16 in lst:
        pos += 1
        x10=ref16to10[x16]
        pwr.append(x10*(16**(le-pos)))
        result += pwr[pos - 1]
    print(pwr)
    print(result)

    return result

def conv_dec2hex_004(decnum):
    '''
        Практика 1, Слайд 12 , Задание 4
        10 -> 16
    '''

    # словарь соответсвия чисел. Можно сделать для систем счисления свыще 16
    ref10to16 = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9',
         10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

    base = 16
    result = ""
    memd = decnum

    while decnum != 0:
        r = decnum % base
        decnum = decnum // base
        result += ref10to16[r]
        print (r, decnum, ref10to16[r])

    print(result)
    result = result[::-1]
    print("dec :" + str(memd) + " => hex: " + result)


# 1
d = int(input ("dec->bin: Введите dec-число: "))
conv_dec2bin_001(d)

# 2
b = input ("bin->dec: Введите bin-число: ")
conv_bin2dec_002(b)

# 3
hexnum = input ("hex->dec Введите hex-число: ")
conv_hex2dec_003(hexnum)

# 4
decnum = int(input ("dec->hex Введите dec-число: "))
conv_dec2hex_004(decnum)


