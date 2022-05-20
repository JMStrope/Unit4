board = [[1,2,3,], [4,5,6], [7,8,9]]
player = 1
print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
print("---------")
print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
print("---------")
print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")


def check_for_winner():   
    for row in range(len(board)):
        if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
                print("Column Win!")
                return True
        elif board[1][0] == board[1][1] and board[1][1] == board[1][2]:
                print("Column Win!")
                return True
        elif board[2][0] == board[2][1] and board[2][1] == board[2][2]:
                print("Column Win!")
                return True
        
    
    for column in range(len(board)):
        column_values = []
        for row in range(len(board)):
            column_values.append(board[row][column])
        if column_values[0] != " ":
            if column_values[0] == column_values[1] == column_values[2]:
                print("Column win")
                return True
                

    if board[0][0] != " ":
        if board[0][0] == board[1][1] and board[1][1] == board [2][2]:
            print("Diagonal win")
            return True
        

    if board[0][2] != " ":
        if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            print("DIAGONAL WIN")
            print()
            return True

turn = 0
while turn < 9:
    if player == 1:
        current_player = 1
        player_symbol = 'X'
        p1_turn = int(input("p1 pick a number to place your X: "))
        print()
        if p1_turn == 1:
                board[0][0] = player_symbol
        elif p1_turn == 2:
                board[0][1] = player_symbol
        elif p1_turn == 3:
                board[0][2] = player_symbol
        elif p1_turn == 4:
                board[1][0] = player_symbol
        elif p1_turn == 5:
                board[1][1] = player_symbol
        elif p1_turn == 6:
                board[1][2] = player_symbol
        elif p1_turn == 7:
                board[2][0] = player_symbol
        elif p1_turn == 8:
                board[2][1] = player_symbol
        elif p1_turn == 9:
                board[2][2] = player_symbol
        else:
                print("invalid number please try again")

        check_for_winner()

        

        turn += 1


    if check_for_winner():
        print(f"Player {current_player} wins the game!")
        break
        
    
    elif player == 2:
        current_player = 2
        player_symbol = 'O'
        p2_turn = int(input("p2 pick a number to place your 0: "))
        print()
        if p2_turn == 1:
                board[0][0] = player_symbol
        elif p2_turn == 2:
                board[0][1] = player_symbol
        elif p2_turn == 3:
                board[0][2] = player_symbol
        elif p2_turn == 4:
                board[1][0] = player_symbol
        elif p2_turn == 5:
                board[1][1] = player_symbol
        elif p2_turn == 6:
                board[1][2] = player_symbol
        elif p2_turn == 7:
                board[2][0] = player_symbol
        elif p2_turn == 8:
                board[2][1] = player_symbol
        elif p2_turn == 9:
                board[2][2] = player_symbol
        else:
                print("invalid number please try again")
        check_for_winner()


    if check_for_winner():
        print()
        print(f"Player {current_player} wins the game!")
        break

    
    turn += 1 

    #update board
    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("---------")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("---------")
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")

    if player == 1:
        player = 2
    else:
        player = 1
print("GAME OVER")
