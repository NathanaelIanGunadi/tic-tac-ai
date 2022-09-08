import random
import time

z = '_________'
wins = 0
blanks = 0
text = ''
turn_count = 1
column_win = False
exit_break = False
scores = {}


def med_ai(a):
    xc = random.randint(1, 3)
    yc = random.randint(1, 3)
    hard = False
    # column
    for i in range(3):
        c = [a[i], a[i + 3], a[i + 6]]
        if (c[0] == "X" and c[1] == "X" or c[0] == "O" and c[1] == "O") and c[2] == "_":
            xc = 3
            yc = i + 1
            hard = True
            break
        elif (c[0] == "X" and c[2] == "X" or c[0] == "O" and c[2] == "O") and c[1] == "_":
            xc = 2
            yc = i + 1
            hard = True
            break
        elif (c[2] == "X" and c[1] == "X" or c[2] == "O" and c[1] == "O") and c[0] == "_":
            xc = 1
            yc = i + 1
            hard = True
            break
    # row
    count = 1
    for i in range(0, 7, 3):

        if (a[i] == "X" and a[i + 1] == "X" or a[i] == "O" and a[i + 1] == "O") and a[i + 2] == "_":
            xc = count
            yc = 3
            hard = True
            break
        elif (a[i] == "X" and a[i + 2] == "X" or a[i] == "O" and a[i + 2] == "O") and a[i + 1] == "_":
            xc = count
            yc = 2
            hard = True
            break
        elif (a[i + 2] == "X" and a[i + 1] == "X" or a[i + 2] == "O" and a[i + 1] == "O") and a[i] == "_":
            xc = count
            yc = 1
            hard = True
            break

        count += 1

    if (a[0] == "X" and a[4] == "X" or a[0] == "O" and a[4] == "O") and a[8] == "_":
        xc = 3
        yc = 3
        hard = True
    elif (a[8] == "X" and a[4] == "X" or a[8] == "O" and a[4] == "O") and a[0] == "_":
        xc = 1
        yc = 1
        hard = True
    elif (a[2] == "X" and a[4] == "X" or a[2] == "O" and a[4] == "O") and a[6] == "_":
        xc = 3
        yc = 1
        hard = True
    elif (a[6] == "X" and a[4] == "X" or a[6] == "O" and a[4] == "O") and a[2] == "_":
        xc = 1
        yc = 3
        hard = True
    elif (a[0] == "X" and a[8] == "X" or a[0] == "O" and a[8] == "O") and a[4] == "_":
        xc = 2
        yc = 2
        hard = True
    elif (a[2] == "X" and a[6] == "X" or a[2] == "O" and a[6] == "O") and a[4] == "_":
        xc = 2
        yc = 2
        hard = True

    return xc, yc, hard


def is_end(board):
    # Vertical win
    for i in range(0, 3):
        if (board[0][i] != '_' and
            board[0][i] == board[1][i] and
            board[1][i] == board[2][i]):
            return board[0][i]

    # Horizontal win
    for i in range(0, 3):
        if board[i] == ['X', 'X', 'X']:
            return 'X'
        elif (board[i] == ['O', 'O', 'O']):
            return 'O'

    # Main diagonal win
    if (board[0][0] != '_' and
        board[0][0] == board[1][1] and
        board[0][0] == board[2][2]):
        return board[0][0]

    # Second diagonal win
    if (board[0][2] != '_' and
        board[0][2] == board[1][1] and
        board[0][2] == board[2][0]):
        return board[0][2]

    # Is whole board full?
    for i in range(0, 3):
        for j in range(0, 3):
            # There's an empty field, we continue the game
            if (board[i][j] == '_'):
                return None

    # It's a tie!
    return 'tie'


def loop_max(board):

    loop_maxv = -2

    px = None
    py = None

    result = is_end(board)

    if result == "X":
        return (1, 0, 0)
    elif result == "tie":
        return (0, 0, 0)
    elif result == "O":
        return (-1, 0, 0)

    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                board[i][j] = "X"

                (evaluation, loop_min_i, loop_min_j) = loop_min(board)

                if evaluation > loop_maxv:
                    loop_maxv = evaluation
                    px = i
                    py = j


                board[i][j] = "_"
    return (loop_maxv, px, py)


def loop_min(board):

    loop_minv = 2

    qx = None
    qy = None

    result = is_end(board)

    if result == "X":
        return (1, 0, 0)
    elif result == "tie":
        return (0, 0, 0)
    elif result == "O":
        return (-1, 0, 0)

    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                board[i][j] = "O"

                (evaluation, loop_max_i, loop_max_j) = loop_max(board)

                if evaluation < loop_minv:
                    loop_minv = evaluation
                    qx = i
                    qy = j

                board[i][j] = "_"

    return (loop_minv, qx, qy)


def x_player(player):
    if player == "user":
        miss = False
        while True:
            numbers = list('0123456789')
            cont = input('Enter the coordinates:')
            input_coords = cont.split()

            for i in input_coords:
                if i not in numbers:
                    print('You should enter numbers!')
                    miss = True
                    break
                else:
                    i = int(i)
                    if i > 3 or i < 1:
                        print('Coordinates should be from 1 to 3!')
                        miss = True
                        break

            if miss:
                miss = False
                continue

            try:
                xc = int(input_coords[0])
                yc = int(input_coords[1])
            except IndexError:
                print('Wrong Input')
                miss = True
            else:
                xc = int(input_coords[0])
                yc = int(input_coords[1])

            if miss:
                miss = False
                continue

            if coords[xc - 1][yc - 1] != '_':
                print('This cell is occupied, choose another one:')
                continue
            else:
                coords[xc - 1][yc - 1] = 'X'
                break

    elif player == "easy":
        print('Making move level "easy"')
        xc = random.randint(1, 3)
        yc = random.randint(1, 3)
        while True:
            if coords[xc - 1][yc - 1] != '_':
                xc = random.randint(1, 3)
                yc = random.randint(1, 3)
            elif coords[xc - 1][yc - 1] == '_':
                coords[xc - 1][yc - 1] = 'X'
                break

    elif player == "medium":
        print('Making move level "medium"')
        time.sleep(0.5)
        while True:
            xc, yc, hard = med_ai(a)
            if coords[xc - 1][yc - 1] != '_':
                med_ai(a)
            elif coords[xc - 1][yc - 1] == '_':
                coords[xc - 1][yc - 1] = 'X'
                break

    elif player == "hard":
        print('Making move level "hard"')
        time.sleep(0.5)
        result, xc, yc = loop_max(coords)
        time.sleep(0.5)
        coords[xc][yc] = "X"


