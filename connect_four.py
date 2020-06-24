""" Connect Four """

LOWEST_COLUMN = [0, 0, 0, 0, 0, 0, 0] #when tile is added, index increases
WINNER = ''
GAMEBOARD = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
TEST_GAMEBOARD = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
def print_board():
    """ print board """
    print("print board")
    for i in range(6):
        for j in range(6):
            print("| "+GAMEBOARD[i][j]+ " ", end="")
        print("|"+GAMEBOARD[i][5], end="")
        print(GAMEBOARD[i][6]+" |", end="\n")
        print("-"*29)

def is_empty(slot):
    """ check if slot is empty """
    if slot == "":
        return True
    return False

def choose_column():
    """ choose column to drop tile in """
    response = input("choose column (1~7)")
    while response not in ['1', '2', '3', '4', '5', '6', '7']:
        print("column must be between 1~7 inclusive\n")
        response = input("choose column (1~7)")
    return int(response)

def fill_slot(col, num):
    """ fill lowest slot on column specified """
    LOWEST_COLUMN[col-1] += 1
    if num == 0: #player tile
        GAMEBOARD[(6-LOWEST_COLUMN[col-1])][col-1] = 'X'
    else: #ai tile
        GAMEBOARD[(6-LOWEST_COLUMN[col-1])][col-1] = 'O'
    print_board()

def ai_move():
    """ ai calculate best move, return column """
    print("predict move")
    #iterate through rows, then columns

    #horizontal
    for row in range(len(GAMEBOARD)):
        for column in range(6):
            print("row/column", row, column)
            if GAMEBOARD[row][column] == "O" and LOWEST_COLUMN[column] < 6:
                if is_empty(GAMEBOARD[row][column+1]):
                    return column+1
    #vertical
    for row in range(len(GAMEBOARD)-1):
        for column in range(7):
            print("row/column", row, column)
            if GAMEBOARD[row][column] == "O" and LOWEST_COLUMN[column] < 6:
                if is_empty(GAMEBOARD[row+1][column]):
                    return column
    #diagonal up
    for row in range(1, len(GAMEBOARD)):
        for column in range(6):
            print("row/column", row, column)
            if GAMEBOARD[row][column] == "O" and LOWEST_COLUMN[column] < 6:
                if is_empty(GAMEBOARD[row-1][column+1]):
                    return column+1
    #diagonal down
    for row in range(len(GAMEBOARD)-1):
        for column in range(6):
            print("row/column", row, column)
            if GAMEBOARD[row][column] == "O" and LOWEST_COLUMN[column] < 6:
                if is_empty(GAMEBOARD[row+1][column+1]):
                    return column+1
    #return random move
    for column in LOWEST_COLUMN:
        if column < 6:
            return column

def run_solo():
    """ game code here """
    print("solo game is running")
    game_over = False
    while not game_over:
        #print the board
        print_board()

        choice = choose_column()
        fill_slot(choice, 0)

        if is_there_winner():
            print(f'winner is {WINNER}')
            game_over = True
        elif is_board_full():
            print('game ends in a tie')
            game_over = True
        else:
            game_over = False
        choice = ai_move()
        fill_slot(choice, 1)

        if is_there_winner():
            print(f'winner is {WINNER}')
            game_over = True
        elif is_board_full():
            print('game ends in a tie')
            game_over = True
        # testing purposes only
        #game_over = True

def run_duo():
    """ game code here """
    print("duo game is running")

def is_board_full():
    """ check if board is full """
    print("is board full")
    return False

def is_there_winner():
    """ check if there is a winner """
    print("is there winner")
    return False

def get_gamemode():
    """ get gamemode """
    mode = str(input("type \'solo\' to play alone or \'duo\' to play against another player.\n"))
    while mode not in ('duo', 'solo'):
        print("type either solo or duo")
        mode = str(input("type \'solo\' to play alone or \'duo\' to play against other players\n"))
        return mode

def main():
    """ main function """
    print("\nConnect Four\n")
    print("Make sure to view the rules in the README file before playing!\n")
    #mode = get_gamemode()
    run_solo()
    #if mode == "solo":
    #    run_solo()
    #else:
    #    run_duo()

if __name__ == "__main__":
    main()
