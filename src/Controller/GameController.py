from src.Model.BoardModel import BoardModel


class GameController(object):
    currentPlayer = 0

    def __init__(self):
        self.board = BoardModel()

    def get_owner(self, num):
        return self.board.get_square(num).get_owner()

    def get_input(self):
        square = input('Select square to move from ')
        to_move = input('Select square to move to ')
        print(square, to_move)
        return

    # Check if the move is valid and if so moves the piece
    def move(self):
        return

    def insert_piece(self):
        return

    def diagonal_move(self):
        return

    def attack(self):
        return

    def jump(self):
        return

