from src.Model.BoardModel import BoardModel
from src.Model.Player import Player


class GameController(object):

    def __init__(self):
        self.board = BoardModel()
        self.players = [Player(), Player()]
        self.toSquare = None
        self.fromSquare = None

        # 0 = Black Player, 1 = Red Player
        self.currentPlayer = self.players[0]

    def get_input(self):
        square = input('Select square to move from ')
        to_move = input('Select square to move to ')
        print(square, to_move)
        return

    # Check if the move is valid and if so moves the piece
    def _is_move_legal(self):
        return

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


#Method called by view
    def click(self, square):
        self

    def squareState(self, index):
        if index > 13:
            return None
        return self.board.squares[index]


