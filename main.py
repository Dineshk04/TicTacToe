import random

board = [' ' for x in range(10)]


def printletter(letter, pos):
    board[pos] = letter


def spacefree(pos):
    return board[pos] == ' '


def printboard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print("------------")
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print("-------------")
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')


def boardfull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def winner(b, l):
    return ((b[1] == l and b[2] == l and b[3] == l) or (b[4] == l and b[5] == l and b[6] == l) or (
            b[7] == l and b[8] == l and b[9] == l) or (b[1] == l and b[4] == l and b[7] == l) or (
                   b[2] == l and b[5] == l and b[8] == l) or (b[3] == l and b[6] == l and b[9] == l) or (
                   b[1] == l and b[5] == l and b[9] == l) or (b[3] == l and b[5] == l and b[7] == l))


def playermove():
    run = True
    while run:
        move = input("Enter a number between (1-9)")
        try:
            move = int(move)
            if 0 < move < 10:
                if spacefree(move):
                    run = False
                    printletter('X', move)
                else:
                    print("Space is occupied")
            else:
                print("Enter a number between (1-9)")

        except:
            print("Enter a number!")


def aimove():
    possiblemoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possiblemoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if winner(boardcopy, let):
                move = i
                move = int(move)
                return move

    cornersopen = []
    for i in possiblemoves:
        if i in [1, 3, 7, 9]:
            cornersopen.append(i)

    if len(cornersopen) > 0:
        move = selectrandom(cornersopen)
        move = int(move)
        return move

    if 5 in possiblemoves:
        move = int(5)
        return move

    edgesopen = []
    for i in possiblemoves:
        if i in [2, 4, 6, 8]:
            edgesopen.append(i)

    if len(edgesopen) > 0:
        move = selectrandom(edgesopen)
        move = int(move)
        return move


def selectrandom(li):
    n = len(li)
    r = random.randrange(0, n)
    return li[r]


def play():
    print("Welcome to the game!")
    printboard(board)

    while not(boardfull(board)):
        if not (winner(board, 'O')):
            playermove()
            printboard(board)
        else:
            print("You loose!")
            break

        if not(winner(board, 'X')):
            move = aimove()
            if move == 0:
                print(" ")
            else:
                if move is not None:
                    printletter('O', move)
                    printboard(board)
                    print('The computer place O in position ', move, ':')
        else:
            print("You Win!")
            break

        if boardfull(board):
            print("Tie game!")


while True:
    x = input("Do you want to play?(y/n)")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print("---------------------")
        play()
    else:
        break




