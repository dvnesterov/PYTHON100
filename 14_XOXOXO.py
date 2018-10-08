"""
Написать реализацию игры крестики нолики
Два человека
Один компьютер
Задание хода – координатами в консоль
Вывод «доски» после каждого хода
Проверка допустимости хода
Проверка условий победы
"""

rowset = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":8}
rowsetrev = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 8:"H"}
table = []
xsize = 3
ysize = 3
X = 1
O = 2
E = 0
currPlayer = X


def initTable():
    global currPlayer
    table = [[0 for _ in range(xsize)] for _ in range(ysize)]

    currPlayer = X

    return table


def drawCell(cell):
    if cell == X:
        xo = "[X]"
    elif cell == O:
        xo = "[O]"
    else:
        xo = "[ ]"
    print(xo ,end='')

def drawHdrXY(pos):
    if pos == 0:
        print("   ", end='')

    xo = "["+str(pos)+"]"
    print(xo ,end='')

def changePlayer():
    global currPlayer
    if currPlayer == X:
        currPlayer=O
    else:
        currPlayer=X



def drawTable():
    abc = ("A", "B", "C", "D", "E", "F", "G", "H")

    #print("\n")

    for row in range(xsize):
        drawHdrXY(row)
    print('', end='\n')

    i = 0
    for row in table:
        print("["+abc[i]+"]", end='')
        i += 1
        for c in row:
            drawCell(c)
        print('', end='\n')

def chkCell(row, col):
    print('rc', row, col)
    if row < 0 or row > ysize:
        return False
    elif col < 0 or col > xsize:
        return False
    elif table[row][col] != E:
        return False
    else:
        return True

def writeCell(row, col):
    table[row][col] = currPlayer
    changePlayer()
    return table

def checkOnWin():

    def chkCount(winline):
        isWin = False
        if winline == "@ROW":
            wininfo = winline + ":" + rowsetrev[yrow]
        elif winline == "@COL":
            wininfo = winline + ":" + str(xcol)
        elif winline == "@DIAG-A0C2":
            wininfo = winline
        elif winline == "@DIAG-C0A2":
            wininfo = winline

        if playerX == xsize:
            print("PLAYER-X WIN!!! ", wininfo)
            isWin = True
        elif playerO == xsize:
            print("PLAYER-O WIN!!! ", wininfo)
            isWin = True
        return isWin

    playerWin = False

    # проверяем rows
    for yrow in range(ysize):
        playerX = 0
        playerO = 0
        for xcol in range(xsize):
            if table[yrow][xcol] == X:
                playerX += 1
            elif table[yrow][xcol] == O:
                playerO += 1
        ret = chkCount("@ROW")
        if not playerWin:
            playerWin = ret

    # проверяем cols
    for xcol in range(xsize):
        playerX = 0
        playerO = 0
        for yrow in range(ysize):
            if table[yrow][xcol] == X:
                playerX += 1
            elif table[yrow][xcol] == O:
                playerO += 1

        ret = chkCount("@COL")
        if not playerWin:
            playerWin = ret


    # проверяем diag a0c2
    playerX = 0
    playerO = 0
    for xcol in range(xsize):
        yrow = xcol
        if table[yrow][xcol] == X:
            playerX += 1
        elif table[yrow][xcol] == O:
            playerO += 1

        ret = chkCount("@DIAG-A0C2")
        if not playerWin:
            playerWin = ret

    # проверяем diag c0a2
    playerX = 0
    playerO = 0
    for xcol in range(xsize):
        yrow = ysize - xcol -1
        if table[yrow][xcol] == X:
            playerX += 1
        elif table[yrow][xcol] == O:
            playerO += 1

        ret = chkCount("@DIAG-C0A2")
        if not playerWin:
            playerWin = ret

    return playerWin

def run(rdata):
    #print(rdata)
    cy = rowset[rdata[0]]
    cx = int(rdata[1])
    if chkCell(cy, cx):
        writeCell(cy, cx)
    else:
        print("\nОШИБКА: проверьте свой ход (неверные координаты или ячейка уже была записана ранее)")
    drawTable()
    ret = checkOnWin()
    return not ret


isPlayOn = True
while isPlayOn:
    table = initTable()
    drawTable()
    isRoundOn = True
    while  isRoundOn:
        rdata = list(input("\n[Игрок #"+str(currPlayer)+"]\nВаш ход (формат A0..C2) ->").upper())
        isRoundOn = run(rdata)

    isPlayOn = input("Начать новую партию? [0 - Exit 1 - Continue]") != '0'

print("*** ~^ GAME OVER ! ^~ ***")