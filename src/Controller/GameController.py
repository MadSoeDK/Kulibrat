from src.Model.BoardModel import BoardModel
from src.Model.Player import Player


class GameController(object):

    def __init__(self):
        self.board = BoardModel()
        self.players = [Player("black"), Player("red")]
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
        self.toSquare = self.currentPlayer

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

    # Method called by view
    def click(self, square_index):
        if square_index == 13 or square_index == 14:
            return
        if self.fromSquare is None:
            self.fromSquare = self.board.squares[square_index-1]
            return
        if self.fromSquare is self.board.squares[square_index-1]:
            self.fromSquare = None
            return
        self.toSquare = self.board.squares[square_index-1]

        self._is_move_legal()
        self.fromSquare = None
        self.toSquare = None
