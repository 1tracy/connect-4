""" Connect Four """

class Game:
    """ main interface """
    def __init__(self, gamemode):
        """ init """
        self._lowest_column = [0, 0, 0, 0, 0, 0, 0] #when tile is added, index increases
        self.gamemode = gamemode

    def choose_column(self, column):
        """ fills lowest spot in column """

    def run(self):
        """ game code here """




class Player(Game):
    """ player interface """
    def fcn(self):
        """docstring"""
        print('player initialized')

def get_gamemode():
    """ get gamemode """
    mode = str(input("type \'solo\' to play alone or \'duo\' to play against another player.\n"))
    while mode not in ('duo', 'solo'):
        print("type either solo or duo")
        mode = str(input("type \'solo\' to play alone or \'duo\' to play against other players\n"))
    return mode


def main():
    """ main function """
    print("Connect Four")
    print("Make sure to view the rules in the README file before playing!")
    mode = get_gamemode()
    print(mode)
    #Game.run(mode)

if __name__ == "__main__":
    main()
