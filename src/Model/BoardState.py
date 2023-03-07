from __future__ import annotations

from src.Model.BoardModel import BoardModel


class Node(object):
    parent: Node = None
    children: list = None
    BoardState: BoardState = None
    eval = None

class BoardState(object):
    board: BoardModel = None
    players = [None, None]
    moves: list = None
