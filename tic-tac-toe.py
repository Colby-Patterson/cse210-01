#Assignment: CSE 210-01 Author: Colby Patterson

def main():
    board = {'1': '1' , '2': '2' , '3': '3' , '4': '4' , '5': '5' , '6': '6' , '7': '7' , '8': '8' , '9': '9' }
    display_board(board)


def display_board(board):
    print(board['1'] + "|" + board['2'] + "|" + board['3'])
    print("-+-+-")
    print(board['4'] + "|" + board['5'] + "|" + board['6'])
    print("-+-+-")
    print(board['7'] + "|" + board['8'] + "|" + board['9'])

def check_win():
    pass

if __name__ == "__main__":
    main()
