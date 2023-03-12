from __future__ import annotations

from src.Model import Square
from src.Model.BoardModel import BoardModel
from src.Model.Player import Player


class Node(object):
    # state: The current board state
    # parent: the node in the tree that generated this node
    # action: the action that was applied to the parents state to generate this node
    # The total cost of the path from the initial state to this node
    def __init__(self, state: BoardState, parent: Node = None, action: Action = None, path_cost: int = None):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost


class BoardState(object):
    board: BoardModel = None
    players = [Player for i in range(2)]
    currentPlayer: Player = None


class Action(object):
    def __init__(self, s1: Square, s2: Square):
        self.fromSquare = s1
        self.toSquare = s2
