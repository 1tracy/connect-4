""" Connect Four """

LOWEST_COLUMN = [0, 0, 0, 0, 0, 0, 0] #when tile is added, index increases
X_COUNT = [[], [], [], [], [], [], []] #stores position of x tiles
O_COUNT = [[], [], [], [], [], [], []] #stores position of o tiles
WINNER = ''

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
        X_COUNT[col-1].append(LOWEST_COLUMN[col-1])
        print(f'X_COUNT: {X_COUNT}')
    else: #ai tile
        O_COUNT[col-1].append(LOWEST_COLUMN[col-1])
        print(f'O_COUNT: {O_COUNT}')

def ai_move():
    """ ai calculate best move, return column """
    print("predict move")
    return 2

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
        #else:
        #    game_over = False
        choice = ai_move()
        fill_slot(choice, 1)

        if is_there_winner():
            print(f'winner is {WINNER}')
            game_over = True
        elif is_board_full():
            print('game ends in a tie')
            game_over = True
        # testing purposes only
        game_over = True

def run_duo():
    """ game code here """
    print("duo game is running")

def is_board_full():
    """ check if board is full """
    print("is board full")

def is_there_winner():
    """ check if there is a winner """
    print("is there winner")

def print_board():
    """ print board """
    print("print board")
    for i in range(7, 0, -1):
        print(i)

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
    mode = get_gamemode()
    run_solo()
    #if mode == "solo":
    #    run_solo()
    #else:
    #    run_duo()

if __name__ == "__main__":
    main()
