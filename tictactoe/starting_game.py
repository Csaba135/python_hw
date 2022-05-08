import os
from win_or_draw import *
def start_game():
    matrix = [x_o[i:i + 3] for i in range(0, len(x_o), 3)]
    for l in matrix:
        print(l)
    while(len(list_of_moves)<9):
        player1choose()
        matrix = [x_o[i:i+3] for i in range(0, len(x_o), 3)]
        for l in matrix:
            print(l)
        if len(list_of_moves)==9:
            break
        player2choose()
        matrix = [x_o[i:i+3] for i in range(0, len(x_o), 3)]
        for l in matrix:
            print(l)
    if len(list_of_moves)==9:
        print("Game ended")
        print(list_of_moves)
    who_win()
    play_again=str(input())
    if play_again=="Yes":
        restart()
        start_game()
    else:exit()
