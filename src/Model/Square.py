from src.Model.Player import Player


class Square(object):
    def __init__(self, num):
        self.selected = False
        self.owner: Player = None
        self.num = num