def o_player(player):
    if player == "user":
        miss = False
        while True:
            numbers = list('0123456789')
            cont = input('Enter the coordinates:')
            input_coords = cont.split()

            for i in input_coords:
                if i not in numbers:
                    print('You should enter numbers!')
                    miss = True
                    break
                else:
                    i = int(i)
                    if i > 3 or i < 1:
                        print('Coordinates should be from 1 to 3!')
                        miss = True
                        break

            if miss:
                miss = False
                continue

            try:
                xc = int(input_coords[0])
                yc = int(input_coords[1])
            except IndexError:
                print('Wrong Input')
                miss = True
            else:
                xc = int(input_coords[0])
                yc = int(input_coords[1])

            if miss:
                miss = False
                continue

            if coords[xc - 1][yc - 1] != '_':
                print('This cell is occupied, choose another one:')
                continue
            else:
                coords[xc - 1][yc - 1] = 'O'
                break

    elif player == "easy":
        print('Making move level "easy"')
        time.sleep(0.5)
        xc = random.randint(1, 3)
        yc = random.randint(1, 3)
        while True:
            if coords[xc - 1][yc - 1] != '_':
                xc = random.randint(1, 3)
                yc = random.randint(1, 3)
            elif coords[xc - 1][yc - 1] == '_':
                coords[xc - 1][yc - 1] = 'O'
                break

    elif player == "medium":
        print('Making move level "medium"')
        time.sleep(0.5)
        while True:
            xc, yc, hard = med_ai(a)
            if coords[xc - 1][yc - 1] != '_':
                med_ai(a)
            elif coords[xc - 1][yc - 1] == '_':
                coords[xc - 1][yc - 1] = 'O'
                break

    elif player == "hard":
        print('Making move level "hard"')
        result, xc, yc = loop_min(coords)
        time.sleep(0.5)
        coords[xc][yc] = "O"

while True:
    blanks = 0

    a = []
    for char in z:
        a.append(char)

    for x in z:  # count blanks
        if x == '_':
            blanks += 1

    first = a[0:3]
    firstp = ' '.join(first)
    second = a[3:6]
    secondp = ' '.join(second)
    third = a[6:9]
    thirdp = ' '.join(third)

    # coordinate matrix
    coords = [first,
              second,
              third]

    if turn_count == 1:
        while True:
            start_menu = input("Input command:")
            start_menu = start_menu.split()

            if start_menu[0] == "start":
                if len(start_menu) != 3:
                    print("Bad parameters!")
                    continue
                else:
                    break
            elif start_menu[0] == "exit":
                exit_break = True
                break

        if exit_break:
            break

        print(f"""---------
| {firstp} |
| {secondp} |
| {thirdp} |
---------""")

    # same column

    for i in range(3):
        c = [a[i], a[i + 3], a[i + 6]]
        if c[0] == c[1] and c[1] == c[2]:
            if c[0] == 'O':
                text = 'O wins'
                print(text)
                column_win = True
                wins += 1
                break
            if c[0] == 'X':
                text = 'X wins'
                print(text)
                column_win = True
                wins += 1
                break

    # same row

    if z[0] == z[1] and z[1] == z[2]:
        if z[0] == 'O':
            text = 'O wins'
            print(text)
            break
            wins += 1
        if z[0] == 'X':
            text = 'X wins'
            print(text)
            break
            wins += 1

    if a[3] == a[4] and a[4] == a[5]:
        if a[4] == 'O':
            text = 'O wins'
            print(text)
            break
            wins += 1
        if a[4] == 'X':
            text = 'X wins'
            print(text)
            break
            wins += 1

    if a[6] == a[7] and a[7] == a[8]:
        if a[6] == 'O':
            text = 'O wins'
            print(text)
            break
            wins += 1
        if a[6] == 'X':
            text = 'X wins'
            print(text)
            break
            wins += 1

    # diagonal

    if a[0] == a[4] and a[4] == a[8] or a[2] == a[4] and a[4] == a[6]:
        if a[4] == 'O':
            text = 'O wins'
            print(text)
            wins += 1
            break
        if a[4] == 'X':
            text = 'X wins'
            print(text)
            wins += 1
            break

    if blanks == 0 and wins == 0:
        text = 'Draw'
        print(text)
        break

    counto = 0
    countx = 0

    for x in a:
        if x == 'O':
            counto += 1
        if x == 'X':
            countx += 1

    if column_win:
        break

    if turn_count % 2 == 1:
        x_player(start_menu[1])
    else:
        o_player(start_menu[2])

    firstp = ' '.join(first)
    secondp = ' '.join(second)
    thirdp = ' '.join(third)

    print(f"""---------
| {firstp} |
| {secondp} |
| {thirdp} |
---------""")
    str_ = ""
    z = str_.join(first) + str_.join(second) + str_.join(third)

    turn_count += 1