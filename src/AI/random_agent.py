import random

from src.Controller.MoveController import possibleMoves
from src.Model.BoardState import BoardState


def random_agent(state: BoardState):
    return random.choice(possibleMoves(state))
