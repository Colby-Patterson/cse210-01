#Assignment: CSE 210-01 Author: Colby Patterson

def main():
    board = {'1': '1' , '2': '2' , '3': '3' , '4': '4' , '5': '5' , '6': '6' , '7': '7' , '8': '8' , '9': '9' }
    current_player = "x"
    turn_count = 0
    
    while turn_count < 9:
        display_board(board)
        current_move = input("Select a number " + current_player + ": ")
        board[current_move] = current_player
        turn_count += 1
        print("")
        
        
        check = check_win(turn_count, board)
        if check == "Win":
            display_board(board)
            print(current_player + " wins!")
            break
        
        elif check == "Draw":
            display_board(board)
            print("It's a draw!")
        
        
        if current_player == "x":
            current_player = "o"
            
        elif current_player == "o":
            current_player = "x"
        


def display_board(board):
    print(board['1'] + "|" + board['2'] + "|" + board['3'])
    print("-+-+-")
    print(board['4'] + "|" + board['5'] + "|" + board['6'])
    print("-+-+-")
    print(board['7'] + "|" + board['8'] + "|" + board['9'])

def check_win(turn_count, board):
    if turn_count >= 3:
        if board['1'] == board['2'] == board['3'] or board['4'] == board['5'] == board['6'] or board['7'] == board['8'] == board['9']:
            return "Win"
        
        elif board['1'] == board['4'] == board['7'] or board['2'] == board['5'] == board['8'] or board['3'] == board['6'] == board['9']:
            return "Win"
        
        elif board['1'] == board['5'] == board['9'] or board['3'] == board['5'] == board['7']:
            return "Win"
        
        elif turn_count == 9:
            return "Draw"
        
if __name__ == "__main__":
    main()