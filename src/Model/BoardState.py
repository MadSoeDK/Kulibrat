from __future__ import annotations

from src.Model import Square
from src.Model.BoardModel import BoardModel
from src.Model.Player import Player


class Node(object):
    parent: Node = None
    children: list = None
    eval = None

    def __init__ (self, boardState: BoardState, move: Move, parent: Node):
        self.boardState = boardState
        self.parent = parent


class BoardState(object):
    board: BoardModel = None
    players = [Player for i in range(2)]
    currentPlayer: Player = None
    moves: list = None


class Move(object):
    fromSquare: Square = None
    toSquare: Square = None