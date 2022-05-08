from input_types import avaible_input_types
player1_choices=[]
player2_choices=[]
list_of_moves=[]
x_o = ["1", "2", "3",
       "4", "5", "6",
       "7", "8", "9"]
def player1choose():
    print("player 1 chooce")
    player1_choice=int(input())
    if player1_choice in avaible_input_types:
        if player1_choice not in list_of_moves:
            player1_choices.append(player1_choice)
            list_of_moves.append(player1_choice)
            x_o[player1_choice-1]="X"
        else: print("it was not a good choice player 2 will choose now")
    else: print("it was not a good choice player 2 will choose now")
def player2choose():
    print("player 2 chooce")
    player2_choice=int(input())
    if player2_choice in avaible_input_types:
        if player2_choice not in list_of_moves:
            player2_choices.append(player2_choice)
            list_of_moves.append(player2_choice)
            x_o[player2_choice-1]="0"
        else: print("it was not a good choice player 1 will choose now")
    else: print("it was not a good choice player 1 will choose now")
def restart():
    player1_choices = []
    player2_choices = []
    list_of_moves = []
    x_o = ["1", "2", "3",
           "4", "5", "6",
           "7", "8", "9"]
