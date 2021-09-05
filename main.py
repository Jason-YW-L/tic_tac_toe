"""This is a tic-tac-toe game
"""

"""This is a tic-tac-toe game
"""
BOARD_SIZE = 3


class Player:
    def __init__(self, name):
        self.name = name

    def move(self, b):
        # asks user for x-y coordinates
        row = int(input("Please enter the row of your move"))
        col = int(input("Please enter the column of your move"))
        # while loop
        while b.board[row][col] == " ":
            print("Invalid input, please try again.")
            row = int(input("Please enter the row of your move"))
            col = int(input("Please enter the column of your move"))
        # update board
        b.board[row][col] = self.name
        board.count += 1


class Board:
    def __init__(self):
        self.board = []
        self.count = 0
        # TODO
        # initialize board

    def display_board(self):


# TODO
# display board


def check_winner(b, curr_player):
    """
    :param b:
    :param curr_player:
    :return: return True if current player win
    """
    # check horizontal
    if b.board[0][0] == b.board[0][1] == b.board[0][2] == curr_player or \
        b.board[1][0] == b.board[1][1] == b.board[1][2] == curr_player or \
        b.board[2][0] == b.board[2][1] == b.board[2][2] == curr_player:
        return curr_player
    # check vertical
    elif b.board[0][1] == b.board[1][1] == b.board[2][1] == curr_player or \
            b.board[0][0] == b.board[1][0] == b.board[2][0] == curr_player or \
            b.board[0][2] == b.board[1][2] == b.board[2][2] == curr_player:
        return curr_player
    # check diagonal
    elif b.board[0][0] == b.board[1][1] == b.board[2][2] == curr_player or\
        b.board[0][2] == b.board[1][1] == b.board[2][0] == curr_player:
        return curr_player
    return False

def check_full(b):
    if board.count == 9:
        return True
    return False


if "__main__" == __name__:

    p1 = Player("1")
    p2 = Player("2")
    board = Board()

    curr_player = p1

    while not check_winner(board, curr_player) and not check_full(board):
        pass

