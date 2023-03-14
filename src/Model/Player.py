class Player(object):
    def __init__(self, color, points: int = 0, pieces: int = 4):
        self.color = color
        self.points: int = points
        self.pieces = pieces
