from src.AI.min_max_DFS import pruning_start, actions
from src.AI.random_agent import random_agent
from src.AI.tree_search import Problem, best_first_search
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
        self.game_mode_hard = True
        self.game_active = True

        # 0 = Black Player, 1 = Red Player
        self.currentPlayer = self.players[0]

        self.moves = actions(BoardState(self.board, self.players, self.currentPlayer))

    # Check if the move is valid and if so moves the piece
    def nextPlayer(self, count: int):
        if count == 0:
            self.fromSquare = None
            self.toSquare = None
        if count == 2:
            self.gameOver()
        self.currentPlayer = self.players[(self.players.index(self.currentPlayer) + 1) % 2]
        self.moves = actions(BoardState(self.board, self.players, self.currentPlayer))
        if not self.moves:
            self.nextPlayer(count + 1)

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

        for move in self.moves:
            if move.fromSquare is self.fromSquare and move.toSquare is self.toSquare:
                if self.board.squares.index(self.toSquare) > 11:
                    self.currentPlayer.points += 1
                    if self.currentPlayer.points == 5:
                        self.gameOver()
                self.fromSquare.owner = None
                self.toSquare.owner = self.currentPlayer
                self.nextPlayer(0)

    def gameOver(self):
        self.game_active = False

    def restart(self):

        for Player.Square in self.board.squares:
            Player.Square.owner = None

        self.players[0].points = 0
        self.players[1].points = 0

    def AI_turn(self):
        if self.currentPlayer is self.players[1]:
            if self.game_mode_hard:
                red_move = pruning_start(BoardState(self.board, self.players, self.currentPlayer),
                                         self.players.index(self.currentPlayer), self.moves)
            else:
                red_move = random_agent(BoardState(self.board, self.players, self.currentPlayer))
            red_move.fromSquare.owner = None
            red_move.toSquare.owner = self.currentPlayer
            if self.board.squares.index(red_move.toSquare) == 13:
                self.currentPlayer.points += 1
            self.nextPlayer(0)
