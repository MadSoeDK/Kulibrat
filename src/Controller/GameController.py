from src.Controller.AiController import Problem, best_first_search
from src.Model.BoardModel import BoardModel
from src.Model.BoardState import BoardState
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

        # Check if player didn't select their own piece
        if self.fromSquare.owner is not self.currentPlayer:
            return False

        # Home run! currentPlayer have gotten a piece home and gets a point.
        # Check if pieces are at the last row and the correct button is pressed
        if ((self.currentPlayer is self.players[0]) and (self.board.squares.index(self.toSquare) == 12)) or (
                self.currentPlayer is self.players[1] and self.board.squares.index(self.toSquare) == 13):
            return self.home_run()

        squares = self.board.squares
        fromColumn = squares.index(self.fromSquare) % 3
        toColumn = squares.index(self.toSquare) % 3
        differenceInRow = int(squares.index(self.fromSquare) / 3) - int(squares.index(self.toSquare) / 3)
        squareIsEmpty = self.toSquare.owner is None

        # Diagonal move. currentPlayer has to move forward, and in a new column. The toSquare must be empty.
        if toColumn is not fromColumn and differenceInRow == (1 if self.currentPlayer is self.players[0] else -1) and squareIsEmpty and abs(fromColumn-toColumn) == 1:
            self.move()
            return True

        # Attack or move forward. currentPlayer has to move forward on a square that is not his own.
        if (fromColumn == toColumn) and differenceInRow == (1 if self.currentPlayer is self.players[0] else -1) and self.fromSquare.owner is not self.toSquare.owner and self.toSquare.owner is not None:
            self.attack()
            return True


        # TODO: Jump move
        if fromColumn is toColumn and abs(differenceInRow) > 1 and squareIsEmpty:

            # Set up variables for loop
            _allowJump = True
            if differenceInRow > 0:
                _direction = 1
            else:
                _direction = -1

            # Check if the jump is legal
            for x in range(1, _direction*differenceInRow):
                if self.board.get_square(self.board.squares.index(self.fromSquare) - 3*x*_direction).owner is self.currentPlayer and not None:
                    _allowJump = False

            # If jump is legal, then jump
            if (_allowJump):
                self.move()

            return _allowJump

        # Default return for now (only because not all cases are accounted for yet
        return False

    def home_run(self):
        # Black has to be at the top row, or white at the bottom row
        if (self.currentPlayer is self.players[0] and 0 <= self.board.squares.index(self.fromSquare) <= 2) or (
                self.currentPlayer is self.players[1] and 9 <= self.board.squares.index(self.fromSquare) <= 11):
            self.fromSquare.owner = None
            self.currentPlayer.points += 1
            return True

        if self.currentPlayer == self.players[0]:
            if self.recursive_goal(int(self.board.squares.index(self.fromSquare) % 3)):
                self.fromSquare.owner = None
                self.currentPlayer.points += 1
                return True
        else:
            if self.recursive_goal(int(self.board.squares.index(self.fromSquare) % 3) + 9):
                self.fromSquare.owner = None
                self.currentPlayer.points += 1
                return True

        # Other cases not allowed
        return False

    def recursive_goal(self, current_square_index) -> bool:
        if self.board.squares.index(self.fromSquare) == current_square_index:
            return True
        if self.board.squares[current_square_index].owner is None or self.board.squares[current_square_index].owner is self.currentPlayer:
            return False
        return self.recursive_goal(current_square_index + 3 if self.currentPlayer is self.players[0] else current_square_index - 3)

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

        # self.AIController() TODO: Does not work yet
        self.nextPlayer()

    def AIController(self):
        problem = Problem(BoardState(self.board, self.players, self.currentPlayer))
        node = best_first_search(problem)
        print(node)


