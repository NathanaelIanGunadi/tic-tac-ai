import random
import time


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
        elif board[i] == ['O', 'O', 'O']:
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
            if board[i][j] == '_':
                return None

    return 'tie'


# minimax algorithm
def loop_max(board):

    loop_maxv = -2  # set lower than worst possible value

    px = None
    py = None

    result = is_end(board)

    if result == "X":  # best case
        return 1, 0, 0
    elif result == "tie":  # neutral
        return 0, 0, 0
    elif result == "O":  # worst case
        return -1, 0, 0

    for i in range(3):  # looks at all possible values
        for j in range(3):
            if board[i][j] == "_":
                board[i][j] = "X"  # changes a tile to "X" and evaluates result

                evaluation, loop_min_i, loop_min_j = loop_min(board)

                if evaluation > loop_maxv:  # takes best possible move (highest value)
                    loop_maxv = evaluation
                    px = i
                    py = j

                board[i][j] = "_"  # reverts back to original state

    return loop_maxv, px, py


def loop_min(board):

    loop_minv = 2  # set higher than worst possible case

    qx = None
    qy = None

    result = is_end(board)

    if result == "X":  # worst case
        return 1, 0, 0
    elif result == "tie":  # neutral
        return 0, 0, 0
    elif result == "O":  # best case
        return -1, 0, 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                board[i][j] = "O"

                (evaluation, loop_max_i, loop_max_j) = loop_max(board)

                if evaluation < loop_minv:  # takes best possible move (lowest value)
                    loop_minv = evaluation
                    qx = i
                    qy = j

                board[i][j] = "_"

    return loop_minv, qx, qy


