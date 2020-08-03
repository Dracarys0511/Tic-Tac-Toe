def display_board(board):
    print("   {}    |    {}    |    {}  ".format(board[6],board[7],board[8]))
    print("________|_________|________")
    print("   {}    |    {}    |    {}  ".format(board[3],board[4],board[5]))
    print("________|_________|________")
    print("   {}    |    {}    |    {}  ".format(board[0],board[1],board[2]))
    print("        |         |        ")

def player_input():
    mark = 1
    while mark != "O":
        mark = input("Select your marker(X or O) : ")
        if mark == "X":
            break
        if mark != "O":
            print("Please enter a valid choice that is, X or O")
    return mark
def place_marker(board, marker, position):
    board[position-1]=marker
def win_check(board, mark):
    win=False
    if board[0]==board[1] == board[2]==mark:
        win=True
    elif board[3]==board[4]== board[5]==mark:
        win=True
    elif board[6]==board[7] ==board[8]==mark:
        win=True
    elif board[0]==board[3]==board[6]==mark:
        win=True
    elif board[1]==board[4]== board[7]==mark:
        win=True
    elif board[2]==board[5]==board[8]==mark:
        win=True
    elif board[0]== board[4]==board[8]==mark:
        win=True
    elif board[2]==board[4]==board[6]==mark:
        win=True
    else:
        win=False
    return win
import random
def choose_first():
    a=random.randint(1,2)
    return a
def space_check(board, position):
    return board[position-1]==" "
def full_board_check(board):
    flag=0
    for i in board:
        if i==" ":
            flag=1
            break
    return flag==0
def player_choice(board):
    flag=0
    g=0
    while flag==0:
        while g==0:
            new_choice=input("Enter the position on which you want to place your marker (1-9): ")
            if new_choice in ["1","2","3","4","5","6","7","8","9"]:
                break
            else:
                print("It's not a valid position enter a valid position(1-9)")
        new_choice=int(new_choice)
        if space_check(board,new_choice):
            flag=1
            g=1
            return new_choice
        else:
            print("Sorry, the position of your choice is not empty. Please enter another position.")
def replay():
    g=1
    while g==1:
        choice=input("Do you want to play again?(Y or N) : ")
        if choice=="Y":
            return True
            break
        elif choice=="N":
            return False
            break
        else:
            g=1
            print("Enter a valid choice")
print('Welcome to Tic Tac Toe!')
while True:
    board=[" "," "," "," "," "," "," "," "," "]
    display_board(board)
    print("Player {} will choose marker first".format(choose_first()))
    marker=player_input()
    if marker=="O" and choose_first()==1:
        marker1="O"
        marker2="X"
    elif marker=="O" and choose_first()==2:
        marker1="X"
        marker2="O"
    elif marker=="X" and choose_first()==1:
        marker1="X"
        marker2="O"
    elif marker=="X" and choose_first()==2:
        marker1="O"
        marker2="X"
    game_on=True
    print('\n'*100)
    while game_on:
        display_board(board)
        print("Player 1 turn: ")
        c1=player_choice(board)
        place_marker(board,marker1,c1)
        display_board(board)
        if win_check(board,marker1):
            print("\n"*100)
            display_board(board)
            print("Congratulations! Player 1 has WON ")
            break
        elif full_board_check(board):
            print("\n"*100)
            display_board(board)
            print("It's a DRAW")
            break
        else:
            print('\n'*100)
        display_board(board)
        print("Player 2 turn: ")
        c2=player_choice(board)
        place_marker(board,marker2,c2)
        display_board(board)
        if win_check(board,marker2):
            print("\n"*100)
            display_board(board)
            print("Congratulations! Player 2 has WON ")
            break
        else:
            print('\n'*100)
    if not replay():
        break
    print('\n'*100)