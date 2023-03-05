from src.Model.BoardModel import BoardModel
from src.Model.Player import Player
from src.Model.Square import Square


class GameController(object):

    def __init__(self):
        self.board = BoardModel()
        self.players = [Player("black"), Player("red")]
        self.toSquare: Square = None
        self.fromSquare: Square = None

        # 0 = Black Player, 1 = Red Player
        self.currentPlayer = self.players[0]

    # Check if the move is valid and if so moves the piece
    def _is_move_legal(self) -> bool:
        # Spawn new piece control. Check that the correct button for the currentPlayer has been pressed.
        if ((self.currentPlayer is self.players[0]) and (self.board.squares.index(self.fromSquare) == 13)) or (
                self.currentPlayer is self.players[1] and self.board.squares.index(self.fromSquare) == 12):
            return self.insert_piece()

        # Checks if player didn't select their own piece
        if self.fromSquare.owner is not self.currentPlayer:
            return False

        squares = self.board.squares
        fromColumn = squares.index(self.fromSquare) % 3
        toColumn = squares.index(self.toSquare) % 3
        differenceInRow = int(squares.index(self.fromSquare) / 3) - int(squares.index(self.toSquare) / 3)
        squareIsEmpty = self.toSquare.owner is None

        # Diagonal move. currentPlayer has to move forward, and in a new column. The toSquare must be empty.
        if toColumn is not fromColumn and differenceInRow == (1 if self.currentPlayer is self.players[0] else -1) and squareIsEmpty:
            self.move()
            return True

        if (fromColumn == toColumn) and differenceInRow == (1 if self.currentPlayer is self.players[0] else -1) and self.fromSquare.owner is not self.toSquare.owner:
            self.attack()
            return True


        # Default return for now (only because not all cases are accounted for yet
        return False

    def move(self):
        self.fromSquare.owner = None
        self.toSquare.owner = self.currentPlayer

    # Method for controlling piece insertion on the board. Checks all cases.
    # Returns true if legal move, false if move is not legal.
    def insert_piece(self) -> bool:
        # Count number of pieces on the board of currentPlayer
        count = 0
        for i in range(12):
            if self.board.squares[i].owner is self.currentPlayer:
                count += 1

        # Max no. of 4 pieces allowed on the board
        if count >= 4:
            return False

        # If the square is occupied by another piece
        if self.toSquare.owner is not None:
            return False

        # Black has to spawn a piece at the top row
        if self.currentPlayer is self.players[0] and 9 <= self.board.squares.index(self.toSquare) <= 11:
            self.toSquare.owner = self.currentPlayer
            return True

        # White has to spawn a piece at the bottom row
        elif self.currentPlayer is self.players[1] and 0 <= self.board.squares.index(self.toSquare) <= 2:
            self.toSquare.owner = self.currentPlayer
            return True

        # All other cases is not allowed for inserting a piece
        return False

    def diagonal_move(self):
        return

    def attack(self):
        self.fromSquare.owner = None
        self.toSquare.owner = self.currentPlayer

    def jump(self):
        return

    def nextPlayer(self):
        self.fromSquare = None
        self.toSquare = None
        self.currentPlayer = self.players[(self.players.index(self.currentPlayer) + 1) % 2]

    # Method called by view
    def click(self, square_index):
        if self.fromSquare is None:
            self.fromSquare = self.board.squares[square_index - 1]
            return
        if self.fromSquare is self.board.squares[square_index - 1]:
            self.fromSquare = None
            return
        else:
            self.toSquare = self.board.squares[square_index - 1]

        if self._is_move_legal() is False:
            self.fromSquare = None
            self.toSquare = None
            return
        self.nextPlayer()
