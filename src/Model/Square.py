from src.Model.Player import Player


class Square(object):
    def __init__(self):
        self.selected = False
        self.owner: Player = None

