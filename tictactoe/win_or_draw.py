from players_choices import *
def who_win():
    global draw2
    matrix = [x_o[i:i+3] for i in range(0, len(x_o), 3)]
    for win1,win2,win3 in matrix:
        if(win1==win2==win3=="X"):
            print("player 1 wins")
        elif(win1==win2==win3=="O"):
            print("player 2 wins")
        else: draw1=True
    if x_o[0]==x_o[4]==x_o[8]=="X":
        print("player 1 wins")
    elif x_o[0]==x_o[4]==x_o[8]=="0":
        print("player 2 wins")
    elif x_o[2]==x_o[4]==x_o[6]=="X":
        print("player 1 wins")
    elif x_o[2] == x_o[4] == x_o[6] == "0":
        print("player 2 wins")
    else: draw2=True

    if x_o[0]==x_o[3]==x_o[6]=="X":
        print("player 1 wins")
    elif x_o[1]==x_o[4]==x_o[7]=="X":
        print("player 1 wins")
    elif x_o[2]==x_o[5]==x_o[8]=="X":
        print("player 1 wins")
    elif x_o[0]==x_o[3]==x_o[6]=="0":
        print("player 2 wins")
    elif x_o[1]==x_o[4]==x_o[7]=="0":
        print("player 2 wins")
    elif x_o[2]==x_o[5]==x_o[8]=="0":
        print("player 2 wins")
    else: draw3=True
    if draw3==draw2==draw1==True:
        print("it was a draw you want to play again?")
