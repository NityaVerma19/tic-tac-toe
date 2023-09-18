'''
import random, csv, os

print("Welcome!")
print("To make a move, choose any number from 1-9")
demo_board = {"a": "1", "b": "2", "c": "3",
              "d": "4", "e": "5", "f": "6",
              "g": "7", "h": "8", "i": "9"}


def d_board(db):
    print(db["a"] + "|" + db["b"] + "|" + db["c"])
    print("-+-+-")
    print(db["d"] + "|" + db["e"] + "|" + db["f"])
    print("-+-+-")
    print(db["g"] + "|" + db["h"] + "|" + db["i"])


d_board(demo_board)

theBoard = {1: " ", 2: " ", 3: " ",
            4: " ", 5: " ", 6: " ",
            7: " ", 8: " ", 9: " "}


def game(b):
    print(b[1] + "|" + b[2] + "|" + b[3])
    print("-+-+-")
    print(b[4] + "|" + b[5] + "|" + b[6])
    print("-+-+-")
    print(b[7] + "|" + b[8] + "|" + b[9])


def player_letters():
    letter = ""
    while not (letter == "X" or letter == "O"):
        print("Choose a letter, either X or O")
        letter = input().upper()
    if letter == "X":
        return "X", "O"
    else:
        return "O", "X"


def who_goes_first():
    if random.randint(0, 1) == 0:
        return "Computer"
    else:
        return "player"


def make_a_move(board, letter, move):
    board[move] = letter


def is_winner(b, l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
            (b[4] == l and b[5] == l and b[6] == l) or
            (b[7] == l and b[8] == l and b[9] == l) or
            (b[1] == l and b[4] == l and b[7] == l) or
            (b[2] == l and b[5] == l and b[8] == l) or
            (b[3] == l and b[6] == l and b[9] == l) or
            (b[1] == l and b[5] == l and b[9] == l) or
            (b[3] == l and b[5] == l and b[7] == l))


def getboardcopy(board):
    return board.copy()


def empty_space(board, move):
    return board[move] == " "


def get_player_move(board):
    move = " "
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not empty_space(board, int(move)):
        print("What's your next move?")
        move = input()
    return int(move)


def choosemove(board, move_list):
    possible_moves = []
    for i in move_list:
        if empty_space(board, i):
            possible_moves.append(i)
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def get_computer_move(board, comp_letter):
    if comp_letter == "X":
        player_letter = "O"
    else:
        player_letter = "X"

    for i in range(1, 10):
        copy = getboardcopy(board)
        if empty_space(copy, i):
            make_a_move(copy, comp_letter, i)
            if is_winner(copy, comp_letter):
                return i

    for i in range(1, 10):
        copy = getboardcopy(board)
        if empty_space(copy, i):
            make_a_move(copy, player_letter, i)
            if is_winner(copy, player_letter):
                return i

    move = choosemove(board, [1, 3, 7, 9])
    if move is not None:
        return move

    if empty_space(board, 5):  # check the middle
        return 5

    return choosemove(board, [2, 4, 6, 8])  # last option is to move to the sides


def check_board_full(board):
    for i in range(1, 10):
        if empty_space(board, i):
            return False
    return True


score_player = 0
score_computer = 0
score_draw = 0
attempts = 1
while True:
    theBoard = {1: " ", 2: " ", 3: " ",
                4: " ", 5: " ", 6: " ",
                7: " ", 8: " ", 9: " "}

    player_letter, comp_letter = player_letters()
    turn = who_goes_first()
    print("The", turn, "will go first")
    gameIsplaying = True

    while gameIsplaying:
        if turn == "player":
            game(theBoard)
            move = get_player_move(theBoard)
            make_a_move(theBoard, player_letter, move)

            if is_winner(theBoard, player_letter):
                game(theBoard)
                score_player += 1
                print("Congrats! You won the game")
                gameIsplaying = False
            else:
                if check_board_full(theBoard):
                    game(theBoard)
                    print("It's a draw!")
                    break
                else:
                    turn = "computer"
        else:
            move = get_computer_move(theBoard, comp_letter)
            make_a_move(theBoard, comp_letter, move)
            if is_winner(theBoard, comp_letter):
                game(theBoard)
                score_computer += 1
                print("Alas! The computer has beaten you")
                gameIsplaying = False
            else:
                if check_board_full(theBoard):
                    game(theBoard)
                    score_draw += 1
                    print("It's a draw!")
                    break
                else:
                    turn = "player"

    play_again = input("Do you want to play again? (yes/no): ").lower()
    mydict = {"ATTEMPTS": attempts, "PLAYER": score_player, "COMPUTER": score_computer, "DRAWS": score_draw}
    t = ("SCOREBOARD:".center(20))
    if play_again != "yes":
        if os.path.exists("SCOREBOARD.csv") == True:
            with open("SCOREBOARD.csv", "a") as f:
                writer = csv.DictWriter(f, fieldnames=mydict.keys())
                writer.writerow(mydict)
        else:
            with open("SCOREBOARD.csv", "w") as f:
                heading = ["ATTEMPTS", "PLAYER", "COMPUTER", "DRAWS"]
                csv.writer(f).writerow([t])
                writer = csv.DictWriter(f, fieldnames=heading)
                writer.writeheader()
                writer.writerow(mydict)

        break
    else:
        attempts += 1
'''