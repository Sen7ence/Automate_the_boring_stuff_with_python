theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' ', }  # 位置


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


turn = 'X'
for i in range(9):  # 9次机会
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')  # 输入填入位置
    move = input()
    theBoard[move] = turn  # 指定位置更改
    # 变换玩家
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)
