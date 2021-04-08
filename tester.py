import tictactoe as ttt
from os import system


def print_board(b):
    # print the top line
    print("-------------")
    for row in range(3):
        for col in range(3):
            value = " " if b[row][col] is None else b[row][col]
            print('|', value, end=' ')
        print('|')
        print("-------------")


def clear():
    system('clear')


board = ttt.initial_state()
clear()
print('Enter an option.')
print('1. Play as X (go first)')
print('2. Play as O')
choice = int(input("Your choice: "))
human = 'X' if choice == 1 else 'O'
ai = 'O' if choice == 1 else 'X'

clear()
print_board(board)


while not ttt.terminal(board):
    if ttt.player(board) == human:
        row = int(input("Enter the row: "))
        col = int(input("Enter the column: "))

        if board[row][col] is None:
            board[row][col] = human
            clear()
            print_board(board)
        continue

    if ttt.player(board) == ai:
        print("waiting for AI...")
        cell = ttt.minimax(board)
        board[cell[0]][cell[1]] = ai
        clear()
        print("AI made the move")
        print_board(board)

winner = ttt.winner(board)
if winner == human:
    print("YOU WIN")
elif winner == ai:
    print("AI WIN")
else:
    print("TIE GAME")








