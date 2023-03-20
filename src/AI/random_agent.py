import random

from src.AI.min_max_DFS import actions
from src.Model.BoardState import BoardState


def random_agent(state: BoardState):
    return random.choice(actions(state))