class Game:
    def __init__(self):
        self.current = [["_", "_", "_"],
                        ["_", "_", "_"],
                        ["_", "_", "_"]]
        self.next_move = "X"
        self.turn_count = 1

    def reset(self):
        self.current = [["_", "_", "_"],
                        ["_", "_", "_"],
                        ["_", "_", "_"]]
        self.next_move = "X"
        self.turn_count = 1

    def set_options(self):
        while True:
            start_menu = input("Input command:")
            start_menu = start_menu.split()
            options = ["easy", "med", "medium", "hard", "user"]

            if start_menu[0] == "start":
                if len(start_menu) != 3:
                    print("Bad parameters!")
                    continue
                elif start_menu[1] not in options and start_menu[2] not in options:
                    print("Bad parameters!")
                    continue
                else:
                    break
            elif start_menu[0] == "exit":
                break
            else:
                print("Bad parameters!")
                continue

        return start_menu[1], start_menu[2]

    def show_board(self):
        print("---------")
        for row in self.current:
            print("| " + " ".join(row) + " |")
        print("---------")

    def easy_ai(self):
        x = random.randint(0, 2)
        y = random.randint(1, 3)
        while True:
            if self.current[x][y] != '_':
                x = random.randint(0, 2)
                y = random.randint(0, 2)
            else:
                break

        return x, y

    def med_ai(self):
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        extended_board = []
        for row in self.current:
            for i in row:
                extended_board.append(i)

        # column
        for i in range(3):
            c = [extended_board[i], extended_board[i + 3], extended_board[i + 6]]
            if (c[0] == "X" and c[1] == "X" or c[0] == "O" and c[1] == "O") and c[2] == "_":
                x = 3
                y = i + 1
                break
            elif (c[0] == "X" and c[2] == "X" or c[0] == "O" and c[2] == "O") and c[1] == "_":
                x = 2
                y = i + 1
                break
            elif (c[2] == "X" and c[1] == "X" or c[2] == "O" and c[1] == "O") and c[0] == "_":
                x = 1
                y = i + 1
                break
        # row
        count = 1
        for i in range(0, 7, 3):

            if (extended_board[i] == "X" and extended_board[i + 1] == "X" or
                    extended_board[i] == "O" and extended_board[i + 1] == "O") and extended_board[i + 2] == "_":
                x = count
                y = 3
                break
            elif (extended_board[i] == "X" and extended_board[i + 2] == "X" or
                    extended_board[i] == "O" and extended_board[i + 2] == "O") and extended_board[i + 1] == "_":
                x = count
                y = 2
                break
            elif (extended_board[i + 2] == "X" and extended_board[i + 1] == "X" or
                    extended_board[i + 2] == "O" and extended_board[i + 1] == "O") and extended_board[i] == "_":
                x = count
                y = 1
                break

            count += 1

        if (extended_board[0] == "X" and extended_board[4] == "X" or
                extended_board[0] == "O" and extended_board[4] == "O") and extended_board[8] == "_":
            x = 3
            y = 3
        elif (extended_board[8] == "X" and extended_board[4] == "X" or
                extended_board[8] == "O" and extended_board[4] == "O") and extended_board[0] == "_":
            x = 1
            y = 1
        elif (extended_board[2] == "X" and extended_board[4] == "X" or
                extended_board[2] == "O" and extended_board[4] == "O") and extended_board[6] == "_":
            x = 3
            y = 1
        elif (extended_board[6] == "X" and extended_board[4] == "X" or
                extended_board[6] == "O" and extended_board[4] == "O") and extended_board[2] == "_":
            x = 1
            y = 3
        elif (extended_board[0] == "X" and extended_board[8] == "X" or
                extended_board[0] == "O" and extended_board[8] == "O") and extended_board[4] == "_":
            x = 2
            y = 2
        elif (extended_board[2] == "X" and extended_board[6] == "X" or
                extended_board[2] == "O" and extended_board[6] == "O") and extended_board[4] == "_":
            x = 2
            y = 2

        if self.current[x - 1][y - 1] != '_':
            x, y = self.med_ai()
            return x, y
        else:
            return x, y

    def hard_ai(self, symbol):
        if symbol == "X":
            result, x, y = loop_max(self.current)
            return x, y
        else:
            result, x, y = loop_min(self.current)
            return x, y

    def get_user_input(self):
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
                x = int(input_coords[0])
                y = int(input_coords[1])
            except IndexError:
                print('Wrong Input')
                miss = True
            else:
                x = int(input_coords[0])
                y = int(input_coords[1])

            if miss:
                miss = False
                continue

            if self.current[x - 1][y - 1] != '_':
                print('This cell is occupied, choose another one:')
                continue
            else:
                break

        return x - 1, y - 1

    def get_next_move(self, player1, player2):
        if self.turn_count % 2 == 1:
            if player1 == "easy":
                time.sleep(0.5)
                x, y = self.easy_ai()
            elif player1 == "medium":
                time.sleep(0.5)
                x, y = (a - 1 for a in self.med_ai())
            elif player1 == "hard":
                time.sleep(0.5)
                x, y = self.hard_ai(self.next_move)
            else:
                x, y = self.get_user_input()
        else:
            if player2 == "easy":
                time.sleep(0.5)
                x, y = self.easy_ai()
            elif player2 == "medium":
                time.sleep(0.5)
                x, y = (a - 1 for a in self.med_ai())
            elif player2 == "hard":
                time.sleep(0.5)
                x, y = self.hard_ai(self.next_move)
            else:
                x, y = self.get_user_input()

        return x, y

    def plot(self, x, y):
        if self.next_move == "X":
            symbol = "X"
            self.next_move = "O"
            self.current[x][y] = symbol
        else:
            symbol = "O"
            self.next_move = "X"
            self.current[x][y] = symbol
        self.turn_count += 1

    def run(self):
        while True:
            if self.turn_count == 1:
                player1, player2 = self.set_options()
                self.show_board()
            x, y = self.get_next_move(player1, player2)
            self.plot(x, y)
            state = is_end(self.current)
            self.show_board()
            if state == "tie":
                print("Draw!")
                break
            elif state is None:
                continue
            else:
                print(f"{state} Wins!")
                break

        while True:
            cont = input("continue playing? (yes/no)")
            if cont == "no":
                break
            elif cont == "yes":
                self.reset()
                self.run()
            else:
                print("enter 'yes' or 'no'")


tic_tac = Game()
tic_tac.run()
